#"// api weather"? 
from pprint import pprint
import requests

APIKEY ="83cf3f79a861e94acfe67ad1ef49e24d"
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID={APIKEY}')
pprint(r.json())
{u'base': u'cmc stations',
 u'clouds': {u'all': 68},
 u'cod': 200,
 u'coord': {u'lat': 51.50853, u'lon': -0.12574},
 u'dt': 1383907026,
 u'id': 2643743,
 u'main': {u'grnd_level': 1007.77,
           u'humidity': 97,
           u'pressure': 1007.77,
           u'sea_level': 1017.97,
           u'temp': 282.241,
           u'temp_max': 282.241,
           u'temp_min': 282.241},
 u'name': u'London',
 u'sys': {u'country': u'GB', u'sunrise': 1383894458, u'sunset': 1383927657},
 u'weather': [{u'description': u'broken clouds',
               u'icon': u'04d',
               u'id': 803,
               u'main': u'Clouds'}],
 u'wind': {u'deg': 158.5, u'speed': 2.36}}


import pyowm
owm = pyowm.OWM()
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
w.get_wind()
{u'speed': 3.1, u'deg': 220}
w.get_humidity()
76


