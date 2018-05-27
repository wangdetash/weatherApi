import requests #requests module need to be added using pip, need to run this file in python 3

import json  #library for json(JavaScript Object Notation)

api_address = 'http://openweathermap.org/data/2.5/weather?appid=b6907d289e10d714a6e88b30761fae22&q='
city = input("City Name:")

url = api_address + city

json_data = requests.get(url).json()

#print(json_data)
#print(type(json_data)) #prints the datatype of variable

place =  json_data['name']
print("Place:",place,"\n\r")

print("********coordinates********************************************************")
coordinates = json_data['coord']
longitude = coordinates['lon']
latitude = coordinates['lat']
print("longitude:",longitude)
print("latitude:",latitude)

print("********wind***************************************************************")
wind  = json_data['wind']
degree = wind['deg']
speed = wind['speed']
print("wind:",degree , "deg" , "at", speed ,"km/hr\n\r")

print("*******temperature*********************************************************")
main = json_data['main']
temp = main['temp']
tempMin = main['temp_min']
tempMax = main['temp_max']
Humidity = main['humidity']
print("current temperature:",temp ,"deg C\n\r")
print("max temperature:",tempMax , "deg C\n\r")
print("min temperature:",tempMin , "deg C\n\r")
print("Humidity:",Humidity ,"%\n\r")









