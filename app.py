import json  #Its a library,nothing but set of tools
import requests #Its a library,nothing but set of tools

#we are using API to fetch the temperature of city
city_name=input('Enter a city name:')
api_key='0b824eba1b475ff84bc74053fcf2a629'

#To build the API URL
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_information=requests.get(api_url)
data=get_server_information.json() #.json(), server sends json data as string (e.g., {"key": "value"}).
print(data)

""" output:
Enter a city name : Goa(only goa is given here)
{'coord': {'lon': 74.0833, 'lat': 15.3333}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 
'base': 'stations', 'main': {'temp': 31.21, 'feels_like': 29.77, 'temp_min': 31.21, 'temp_max': 31.21, 'pressure': 1011, 'humidity': 28, 'sea_level': 1011, 
'grnd_level': 999}, 'visibility': 10000, 'wind': {'speed': 3.74, 'deg': 67, 'gust': 4.41}, 'clouds': {'all': 36}, 'dt': 1734250561, 'sys': {'type': 1, 'id': 9233, 
'country': 'IN', 'sunrise': 1734225735, 'sunset': 1734266136}, 'timezone': 19800, 'id': 1271157, 'name': 'Goa', 'cod': 200}
 """

#for pretty formatting the json data(it means the string can be coverted into json format)
pretty_data=json.dumps(data, indent=4) #json is library, dumps is built in function in json module, dumps is used to convert the string into json readable format.
print(pretty_data)
""" output:
    {
    "coord": {
        "lon": 74.0833,
        "lat": 15.3333
    },
    "weather": [
        {
            "id": 801,
            "main": "Clouds",
            "description": "few clouds",
            "icon": "02d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 31.21,
        "feels_like": 31.83,
        "temp_min": 31.21,
        "temp_max": 31.21,
        "pressure": 1011,
        "humidity": 44,
        "sea_level": 1011,
        "grnd_level": 998
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.93,
        "deg": 65,
        "gust": 2.45
    },
    "clouds": {
        "all": 12
    },
    "dt": 1734264261,
    "sys": {
        "type": 1,
        "id": 9233,
        "country": "IN",
        "sunrise": 1734225735,
        "sunset": 1734266136
    },
    "timezone": 19800,
    "id": 1271157,
    "name": "Goa",
    "cod": 200
} """
 
 
 
 
 
"""  -->To comment a single line : #
 -->To comment the multiple lines in VSCode : alt+shift+A """