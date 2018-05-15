
# WeatherPy
## Analysis
 - The closer a city is to the equator, the higher the temperature (F) of that city. This is noted in the "City Latitude vs. Temperature (3/1/2018)" graph, below, where the highest data points for temperature are above the "0" latitude (note that the equator is at latitude 0).
 - The Northern Hemisphere typically has higher wind speeds (mph). This is indicated in the "City Latitude vs. Wind Speed (3/1/2018)" graph where the data points for wind speed for cities in the Nothern Hemisphere (latitudes 0 to 90) are higher than for cities in the Southern Hemisphere (latitude -90 to 0).
 - The Southern Hemisphere typically has higher humidity %). This is indicated in the "City Latitude vs. Humidity (3/1/2018)" graph where there is greater number of data points with higher humidty for cities in the Souther Hemisphere (latitudes -90 to 0) than for cities in the Northern Hemisphere (latitude 0 to 90).
  


```python
# Import Dependencies
import requests as req
import json
from citipy import citipy
from random import uniform
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
# API config and URL info
api_key = "84fe59f3ffa1bf7920c39149bf3dde70"
url = "http://api.openweathermap.org/data/2.5/weather?"
```


```python
## Generate random lng/lat to put into citipy (citipy take in 2 coordinates (lng, lat))

# Functions for generating random latitude
def rand_lat():
  return uniform(-90, 90)

# Function for generating random longitude
def rand_lng():
  return uniform(-180,180)
```


```python
# Create empty df to hold weather data for each city 
weather_data_df = pd.DataFrame(columns=["City", "Cloudiness", "Country", "Date", "Humidity", "Lat", "Lng", "Temperature", "Wind Speed"])

# Create initial variables for looping
counter = 0
unique_cities = []

# Initial print header for output log
print("Beginning Data Retrieval")
print("---------------------------")

# While loop to only capture cities without null weather data
while counter < 500:
    # Retrieve a city for each random lat/lng generated
    # Obtain the JSON response for each city
    city = citipy.nearest_city(rand_lat(), rand_lng())
    query_url =  url + "appid=" + api_key + "&q=" + city.city_name + "," + city.country_code + "&units=imperial"
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    
    # If statement for only cities with weather data (internal paramer "cod" = 200)
    if weather_json["cod"] == 200:
        # Check for duplicates
        if weather_json["name"] not in unique_cities:
            # Append weather data for the city to df
            weather_data_df = weather_data_df.append([{"City": weather_json["name"],
                                                       "Temperature": weather_json["main"]["temp"],
                                                       "Humidity": weather_json["main"]["humidity"],
                                                       "Cloudiness": weather_json["clouds"]["all"],
                                                       "Wind Speed": weather_json["wind"]["speed"],
                                                       "Lat": weather_json["coord"]["lat"],
                                                       "Country": weather_json["sys"]["country"],
                                                       "Lng": weather_json["coord"]["lon"],
                                                       "Date": weather_json["dt"]
                                                      }])
            
            # Add to city-weather data confirmed counter         
            counter += 1
            
            # Append the city to the unique cities list
            unique_cities.append(weather_json["name"])
        
            # Print log statements
            print("Processing Record #" + str(counter) + " | City ID: " + str(weather_json["id"]) + " | City Name: " + city.city_name)
            print(query_url)

```

    Beginning Data Retrieval
    ---------------------------
    Processing Record #1 | City ID: 2077963 | City Name: albany
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=albany,au&units=imperial
    Processing Record #2 | City ID: 2163355 | City Name: hobart
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hobart,au&units=imperial
    Processing Record #3 | City ID: 3361934 | City Name: saldanha
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saldanha,za&units=imperial
    Processing Record #4 | City ID: 5380437 | City Name: pacific grove
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pacific grove,us&units=imperial
    Processing Record #5 | City ID: 3833367 | City Name: ushuaia
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ushuaia,ar&units=imperial
    Processing Record #6 | City ID: 3652567 | City Name: san cristobal
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=san cristobal,ec&units=imperial
    Processing Record #7 | City ID: 2121385 | City Name: severo-kurilsk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=severo-kurilsk,ru&units=imperial
    Processing Record #8 | City ID: 6185377 | City Name: yellowknife
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yellowknife,ca&units=imperial
    Processing Record #9 | City ID: 1641899 | City Name: labuhan
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=labuhan,id&units=imperial
    Processing Record #10 | City ID: 3652764 | City Name: puerto ayora
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=puerto ayora,ec&units=imperial
    Processing Record #11 | City ID: 4030556 | City Name: rikitea
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=rikitea,pf&units=imperial
    Processing Record #12 | City ID: 5880568 | City Name: bethel
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bethel,us&units=imperial
    Processing Record #13 | City ID: 1006984 | City Name: east london
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=east london,za&units=imperial
    Processing Record #14 | City ID: 1507390 | City Name: dikson
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=dikson,ru&units=imperial
    Processing Record #15 | City ID: 2075265 | City Name: busselton
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=busselton,au&units=imperial
    Processing Record #16 | City ID: 1282256 | City Name: hithadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hithadhoo,mv&units=imperial
    Processing Record #17 | City ID: 2126123 | City Name: chokurdakh
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=chokurdakh,ru&units=imperial
    Processing Record #18 | City ID: 50814 | City Name: wajid
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=wajid,so&units=imperial
    Processing Record #19 | City ID: 2015306 | City Name: tiksi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tiksi,ru&units=imperial
    Processing Record #20 | City ID: 3369157 | City Name: cape town
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cape town,za&units=imperial
    Processing Record #21 | City ID: 3654410 | City Name: manta
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=manta,ec&units=imperial
    Processing Record #22 | City ID: 5072006 | City Name: lincoln
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=lincoln,us&units=imperial
    Processing Record #23 | City ID: 3421982 | City Name: maniitsoq
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=maniitsoq,gl&units=imperial
    Processing Record #24 | City ID: 3883457 | City Name: lebu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=lebu,cl&units=imperial
    Processing Record #25 | City ID: 1737185 | City Name: kapit
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kapit,my&units=imperial
    Processing Record #26 | City ID: 6320062 | City Name: vila velha
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vila velha,br&units=imperial
    Processing Record #27 | City ID: 4035715 | City Name: avarua
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=avarua,ck&units=imperial
    Processing Record #28 | City ID: 2063030 | City Name: port pirie
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port pirie,au&units=imperial
    Processing Record #29 | City ID: 3366880 | City Name: hermanus
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hermanus,za&units=imperial
    Processing Record #30 | City ID: 920233 | City Name: chibombo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=chibombo,zm&units=imperial
    Processing Record #31 | City ID: 1788452 | City Name: zhucheng
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=zhucheng,cn&units=imperial
    Processing Record #32 | City ID: 4020109 | City Name: atuona
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=atuona,pf&units=imperial
    Processing Record #33 | City ID: 3374346 | City Name: ponta do sol
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ponta do sol,cv&units=imperial
    Processing Record #34 | City ID: 1490256 | City Name: talnakh
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=talnakh,ru&units=imperial
    Processing Record #35 | City ID: 1651531 | City Name: ambon
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ambon,id&units=imperial
    Processing Record #36 | City ID: 6138501 | City Name: saint-augustin
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saint-augustin,ca&units=imperial
    Processing Record #37 | City ID: 955313 | City Name: siyabuswa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=siyabuswa,za&units=imperial
    Processing Record #38 | City ID: 3899539 | City Name: antofagasta
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=antofagasta,cl&units=imperial
    Processing Record #39 | City ID: 1162094 | City Name: ziarat
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ziarat,pk&units=imperial
    Processing Record #40 | City ID: 4031574 | City Name: provideniya
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=provideniya,ru&units=imperial
    Processing Record #41 | City ID: 1258291 | City Name: rayachoti
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=rayachoti,in&units=imperial
    Processing Record #42 | City ID: 2017155 | City Name: saskylakh
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saskylakh,ru&units=imperial
    Processing Record #43 | City ID: 3437920 | City Name: itaquyry
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=itaquyry,py&units=imperial
    Processing Record #44 | City ID: 4252975 | City Name: barrow
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=barrow,us&units=imperial
    Processing Record #45 | City ID: 934322 | City Name: mahebourg
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mahebourg,mu&units=imperial
    Processing Record #46 | City ID: 5969025 | City Name: haines junction
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=haines junction,ca&units=imperial
    Processing Record #47 | City ID: 2125906 | City Name: dukat
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=dukat,ru&units=imperial
    Processing Record #48 | City ID: 2155415 | City Name: new norfolk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=new norfolk,au&units=imperial
    Processing Record #49 | City ID: 3863379 | City Name: mar del plata
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mar del plata,ar&units=imperial
    Processing Record #50 | City ID: 964420 | City Name: port elizabeth
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port elizabeth,za&units=imperial
    Processing Record #51 | City ID: 2122090 | City Name: pevek
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pevek,ru&units=imperial
    Processing Record #52 | City ID: 3418910 | City Name: upernavik
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=upernavik,gl&units=imperial
    Processing Record #53 | City ID: 5848280 | City Name: kapaa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kapaa,us&units=imperial
    Processing Record #54 | City ID: 3370903 | City Name: jamestown
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=jamestown,sh&units=imperial
    Processing Record #55 | City ID: 4021858 | City Name: guerrero negro
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=guerrero negro,mx&units=imperial
    Processing Record #56 | City ID: 212730 | City Name: kisangani
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kisangani,cd&units=imperial
    Processing Record #57 | City ID: 665899 | City Name: stulpicani
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=stulpicani,ro&units=imperial
    Processing Record #58 | City ID: 625721 | City Name: lyuban
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=lyuban,by&units=imperial
    Processing Record #59 | City ID: 2094342 | City Name: kavieng
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kavieng,pg&units=imperial
    Processing Record #60 | City ID: 3421765 | City Name: nanortalik
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nanortalik,gl&units=imperial
    Processing Record #61 | City ID: 6113406 | City Name: prince rupert
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=prince rupert,ca&units=imperial
    Processing Record #62 | City ID: 2017215 | City Name: sangar
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sangar,ru&units=imperial
    Processing Record #63 | City ID: 964432 | City Name: port alfred
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port alfred,za&units=imperial
    Processing Record #64 | City ID: 4034551 | City Name: faanui
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=faanui,pf&units=imperial
    Processing Record #65 | City ID: 6149374 | City Name: slave lake
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=slave lake,ca&units=imperial
    Processing Record #66 | City ID: 86049 | City Name: jalu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=jalu,ly&units=imperial
    Processing Record #67 | City ID: 6167817 | City Name: torbay
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=torbay,ca&units=imperial
    Processing Record #68 | City ID: 536466 | City Name: lebyazhye
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=lebyazhye,ru&units=imperial
    Processing Record #69 | City ID: 2110227 | City Name: butaritari
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=butaritari,ki&units=imperial
    Processing Record #70 | City ID: 5855927 | City Name: hilo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hilo,us&units=imperial
    Processing Record #71 | City ID: 2381334 | City Name: atar
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=atar,mr&units=imperial
    Processing Record #72 | City ID: 3874787 | City Name: punta arenas
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=punta arenas,cl&units=imperial
    Processing Record #73 | City ID: 3896218 | City Name: castro
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=castro,cl&units=imperial
    Processing Record #74 | City ID: 1651103 | City Name: atambua
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=atambua,id&units=imperial
    Processing Record #75 | City ID: 3471451 | City Name: arraial do cabo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=arraial do cabo,br&units=imperial
    Processing Record #76 | City ID: 3372472 | City Name: vila franca do campo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vila franca do campo,pt&units=imperial
    Processing Record #77 | City ID: 1850144 | City Name: nishihara
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nishihara,jp&units=imperial
    Processing Record #78 | City ID: 5372253 | City Name: merced
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=merced,us&units=imperial
    Processing Record #79 | City ID: 3464724 | City Name: diamantino
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=diamantino,br&units=imperial
    Processing Record #80 | City ID: 4032243 | City Name: vaini
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vaini,to&units=imperial
    Processing Record #81 | City ID: 3933104 | City Name: pangoa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pangoa,pe&units=imperial
    Processing Record #82 | City ID: 3846616 | City Name: cordoba
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cordoba,ar&units=imperial
    Processing Record #83 | City ID: 2074865 | City Name: carnarvon
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=carnarvon,au&units=imperial
    Processing Record #84 | City ID: 6165406 | City Name: thompson
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=thompson,ca&units=imperial
    Processing Record #85 | City ID: 6170031 | City Name: tuktoyaktuk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tuktoyaktuk,ca&units=imperial
    Processing Record #86 | City ID: 2181625 | City Name: te anau
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=te anau,nz&units=imperial
    Processing Record #87 | City ID: 2206939 | City Name: bluff
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bluff,nz&units=imperial
    Processing Record #88 | City ID: 64814 | City Name: bandarbeyla
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bandarbeyla,so&units=imperial
    Processing Record #89 | City ID: 2960970 | City Name: westport
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=westport,ie&units=imperial
    Processing Record #90 | City ID: 2070998 | City Name: geraldton
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=geraldton,au&units=imperial
    Processing Record #91 | City ID: 1853140 | City Name: yuza
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yuza,jp&units=imperial
    Processing Record #92 | City ID: 2240449 | City Name: luanda
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=luanda,ao&units=imperial
    Processing Record #93 | City ID: 2124611 | City Name: kholodnyy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kholodnyy,ru&units=imperial
    Processing Record #94 | City ID: 2150163 | City Name: sawtell
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sawtell,au&units=imperial
    Processing Record #95 | City ID: 3995236 | City Name: mulege
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mulege,mx&units=imperial
    Processing Record #96 | City ID: 3397763 | City Name: jacareacanga
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=jacareacanga,br&units=imperial
    Processing Record #97 | City ID: 6050194 | City Name: la sarre
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=la sarre,ca&units=imperial
    Processing Record #98 | City ID: 2966778 | City Name: ballina
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ballina,ie&units=imperial
    Processing Record #99 | City ID: 3573061 | City Name: saint george
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saint george,bm&units=imperial
    Processing Record #100 | City ID: 2455290 | City Name: kidal
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kidal,ml&units=imperial
    Processing Record #101 | City ID: 942470 | City Name: vryheid
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vryheid,za&units=imperial
    Processing Record #102 | City ID: 2109701 | City Name: auki
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=auki,sb&units=imperial
    Processing Record #103 | City ID: 2123814 | City Name: leningradskiy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=leningradskiy,ru&units=imperial
    Processing Record #104 | City ID: 1486321 | City Name: yar-sale
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yar-sale,ru&units=imperial
    Processing Record #105 | City ID: 3372783 | City Name: ponta delgada
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ponta delgada,pt&units=imperial
    Processing Record #106 | City ID: 2514651 | City Name: los llanos de aridane
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=los llanos de aridane,es&units=imperial
    Processing Record #107 | City ID: 1254046 | City Name: tura
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tura,in&units=imperial
    Processing Record #108 | City ID: 2303611 | City Name: axim
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=axim,gh&units=imperial
    Processing Record #109 | City ID: 3033308 | City Name: bernay
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bernay,fr&units=imperial
    Processing Record #110 | City ID: 4467485 | City Name: fuquay-varina
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=fuquay-varina,us&units=imperial
    Processing Record #111 | City ID: 3382160 | City Name: cayenne
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cayenne,gf&units=imperial
    Processing Record #112 | City ID: 933995 | City Name: souillac
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=souillac,mu&units=imperial
    Processing Record #113 | City ID: 2318123 | City Name: yenagoa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yenagoa,ng&units=imperial
    Processing Record #114 | City ID: 3920736 | City Name: chimore
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=chimore,bo&units=imperial
    Processing Record #115 | City ID: 3423146 | City Name: ilulissat
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ilulissat,gl&units=imperial
    Processing Record #116 | City ID: 3868633 | City Name: vallenar
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vallenar,cl&units=imperial
    Processing Record #117 | City ID: 1529651 | City Name: altay
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=altay,cn&units=imperial
    Processing Record #118 | City ID: 2013465 | City Name: verkhoyansk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=verkhoyansk,ru&units=imperial
    Processing Record #119 | City ID: 2128975 | City Name: nemuro
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nemuro,jp&units=imperial
    Processing Record #120 | City ID: 3424607 | City Name: tasiilaq
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tasiilaq,gl&units=imperial
    Processing Record #121 | City ID: 1015776 | City Name: bredasdorp
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bredasdorp,za&units=imperial
    Processing Record #122 | City ID: 6255012 | City Name: flinders
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=flinders,au&units=imperial
    Processing Record #123 | City ID: 2153778 | City Name: parkes
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=parkes,au&units=imperial
    Processing Record #124 | City ID: 260895 | City Name: karpathos
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=karpathos,gr&units=imperial
    Processing Record #125 | City ID: 3860443 | City Name: comodoro rivadavia
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=comodoro rivadavia,ar&units=imperial
    Processing Record #126 | City ID: 2126199 | City Name: cherskiy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cherskiy,ru&units=imperial
    Processing Record #127 | City ID: 5859699 | City Name: college
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=college,us&units=imperial
    Processing Record #128 | City ID: 1500933 | City Name: labytnangi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=labytnangi,ru&units=imperial
    Processing Record #129 | City ID: 2013279 | City Name: vostok
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vostok,ru&units=imperial
    Processing Record #130 | City ID: 3424934 | City Name: saint-pierre
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saint-pierre,pm&units=imperial
    Processing Record #131 | City ID: 2276492 | City Name: harper
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=harper,lr&units=imperial
    Processing Record #132 | City ID: 3394023 | City Name: natal
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=natal,br&units=imperial
    Processing Record #133 | City ID: 2140558 | City Name: koumac
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=koumac,nc&units=imperial
    Processing Record #134 | City ID: 2037069 | City Name: hailun
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hailun,cn&units=imperial
    Processing Record #135 | City ID: 1259385 | City Name: port blair
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port blair,in&units=imperial
    Processing Record #136 | City ID: 4407665 | City Name: kodiak
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kodiak,us&units=imperial
    Processing Record #137 | City ID: 463355 | City Name: zheleznodorozhnyy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=zheleznodorozhnyy,ru&units=imperial
    Processing Record #138 | City ID: 2729907 | City Name: longyearbyen
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=longyearbyen,sj&units=imperial
    Processing Record #139 | City ID: 5924351 | City Name: clyde river
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=clyde river,ca&units=imperial
    Processing Record #140 | City ID: 1847947 | City Name: shingu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=shingu,jp&units=imperial
    Processing Record #141 | City ID: 524681 | City Name: mrakovo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mrakovo,ru&units=imperial
    Processing Record #142 | City ID: 3372707 | City Name: ribeira grande
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ribeira grande,pt&units=imperial
    Processing Record #143 | City ID: 3985168 | City Name: san patricio
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=san patricio,mx&units=imperial
    Processing Record #144 | City ID: 3141667 | City Name: roald
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=roald,no&units=imperial
    Processing Record #145 | City ID: 552006 | City Name: kashary
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kashary,ru&units=imperial
    Processing Record #146 | City ID: 2741961 | City Name: buarcos
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=buarcos,pt&units=imperial
    Processing Record #147 | City ID: 479426 | City Name: svobodnyy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=svobodnyy,ru&units=imperial
    Processing Record #148 | City ID: 3395981 | City Name: maceio
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=maceio,br&units=imperial
    Processing Record #149 | City ID: 3831208 | City Name: qaanaaq
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=qaanaaq,gl&units=imperial
    Processing Record #150 | City ID: 2156643 | City Name: mount gambier
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mount gambier,au&units=imperial
    Processing Record #151 | City ID: 2618795 | City Name: klaksvik
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=klaksvik,fo&units=imperial
    Processing Record #152 | City ID: 546105 | City Name: nikolskoye
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nikolskoye,ru&units=imperial
    Processing Record #153 | City ID: 3573197 | City Name: hamilton
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hamilton,bm&units=imperial
    Processing Record #154 | City ID: 4011743 | City Name: constitucion
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=constitucion,mx&units=imperial
    Processing Record #155 | City ID: 2174444 | City Name: bowen
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bowen,au&units=imperial
    Processing Record #156 | City ID: 1280037 | City Name: shache
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=shache,cn&units=imperial
    Processing Record #157 | City ID: 3625710 | City Name: upata
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=upata,ve&units=imperial
    Processing Record #158 | City ID: 1526384 | City Name: boralday
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=boralday,kz&units=imperial
    Processing Record #159 | City ID: 1045114 | City Name: inhambane
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=inhambane,mz&units=imperial
    Processing Record #160 | City ID: 6063429 | City Name: macklin
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=macklin,ca&units=imperial
    Processing Record #161 | City ID: 5572979 | City Name: merrill
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=merrill,us&units=imperial
    Processing Record #162 | City ID: 6068416 | City Name: mayo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mayo,ca&units=imperial
    Processing Record #163 | City ID: 964712 | City Name: plettenberg bay
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=plettenberg bay,za&units=imperial
    Processing Record #164 | City ID: 2964782 | City Name: dingle
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=dingle,ie&units=imperial
    Processing Record #165 | City ID: 2071860 | City Name: esperance
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=esperance,au&units=imperial
    Processing Record #166 | City ID: 504187 | City Name: puksoozero
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=puksoozero,ru&units=imperial
    Processing Record #167 | City ID: 595284 | City Name: rietavas
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=rietavas,lt&units=imperial
    Processing Record #168 | City ID: 3355672 | City Name: luderitz
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=luderitz,na&units=imperial
    Processing Record #169 | City ID: 370481 | City Name: marawi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=marawi,sd&units=imperial
    Processing Record #170 | City ID: 3689718 | City Name: guasdualito
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=guasdualito,ve&units=imperial
    Processing Record #171 | City ID: 2063042 | City Name: port hedland
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port hedland,au&units=imperial
    Processing Record #172 | City ID: 2234663 | City Name: batouri
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=batouri,cm&units=imperial
    Processing Record #173 | City ID: 2658904 | City Name: saanen
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saanen,ch&units=imperial
    Processing Record #174 | City ID: 87205 | City Name: darnah
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=darnah,ly&units=imperial
    Processing Record #175 | City ID: 5883074 | City Name: albanel
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=albanel,ca&units=imperial
    Processing Record #176 | City ID: 2152668 | City Name: portland
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=portland,au&units=imperial
    Processing Record #177 | City ID: 4732862 | City Name: nome
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nome,us&units=imperial
    Processing Record #178 | City ID: 1261853 | City Name: narasannapeta
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=narasannapeta,in&units=imperial
    Processing Record #179 | City ID: 2191562 | City Name: dunedin
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=dunedin,nz&units=imperial
    Processing Record #180 | City ID: 777019 | City Name: vardo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vardo,no&units=imperial
    Processing Record #181 | City ID: 3352263 | City Name: warmbad
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=warmbad,na&units=imperial
    Processing Record #182 | City ID: 3391889 | City Name: pitimbu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pitimbu,br&units=imperial
    Processing Record #183 | City ID: 3495137 | City Name: pedernales
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pedernales,do&units=imperial
    Processing Record #184 | City ID: 3402648 | City Name: carutapera
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=carutapera,br&units=imperial
    Processing Record #185 | City ID: 2075720 | City Name: broome
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=broome,au&units=imperial
    Processing Record #186 | City ID: 247176 | City Name: sabha
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sabha,jo&units=imperial
    Processing Record #187 | City ID: 2132606 | City Name: samarai
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=samarai,pg&units=imperial
    Processing Record #188 | City ID: 1528998 | City Name: yumen
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yumen,cn&units=imperial
    Processing Record #189 | City ID: 2194098 | City Name: ahipara
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ahipara,nz&units=imperial
    Processing Record #190 | City ID: 2021031 | City Name: kyren
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kyren,ru&units=imperial
    Processing Record #191 | City ID: 3466980 | City Name: caravelas
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=caravelas,br&units=imperial
    Processing Record #192 | City ID: 6452235 | City Name: ajaccio
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ajaccio,fr&units=imperial
    Processing Record #193 | City ID: 5847411 | City Name: kahului
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kahului,us&units=imperial
    Processing Record #194 | City ID: 2180815 | City Name: tuatapere
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tuatapere,nz&units=imperial
    Processing Record #195 | City ID: 2208248 | City Name: kaitangata
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kaitangata,nz&units=imperial
    Processing Record #196 | City ID: 5864145 | City Name: homer
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=homer,us&units=imperial
    Processing Record #197 | City ID: 2629833 | City Name: husavik
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=husavik,is&units=imperial
    Processing Record #198 | City ID: 415189 | City Name: aden
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=aden,ye&units=imperial
    Processing Record #199 | City ID: 3466165 | City Name: cidreira
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cidreira,br&units=imperial
    Processing Record #200 | City ID: 4276800 | City Name: oswego
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=oswego,us&units=imperial
    Processing Record #201 | City ID: 7522928 | City Name: san andres
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=san andres,co&units=imperial
    Processing Record #202 | City ID: 3629710 | City Name: puerto ayacucho
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=puerto ayacucho,ve&units=imperial
    Processing Record #203 | City ID: 2272197 | City Name: alcains
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=alcains,pt&units=imperial
    Processing Record #204 | City ID: 53157 | City Name: qandala
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=qandala,so&units=imperial
    Processing Record #205 | City ID: 2655288 | City Name: boddam
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=boddam,gb&units=imperial
    Processing Record #206 | City ID: 5248511 | City Name: chippewa falls
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=chippewa falls,us&units=imperial
    Processing Record #207 | City ID: 2120591 | City Name: tilichiki
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tilichiki,ru&units=imperial
    Processing Record #208 | City ID: 1706889 | City Name: puro
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=puro,ph&units=imperial
    Processing Record #209 | City ID: 2428394 | City Name: mao
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mao,td&units=imperial
    Processing Record #210 | City ID: 3904666 | City Name: san jose
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=san jose,bo&units=imperial
    Processing Record #211 | City ID: 5882953 | City Name: aklavik
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=aklavik,ca&units=imperial
    Processing Record #212 | City ID: 3421193 | City Name: paamiut
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=paamiut,gl&units=imperial
    Processing Record #213 | City ID: 3374210 | City Name: sao filipe
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sao filipe,cv&units=imperial
    Processing Record #214 | City ID: 3838859 | City Name: rio gallegos
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=rio gallegos,ar&units=imperial
    Processing Record #215 | City ID: 1337619 | City Name: ugoofaaru
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ugoofaaru,mv&units=imperial
    Processing Record #216 | City ID: 162158 | City Name: baherden
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=baherden,tm&units=imperial
    Processing Record #217 | City ID: 2839050 | City Name: schkeuditz
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=schkeuditz,de&units=imperial
    Processing Record #218 | City ID: 935215 | City Name: saint-philippe
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saint-philippe,re&units=imperial
    Processing Record #219 | City ID: 5118398 | City Name: geneva
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=geneva,us&units=imperial
    Processing Record #220 | City ID: 3451138 | City Name: rio grande
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=rio grande,br&units=imperial
    Processing Record #221 | City ID: 6690296 | City Name: saint-joseph
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saint-joseph,re&units=imperial
    Processing Record #222 | City ID: 212902 | City Name: kindu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kindu,cd&units=imperial
    Processing Record #223 | City ID: 2030065 | City Name: mandalgovi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mandalgovi,mn&units=imperial
    Processing Record #224 | City ID: 3981460 | City Name: coahuayana
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=coahuayana,mx&units=imperial
    Processing Record #225 | City ID: 2399959 | City Name: koulamoutou
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=koulamoutou,ga&units=imperial
    Processing Record #226 | City ID: 2063039 | City Name: port keats
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port keats,au&units=imperial
    Processing Record #227 | City ID: 786113 | City Name: samokov
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=samokov,mk&units=imperial
    Processing Record #228 | City ID: 1504382 | City Name: kargasok
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kargasok,ru&units=imperial
    Processing Record #229 | City ID: 77408 | City Name: bajil
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bajil,ye&units=imperial
    Processing Record #230 | City ID: 2144528 | City Name: warrnambool
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=warrnambool,au&units=imperial
    Processing Record #231 | City ID: 556268 | City Name: ostrovnoy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ostrovnoy,ru&units=imperial
    Processing Record #232 | City ID: 2084442 | City Name: vanimo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vanimo,pg&units=imperial
    Processing Record #233 | City ID: 361055 | City Name: ismailia
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ismailia,eg&units=imperial
    Processing Record #234 | City ID: 1505526 | City Name: irbit
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=irbit,ru&units=imperial
    Processing Record #235 | City ID: 3137469 | City Name: sorland
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sorland,no&units=imperial
    Processing Record #236 | City ID: 2108502 | City Name: honiara
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=honiara,sb&units=imperial
    Processing Record #237 | City ID: 1485997 | City Name: yeniseysk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yeniseysk,ru&units=imperial
    Processing Record #238 | City ID: 3587636 | City Name: yepocapa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yepocapa,gt&units=imperial
    Processing Record #239 | City ID: 627904 | City Name: hrodna
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hrodna,by&units=imperial
    Processing Record #240 | City ID: 5374920 | City Name: morro bay
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=morro bay,us&units=imperial
    Processing Record #241 | City ID: 778707 | City Name: mehamn
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mehamn,no&units=imperial
    Processing Record #242 | City ID: 2119538 | City Name: yelizovo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yelizovo,ru&units=imperial
    Processing Record #243 | City ID: 1106677 | City Name: bambous virieux
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bambous virieux,mu&units=imperial
    Processing Record #244 | City ID: 157429 | City Name: kilindoni
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kilindoni,tz&units=imperial
    Processing Record #245 | City ID: 2022572 | City Name: khatanga
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=khatanga,ru&units=imperial
    Processing Record #246 | City ID: 5866063 | City Name: kenai
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kenai,us&units=imperial
    Processing Record #247 | City ID: 2039557 | City Name: khasan
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=khasan,ru&units=imperial
    Processing Record #248 | City ID: 5972762 | City Name: hay river
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hay river,ca&units=imperial
    Processing Record #249 | City ID: 2967166 | City Name: yzeure
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yzeure,fr&units=imperial
    Processing Record #250 | City ID: 7535694 | City Name: desbiens
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=desbiens,ca&units=imperial
    Processing Record #251 | City ID: 2510821 | City Name: soller
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=soller,es&units=imperial
    Processing Record #252 | City ID: 3553478 | City Name: santa fe
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=santa fe,cu&units=imperial
    Processing Record #253 | City ID: 2090021 | City Name: namatanai
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=namatanai,pg&units=imperial
    Processing Record #254 | City ID: 3347019 | City Name: namibe
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=namibe,ao&units=imperial
    Processing Record #255 | City ID: 3985710 | City Name: cabo san lucas
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cabo san lucas,mx&units=imperial
    Processing Record #256 | City ID: 5640350 | City Name: billings
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=billings,us&units=imperial
    Processing Record #257 | City ID: 2146219 | City Name: hervey bay
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hervey bay,au&units=imperial
    Processing Record #258 | City ID: 2239862 | City Name: malanje
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=malanje,ao&units=imperial
    Processing Record #259 | City ID: 1735902 | City Name: sibu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sibu,my&units=imperial
    Processing Record #260 | City ID: 3870282 | City Name: talcahuano
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=talcahuano,cl&units=imperial
    Processing Record #261 | City ID: 1054329 | City Name: vangaindrano
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vangaindrano,mg&units=imperial
    Processing Record #262 | City ID: 3894426 | City Name: coihaique
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=coihaique,cl&units=imperial
    Processing Record #263 | City ID: 934479 | City Name: grand gaube
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=grand gaube,mu&units=imperial
    Processing Record #264 | City ID: 3356832 | City Name: henties bay
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=henties bay,na&units=imperial
    Processing Record #265 | City ID: 2522437 | City Name: adeje
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=adeje,es&units=imperial
    Processing Record #266 | City ID: 495112 | City Name: shebekino
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=shebekino,ru&units=imperial
    Processing Record #267 | City ID: 777682 | City Name: skjervoy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=skjervoy,no&units=imperial
    Processing Record #268 | City ID: 3691954 | City Name: sechura
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sechura,pe&units=imperial
    Processing Record #269 | City ID: 847634 | City Name: rypefjord
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=rypefjord,no&units=imperial
    Processing Record #270 | City ID: 6089245 | City Name: norman wells
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=norman wells,ca&units=imperial
    Processing Record #271 | City ID: 6316343 | City Name: alta floresta
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=alta floresta,br&units=imperial
    Processing Record #272 | City ID: 1862505 | City Name: hirara
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hirara,jp&units=imperial
    Processing Record #273 | City ID: 7671223 | City Name: kloulklubed
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kloulklubed,pw&units=imperial
    Processing Record #274 | City ID: 2063056 | City Name: port augusta
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port augusta,au&units=imperial
    Processing Record #275 | City ID: 3703946 | City Name: nargana
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nargana,pa&units=imperial
    Processing Record #276 | City ID: 6096551 | City Name: pangnirtung
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pangnirtung,ca&units=imperial
    Processing Record #277 | City ID: 5797693 | City Name: hoquiam
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hoquiam,us&units=imperial
    Processing Record #278 | City ID: 1264976 | City Name: leh
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=leh,in&units=imperial
    Processing Record #279 | City ID: 1254390 | City Name: tiruchchendur
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tiruchchendur,in&units=imperial
    Processing Record #280 | City ID: 2092164 | City Name: lorengau
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=lorengau,pg&units=imperial
    Processing Record #281 | City ID: 986134 | City Name: kuruman
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kuruman,za&units=imperial
    Processing Record #282 | City ID: 2187834 | City Name: mamaku
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mamaku,nz&units=imperial
    Processing Record #283 | City ID: 3580733 | City Name: bodden town
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bodden town,ky&units=imperial
    Processing Record #284 | City ID: 2093691 | City Name: kokoda
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kokoda,pg&units=imperial
    Processing Record #285 | City ID: 1629380 | City Name: ruteng
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ruteng,id&units=imperial
    Processing Record #286 | City ID: 7626370 | City Name: bud
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bud,no&units=imperial
    Processing Record #287 | City ID: 3430443 | City Name: necochea
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=necochea,ar&units=imperial
    Processing Record #288 | City ID: 2966356 | City Name: bantry
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bantry,ie&units=imperial
    Processing Record #289 | City ID: 3147822 | City Name: gravdal
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=gravdal,no&units=imperial
    Processing Record #290 | City ID: 2450173 | City Name: taoudenni
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=taoudenni,ml&units=imperial
    Processing Record #291 | City ID: 1651591 | City Name: amahai
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=amahai,id&units=imperial
    Processing Record #292 | City ID: 2521582 | City Name: arona
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=arona,es&units=imperial
    Processing Record #293 | City ID: 2446796 | City Name: bilma
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bilma,ne&units=imperial
    Processing Record #294 | City ID: 162099 | City Name: buzmeyin
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=buzmeyin,tm&units=imperial
    Processing Record #295 | City ID: 3145148 | City Name: myre
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=myre,no&units=imperial
    Processing Record #296 | City ID: 3457928 | City Name: mantenopolis
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mantenopolis,br&units=imperial
    Processing Record #297 | City ID: 1516048 | City Name: hovd
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hovd,mn&units=imperial
    Processing Record #298 | City ID: 2013727 | City Name: vanavara
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vanavara,ru&units=imperial
    Processing Record #299 | City ID: 2267254 | City Name: lagoa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=lagoa,pt&units=imperial
    Processing Record #300 | City ID: 3354071 | City Name: oranjemund
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=oranjemund,na&units=imperial
    Processing Record #301 | City ID: 3359736 | City Name: vredendal
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vredendal,za&units=imperial
    Processing Record #302 | City ID: 113659 | City Name: tabas
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tabas,ir&units=imperial
    Processing Record #303 | City ID: 4734350 | City Name: stephenville
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=stephenville,us&units=imperial
    Processing Record #304 | City ID: 3447589 | City Name: silvania
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=silvania,br&units=imperial
    Processing Record #305 | City ID: 3443061 | City Name: chuy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=chuy,uy&units=imperial
    Processing Record #306 | City ID: 4943204 | City Name: marshfield
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=marshfield,us&units=imperial
    Processing Record #307 | City ID: 2965761 | City Name: carndonagh
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=carndonagh,ie&units=imperial
    Processing Record #308 | City ID: 2137773 | City Name: vao
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vao,nc&units=imperial
    Processing Record #309 | City ID: 2161515 | City Name: kiama
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kiama,au&units=imperial
    Processing Record #310 | City ID: 2255304 | City Name: sembe
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sembe,cg&units=imperial
    Processing Record #311 | City ID: 108410 | City Name: riyadh
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=riyadh,sa&units=imperial
    Processing Record #312 | City ID: 2411397 | City Name: georgetown
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=georgetown,sh&units=imperial
    Processing Record #313 | City ID: 6159980 | City Name: sussex
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sussex,ca&units=imperial
    Processing Record #314 | City ID: 3576994 | City Name: cockburn town
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cockburn town,tc&units=imperial
    Processing Record #315 | City ID: 478050 | City Name: ust-kulom
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ust-kulom,ru&units=imperial
    Processing Record #316 | City ID: 1498087 | City Name: nadym
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nadym,ru&units=imperial
    Processing Record #317 | City ID: 3982846 | City Name: san jeronimo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=san jeronimo,mx&units=imperial
    Processing Record #318 | City ID: 2051523 | City Name: bratsk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bratsk,ru&units=imperial
    Processing Record #319 | City ID: 6104745 | City Name: pilot butte
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pilot butte,ca&units=imperial
    Processing Record #320 | City ID: 1604771 | City Name: yaring
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yaring,th&units=imperial
    Processing Record #321 | City ID: 2610343 | City Name: vestmanna
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=vestmanna,fo&units=imperial
    Processing Record #322 | City ID: 2396853 | City Name: omboue
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=omboue,ga&units=imperial
    Processing Record #323 | City ID: 2063036 | City Name: port lincoln
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port lincoln,au&units=imperial
    Processing Record #324 | City ID: 2176639 | City Name: batemans bay
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=batemans bay,au&units=imperial
    Processing Record #325 | City ID: 1271476 | City Name: sualkuchi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sualkuchi,in&units=imperial
    Processing Record #326 | City ID: 5994763 | City Name: labelle
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=labelle,ca&units=imperial
    Processing Record #327 | City ID: 5563839 | City Name: fortuna
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=fortuna,us&units=imperial
    Processing Record #328 | City ID: 2270385 | City Name: camacha
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=camacha,pt&units=imperial
    Processing Record #329 | City ID: 3388847 | City Name: sao felix do xingu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sao felix do xingu,br&units=imperial
    Processing Record #330 | City ID: 1529376 | City Name: korla
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=korla,cn&units=imperial
    Processing Record #331 | City ID: 3867291 | City Name: filadelfia
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=filadelfia,py&units=imperial
    Processing Record #332 | City ID: 2036986 | City Name: hegang
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hegang,cn&units=imperial
    Processing Record #333 | City ID: 2185329 | City Name: waipawa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=waipawa,nz&units=imperial
    Processing Record #334 | City ID: 581049 | City Name: arkhangelsk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=arkhangelsk,ru&units=imperial
    Processing Record #335 | City ID: 3416888 | City Name: grindavik
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=grindavik,is&units=imperial
    Processing Record #336 | City ID: 2147756 | City Name: swan hill
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=swan hill,au&units=imperial
    Processing Record #337 | City ID: 1262260 | City Name: nagapattinam
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nagapattinam,in&units=imperial
    Processing Record #338 | City ID: 1293625 | City Name: dawei
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=dawei,mm&units=imperial
    Processing Record #339 | City ID: 118191 | City Name: rudsar
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=rudsar,ir&units=imperial
    Processing Record #340 | City ID: 504269 | City Name: pudozh
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pudozh,ru&units=imperial
    Processing Record #341 | City ID: 3448011 | City Name: saquarema
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saquarema,br&units=imperial
    Processing Record #342 | City ID: 5380420 | City Name: pacifica
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pacifica,us&units=imperial
    Processing Record #343 | City ID: 4032420 | City Name: neiafu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=neiafu,to&units=imperial
    Processing Record #344 | City ID: 2020738 | City Name: litovko
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=litovko,ru&units=imperial
    Processing Record #345 | City ID: 1279134 | City Name: akbarpur
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=akbarpur,in&units=imperial
    Processing Record #346 | City ID: 4944903 | City Name: nantucket
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nantucket,us&units=imperial
    Processing Record #347 | City ID: 2013923 | City Name: ust-kut
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ust-kut,ru&units=imperial
    Processing Record #348 | City ID: 230584 | City Name: kumi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kumi,ug&units=imperial
    Processing Record #349 | City ID: 739600 | City Name: sinop
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sinop,tr&units=imperial
    Processing Record #350 | City ID: 2236967 | City Name: soyo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=soyo,ao&units=imperial
    Processing Record #351 | City ID: 2986933 | City Name: plaisance-du-touch
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=plaisance-du-touch,fr&units=imperial
    Processing Record #352 | City ID: 898947 | City Name: senanga
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=senanga,zm&units=imperial
    Processing Record #353 | City ID: 2160517 | City Name: launceston
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=launceston,au&units=imperial
    Processing Record #354 | City ID: 2012530 | City Name: zhigansk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=zhigansk,ru&units=imperial
    Processing Record #355 | City ID: 1496073 | City Name: orlik
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=orlik,ru&units=imperial
    Processing Record #356 | City ID: 3094086 | City Name: kwidzyn
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kwidzyn,pl&units=imperial
    Processing Record #357 | City ID: 5919815 | City Name: channel-port aux basques
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=channel-port aux basques,ca&units=imperial
    Processing Record #358 | City ID: 986717 | City Name: kruisfontein
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kruisfontein,za&units=imperial
    Processing Record #359 | City ID: 3835994 | City Name: santa rosa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=santa rosa,ar&units=imperial
    Processing Record #360 | City ID: 750598 | City Name: bilecik
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bilecik,tr&units=imperial
    Processing Record #361 | City ID: 2077895 | City Name: alice springs
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=alice springs,au&units=imperial
    Processing Record #362 | City ID: 285663 | City Name: bayan
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bayan,kw&units=imperial
    Processing Record #363 | City ID: 5079250 | City Name: south sioux city
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=south sioux city,us&units=imperial
    Processing Record #364 | City ID: 6089179 | City Name: normandin
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=normandin,ca&units=imperial
    Processing Record #365 | City ID: 2964492 | City Name: dunmore east
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=dunmore east,ie&units=imperial
    Processing Record #366 | City ID: 2033135 | City Name: zhengjiatun
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=zhengjiatun,cn&units=imperial
    Processing Record #367 | City ID: 2377457 | City Name: nouadhibou
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nouadhibou,mr&units=imperial
    Processing Record #368 | City ID: 2440371 | City Name: ouallam
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ouallam,ne&units=imperial
    Processing Record #369 | City ID: 1525988 | City Name: ayagoz
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ayagoz,kz&units=imperial
    Processing Record #370 | City ID: 3385670 | City Name: urucara
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=urucara,br&units=imperial
    Processing Record #371 | City ID: 4033356 | City Name: tiarei
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tiarei,pf&units=imperial
    Processing Record #372 | City ID: 3899695 | City Name: ancud
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ancud,cl&units=imperial
    Processing Record #373 | City ID: 509483 | City Name: pinega
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pinega,ru&units=imperial
    Processing Record #374 | City ID: 2193968 | City Name: amberley
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=amberley,nz&units=imperial
    Processing Record #375 | City ID: 5059429 | City Name: key west
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=key west,us&units=imperial
    Processing Record #376 | City ID: 217834 | City Name: bukama
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bukama,cd&units=imperial
    Processing Record #377 | City ID: 2347059 | City Name: birnin kebbi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=birnin kebbi,ng&units=imperial
    Processing Record #378 | City ID: 5983720 | City Name: iqaluit
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=iqaluit,ca&units=imperial
    Processing Record #379 | City ID: 2235776 | City Name: akonolinga
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=akonolinga,cm&units=imperial
    Processing Record #380 | City ID: 2151187 | City Name: roma
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=roma,au&units=imperial
    Processing Record #381 | City ID: 3354077 | City Name: opuwo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=opuwo,na&units=imperial
    Processing Record #382 | City ID: 2297810 | City Name: mumford
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mumford,gh&units=imperial
    Processing Record #383 | City ID: 3421719 | City Name: narsaq
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=narsaq,gl&units=imperial
    Processing Record #384 | City ID: 876177 | City Name: luau
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=luau,ao&units=imperial
    Processing Record #385 | City ID: 3939761 | City Name: hualmay
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hualmay,pe&units=imperial
    Processing Record #386 | City ID: 2012593 | City Name: zeya
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=zeya,ru&units=imperial
    Processing Record #387 | City ID: 1527497 | City Name: kyzyl-suu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kyzyl-suu,kg&units=imperial
    Processing Record #388 | City ID: 148730 | City Name: zanzibar
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=zanzibar,tz&units=imperial
    Processing Record #389 | City ID: 2123628 | City Name: magadan
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=magadan,ru&units=imperial
    Processing Record #390 | City ID: 978895 | City Name: margate
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=margate,za&units=imperial
    Processing Record #391 | City ID: 3158300 | City Name: elverum
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=elverum,no&units=imperial
    Processing Record #392 | City ID: 3034483 | City Name: bayeux
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bayeux,fr&units=imperial
    Processing Record #393 | City ID: 3839307 | City Name: rawson
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=rawson,ar&units=imperial
    Processing Record #394 | City ID: 2293801 | City Name: yendi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=yendi,gh&units=imperial
    Processing Record #395 | City ID: 3931275 | City Name: putina
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=putina,pe&units=imperial
    Processing Record #396 | City ID: 945945 | City Name: upington
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=upington,za&units=imperial
    Processing Record #397 | City ID: 1648186 | City Name: bontang
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bontang,id&units=imperial
    Processing Record #398 | City ID: 3524903 | City Name: las choapas
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=las choapas,mx&units=imperial
    Processing Record #399 | City ID: 359792 | City Name: aswan
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=aswan,eg&units=imperial
    Processing Record #400 | City ID: 558384 | City Name: grushevskaya
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=grushevskaya,ru&units=imperial
    Processing Record #401 | City ID: 1274337 | City Name: chhatarpur
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=chhatarpur,in&units=imperial
    Processing Record #402 | City ID: 934649 | City Name: cap malheureux
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cap malheureux,mu&units=imperial
    Processing Record #403 | City ID: 339448 | City Name: dembi dolo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=dembi dolo,et&units=imperial
    Processing Record #404 | City ID: 1695555 | City Name: pandan
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pandan,ph&units=imperial
    Processing Record #405 | City ID: 3663503 | City Name: manicore
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=manicore,br&units=imperial
    Processing Record #406 | City ID: 1263942 | City Name: manavalakurichi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=manavalakurichi,in&units=imperial
    Processing Record #407 | City ID: 2641181 | City Name: norwich
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=norwich,gb&units=imperial
    Processing Record #408 | City ID: 4392768 | City Name: joplin
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=joplin,us&units=imperial
    Processing Record #409 | City ID: 2121025 | City Name: srednekolymsk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=srednekolymsk,ru&units=imperial
    Processing Record #410 | City ID: 3664539 | City Name: coari
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=coari,br&units=imperial
    Processing Record #411 | City ID: 2122605 | City Name: okhotsk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=okhotsk,ru&units=imperial
    Processing Record #412 | City ID: 1244926 | City Name: hambantota
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hambantota,lk&units=imperial
    Processing Record #413 | City ID: 2025241 | City Name: churapcha
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=churapcha,ru&units=imperial
    Processing Record #414 | City ID: 325304 | City Name: afsin
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=afsin,tr&units=imperial
    Processing Record #415 | City ID: 2214846 | City Name: misratah
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=misratah,ly&units=imperial
    Processing Record #416 | City ID: 1640576 | City Name: kefamenanu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kefamenanu,id&units=imperial
    Processing Record #417 | City ID: 3996234 | City Name: lazaro cardenas
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=lazaro cardenas,mx&units=imperial
    Processing Record #418 | City ID: 3578441 | City Name: saint-francois
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=saint-francois,gp&units=imperial
    Processing Record #419 | City ID: 2120047 | City Name: ust-omchug
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ust-omchug,ru&units=imperial
    Processing Record #420 | City ID: 2418437 | City Name: kouroussa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kouroussa,gn&units=imperial
    Processing Record #421 | City ID: 3358666 | City Name: aranos
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=aranos,na&units=imperial
    Processing Record #422 | City ID: 3691582 | City Name: talara
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=talara,pe&units=imperial
    Processing Record #423 | City ID: 1716788 | City Name: cortes
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cortes,ph&units=imperial
    Processing Record #424 | City ID: 3393692 | City Name: itarema
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=itarema,br&units=imperial
    Processing Record #425 | City ID: 707695 | City Name: illintsi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=illintsi,ua&units=imperial
    Processing Record #426 | City ID: 6111862 | City Name: port hardy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port hardy,ca&units=imperial
    Processing Record #427 | City ID: 3461425 | City Name: ilhabela
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ilhabela,br&units=imperial
    Processing Record #428 | City ID: 3381538 | City Name: grand-santi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=grand-santi,gf&units=imperial
    Processing Record #429 | City ID: 3398381 | City Name: morros
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=morros,br&units=imperial
    Processing Record #430 | City ID: 3450671 | City Name: salinas
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=salinas,br&units=imperial
    Processing Record #431 | City ID: 3141332 | City Name: roros
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=roros,no&units=imperial
    Processing Record #432 | City ID: 3471846 | City Name: aracuai
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=aracuai,br&units=imperial
    Processing Record #433 | City ID: 475955 | City Name: velizh
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=velizh,ru&units=imperial
    Processing Record #434 | City ID: 2037086 | City Name: haicheng
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=haicheng,cn&units=imperial
    Processing Record #435 | City ID: 6149996 | City Name: smithers
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=smithers,ca&units=imperial
    Processing Record #436 | City ID: 2064735 | City Name: nhulunbuy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nhulunbuy,au&units=imperial
    Processing Record #437 | City ID: 2187175 | City Name: matata
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=matata,nz&units=imperial
    Processing Record #438 | City ID: 5742974 | City Name: north bend
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=north bend,us&units=imperial
    Processing Record #439 | City ID: 2033196 | City Name: zhangjiakou
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=zhangjiakou,cn&units=imperial
    Processing Record #440 | City ID: 1635815 | City Name: maumere
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=maumere,id&units=imperial
    Processing Record #441 | City ID: 2022463 | City Name: khilok
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=khilok,ru&units=imperial
    Processing Record #442 | City ID: 2139521 | City Name: noumea
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=noumea,nc&units=imperial
    Processing Record #443 | City ID: 1634614 | City Name: nabire
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nabire,id&units=imperial
    Processing Record #444 | City ID: 1855363 | City Name: nirasaki
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nirasaki,jp&units=imperial
    Processing Record #445 | City ID: 1526038 | City Name: atbasar
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=atbasar,kz&units=imperial
    Processing Record #446 | City ID: 2012728 | City Name: zakamensk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=zakamensk,ru&units=imperial
    Processing Record #447 | City ID: 3909038 | City Name: padilla
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=padilla,bo&units=imperial
    Processing Record #448 | City ID: 1257638 | City Name: salaya
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=salaya,in&units=imperial
    Processing Record #449 | City ID: 241131 | City Name: victoria
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=victoria,sc&units=imperial
    Processing Record #450 | City ID: 544397 | City Name: kortkeros
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kortkeros,ru&units=imperial
    Processing Record #451 | City ID: 103630 | City Name: najran
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=najran,sa&units=imperial
    Processing Record #452 | City ID: 5895424 | City Name: bay roberts
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bay roberts,ca&units=imperial
    Processing Record #453 | City ID: 586001 | City Name: xudat
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=xudat,az&units=imperial
    Processing Record #454 | City ID: 3404558 | City Name: cabedelo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cabedelo,br&units=imperial
    Processing Record #455 | City ID: 3429886 | City Name: punta alta
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=punta alta,ar&units=imperial
    Processing Record #456 | City ID: 1527121 | City Name: tyup
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=tyup,kg&units=imperial
    Processing Record #457 | City ID: 2396518 | City Name: port-gentil
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=port-gentil,ga&units=imperial
    Processing Record #458 | City ID: 1501377 | City Name: kungurtug
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kungurtug,ru&units=imperial
    Processing Record #459 | City ID: 1185148 | City Name: patiya
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=patiya,bd&units=imperial
    Processing Record #460 | City ID: 2126682 | City Name: bilibino
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bilibino,ru&units=imperial
    Processing Record #461 | City ID: 1788268 | City Name: dongsheng
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=dongsheng,cn&units=imperial
    Processing Record #462 | City ID: 2329821 | City Name: mubi
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=mubi,ng&units=imperial
    Processing Record #463 | City ID: 5955902 | City Name: fort nelson
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=fort nelson,ca&units=imperial
    Processing Record #464 | City ID: 1715348 | City Name: panacan
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=panacan,ph&units=imperial
    Processing Record #465 | City ID: 2022129 | City Name: kichera
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kichera,ru&units=imperial
    Processing Record #466 | City ID: 1785462 | City Name: zaoyang
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=zaoyang,cn&units=imperial
    Processing Record #467 | City ID: 1835848 | City Name: seoul
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=seoul,kr&units=imperial
    Processing Record #468 | City ID: 1808106 | City Name: hongjiang
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hongjiang,cn&units=imperial
    Processing Record #469 | City ID: 105299 | City Name: jizan
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=jizan,sa&units=imperial
    Processing Record #470 | City ID: 1504380 | City Name: kargat
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kargat,ru&units=imperial
    Processing Record #471 | City ID: 525426 | City Name: sobolevo
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=sobolevo,ru&units=imperial
    Processing Record #472 | City ID: 3921355 | City Name: challapata
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=challapata,bo&units=imperial
    Processing Record #473 | City ID: 2361373 | City Name: diapaga
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=diapaga,bf&units=imperial
    Processing Record #474 | City ID: 2013639 | City Name: verkhnevilyuysk
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=verkhnevilyuysk,ru&units=imperial
    Processing Record #475 | City ID: 4272782 | City Name: hays
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=hays,us&units=imperial
    Processing Record #476 | City ID: 1788852 | City Name: xining
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=xining,cn&units=imperial
    Processing Record #477 | City ID: 1033356 | City Name: nampula
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nampula,mz&units=imperial
    Processing Record #478 | City ID: 211098 | City Name: lubao
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=lubao,cd&units=imperial
    Processing Record #479 | City ID: 6243926 | City Name: seddon
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=seddon,nz&units=imperial
    Processing Record #480 | City ID: 2395317 | City Name: banikoara
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=banikoara,bj&units=imperial
    Processing Record #481 | City ID: 1214488 | City Name: meulaboh
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=meulaboh,id&units=imperial
    Processing Record #482 | City ID: 2315026 | City Name: kasongo-lunda
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=kasongo-lunda,cd&units=imperial
    Processing Record #483 | City ID: 1865309 | City Name: katsuura
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=katsuura,jp&units=imperial
    Processing Record #484 | City ID: 217745 | City Name: bumba
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bumba,cd&units=imperial
    Processing Record #485 | City ID: 5924500 | City Name: coaticook
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=coaticook,ca&units=imperial
    Processing Record #486 | City ID: 3932145 | City Name: pisco
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=pisco,pe&units=imperial
    Processing Record #487 | City ID: 2145554 | City Name: ulladulla
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=ulladulla,au&units=imperial
    Processing Record #488 | City ID: 6065867 | City Name: marathon
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=marathon,ca&units=imperial
    Processing Record #489 | City ID: 505256 | City Name: primorka
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=primorka,ru&units=imperial
    Processing Record #490 | City ID: 3354021 | City Name: oshakati
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=oshakati,na&units=imperial
    Processing Record #491 | City ID: 3351663 | City Name: benguela
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=benguela,ao&units=imperial
    Processing Record #492 | City ID: 1058080 | City Name: nosy varika
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=nosy varika,mg&units=imperial
    Processing Record #493 | City ID: 2878074 | City Name: lichtenfels
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=lichtenfels,de&units=imperial
    Processing Record #494 | City ID: 2028164 | City Name: deputatskiy
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=deputatskiy,ru&units=imperial
    Processing Record #495 | City ID: 3530617 | City Name: cintalapa
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=cintalapa,mx&units=imperial
    Processing Record #496 | City ID: 3374083 | City Name: bathsheba
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=bathsheba,bb&units=imperial
    Processing Record #497 | City ID: 3468020 | City Name: camapua
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=camapua,br&units=imperial
    Processing Record #498 | City ID: 3465342 | City Name: puerto quijarro
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=puerto quijarro,bo&units=imperial
    Processing Record #499 | City ID: 725988 | City Name: velingrad
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=velingrad,bg&units=imperial
    Processing Record #500 | City ID: 1622318 | City Name: waingapu
    http://api.openweathermap.org/data/2.5/weather?appid=84fe59f3ffa1bf7920c39149bf3dde70&q=waingapu,id&units=imperial
    


```python
# Output to csv
weather_data_df.to_csv("weather_data.csv", encoding="utf-8", index=False)
```


```python
# Display the count for each column in the Data Frame
weather_data_df.count()
```




    City           500
    Cloudiness     500
    Country        500
    Date           500
    Humidity       500
    Lat            500
    Lng            500
    Temperature    500
    Wind Speed     500
    dtype: int64




```python
# Display the Weather Data Frame
weather_data_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness</th>
      <th>Country</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>Lat</th>
      <th>Lng</th>
      <th>Temperature</th>
      <th>Wind Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Albany</td>
      <td>92</td>
      <td>AU</td>
      <td>1519942609</td>
      <td>93</td>
      <td>-35.02</td>
      <td>117.88</td>
      <td>59.32</td>
      <td>4.21</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Hobart</td>
      <td>75</td>
      <td>AU</td>
      <td>1519941600</td>
      <td>77</td>
      <td>-42.88</td>
      <td>147.33</td>
      <td>59.00</td>
      <td>5.82</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Saldanha</td>
      <td>0</td>
      <td>ZA</td>
      <td>1519938000</td>
      <td>52</td>
      <td>-33.01</td>
      <td>17.94</td>
      <td>69.80</td>
      <td>6.93</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Pacific Grove</td>
      <td>90</td>
      <td>US</td>
      <td>1519942080</td>
      <td>87</td>
      <td>36.62</td>
      <td>-121.92</td>
      <td>56.34</td>
      <td>19.46</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Ushuaia</td>
      <td>75</td>
      <td>AR</td>
      <td>1519938000</td>
      <td>66</td>
      <td>-54.81</td>
      <td>-68.31</td>
      <td>51.80</td>
      <td>4.70</td>
    </tr>
  </tbody>
</table>
</div>




```python
### Create the necessary graphs from the data frame
### AND SAVE each image as .png files

## Temperature (F) vs. Latitude
plt.title("City Latitude vs. Temperature (3/1/2018)")
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")

plt.xlim(min(weather_data_df["Lat"])-20, max(weather_data_df["Lat"]) + 20)
plt.ylim(min(weather_data_df["Temperature"])-50, max(weather_data_df["Temperature"]) + 50)


plt.scatter(weather_data_df["Lat"], weather_data_df["Temperature"], s =20, edgecolor = "black", c = "blue")
sns.set()
plt.savefig("City-Latitude-vs-Temperature.png")
plt.show()
```


![png](output_8_0.png)



```python
## Humidity (%) vs. Latitude
plt.title("City Latitude vs. Humidity (3/1/2018)")
plt.xlabel("Latitude")
plt.ylabel("Humdity (%)")

plt.xlim(min(weather_data_df["Lat"])-20, max(weather_data_df["Lat"]) + 20)
plt.ylim(min(weather_data_df["Humidity"])-20, max(weather_data_df["Humidity"]) + 20)


plt.scatter(weather_data_df["Lat"], weather_data_df["Humidity"], s =20, edgecolor = "black", c = "blue")
sns.set()
plt.savefig("City-Latitude-vs-Humidity.png")
plt.show()
```


![png](output_9_0.png)



```python
## Cloudiness (%) vs. Latitude
plt.title("City Latitude vs. Cloudiness (3/1/2018)")
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")

plt.xlim(min(weather_data_df["Lat"])-20, max(weather_data_df["Lat"]) + 20)
plt.ylim(min(weather_data_df["Cloudiness"])-20, max(weather_data_df["Cloudiness"]) + 20)


plt.scatter(weather_data_df["Lat"], weather_data_df["Cloudiness"], s =20, edgecolor = "black", c = "blue")
sns.set()
plt.savefig("City-Latitude-vs-Cloudiness.png")
plt.show()
```


![png](output_10_0.png)



```python
## Wind Speed (mph) vs. Latitude
plt.title("City Latitude vs. Wind Speed (3/1/2018)")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")

plt.xlim(min(weather_data_df["Lat"])-20, max(weather_data_df["Lat"]) + 20)
plt.ylim(min(weather_data_df["Wind Speed"])-10, max(weather_data_df["Wind Speed"]) + 10)


plt.scatter(weather_data_df["Lat"], weather_data_df["Wind Speed"], s =20, edgecolor = "black", c = "blue")
sns.set()
plt.savefig("City-Latitude-vs-Wind-Speed.png")
plt.show()
```


![png](output_11_0.png)

