import requests
from datetime import datetime

from twilio.rest import Client
body = ''

print('What is your address?')
body = body + 'What is your address?\n'
address = input()
body = body + address + '\n'
r = requests.get('https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=' + address + '&benchmark=9&format=json')

json = r.json()

resultY = json['result']['addressMatches'][0]['coordinates']['y']

resultX = json['result']['addressMatches'][0]['coordinates']['x']

s = requests.get('https://api.darksky.net/forecast/4588b8443530f7c04ea4160a434520d3/' + str(resultY) + ',' + str(resultX))

json1 = s.json()

weather = json1['daily']['data']
for day in weather:
    date = datetime.fromtimestamp(day['time'])

    if day['precipProbability'] >= 0.5:
        print(date.strftime('%m/%d/%y - %A') + ' - ' + u'\u2602')
        body = body + date.strftime('%m/%d/%y %A' + u'\u2602\n')

    else:
        print(date.strftime('%m/%d/%y - %A') + ' - ' + u'\u2600')
        body = body + date.strftime('%m/%d/%y %A' + u'\u2600\n')


account_sid = 'AC411c6a78f221cb517097cfdcca9a55db'
auth_token = '049894ce8526ba2ddb744794e193473c'
client = Client(account_sid, auth_token)

message = client.messages.create\
(
    from_='+19082743337',
    body='\n' + body,
    to='+19084949958'
)


