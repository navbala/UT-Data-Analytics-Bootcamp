# import Dependencies
import requests as req
import json
from citipy import citipy
import random

# Generate random lng/lat to put into citipy (citipy take in 2 coordinates)


### Use the cities obtained via citipy and get weather from openweather API
# test using manully input cities first
 # Example url
 #api.openweathermap.org/data/2.5/weather?q={city name}


# Save config information
api_key = "84fe59f3ffa1bf7920c39149bf3dde70"
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "London"

# Build query URL
query_url = url + "appid=" + api_key + "&q=" + city + "&units=imperial"

# Get weather data
weather_response = req.get(query_url)
weather_json = weather_response.json()

# Get the temperature/other readings from the response
print(query_url)
print()
print("The temperature in London is: " + str(weather_json["main"]["temp"]) + ".")
