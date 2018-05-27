import requests #requests module need to be added using pip, need to run this file in python 3

import json  #library for json(JavaScript Object Notation)

api_address = 'http://openweathermap.org/data/2.5/weather?appid=b6907d289e10d714a6e88b30761fae22&q='
city = input("City Name:")

url = api_address + city

json_data = requests.get(url).json()

#print(json_data)
#print(type(json_data)) #prints the datatype of variable

visibility = json_data['visibility']
place =  json_data['name']

wind  = json_data['wind']
degree = wind['deg']
speed = wind['speed']

main = json_data['main']
temp = main['temp']
tempMin = main['temp_min']
tempMax = main['temp_max']
Humidity = main['humidity']

print("Place:",place,"\n\r")

print("wind:",degree , "deg" , "at", speed ,"km/hr\n\r")

print("current temperature:",temp ,"deg C\n\r")
print("max temperature:",tempMax , "deg C\n\r")
print("min temperature:",tempMin , "deg C\n\r")
print("Humidity:",Humidity ,"%\n\r")



