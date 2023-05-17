import requests
import pprint
from datetime import datetime

addressW = 'y'
while addressW == 'y':

    print('What is your address?')

    address = input()
    r = requests.get('https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=' + address + '&benchmark=9&format=json')

    json = r.json()

    resultY = json['result']['addressMatches'][0]['coordinates']['y']

    resultX = json['result']['addressMatches'][0]['coordinates']['x']

    s = requests.get('https://api.darksky.net/forecast/4588b8443530f7c04ea4160a434520d3/' + str(resultY) + ',' + str(resultX))

    json1 = s.json()

    weather = json1['daily']['data']

    for day in weather:
        date = datetime.fromtimestamp(day['time'])
        print(date.strftime('%A, %B, %d'))
        pprint.pprint(day['precipProbability'])

        if day['precipProbability'] >= 0.5:
            print(u'\u2602')
        else:
            print(u'\u2600')

    print('Weather for another address? (y/n)')
    addressW = input()

