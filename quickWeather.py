#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json
import requests
import sys

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])


url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3'.format
(location)
response = requests.get(url)
response.raise_for_status()


weatherData = json.loads(response.text)

w = weatherData['list']

print('Current weather in {}:'.format(location))
print(w[0]['weather'][0]['main'])

print(w[1]['weather'][0]['main'])

print(w[2]['weather'][0]['main'])
