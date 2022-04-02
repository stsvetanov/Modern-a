import requests
import pytz
from datetime import datetime
import json

response = requests.get('http://api.openweathermap.org/data/2.5/weather',    # основен URL
                        params={   # GET параметри - dict
                            'q': 'Sofia',
                            'appid': '4d1231103d3ac41e56becfa993f6e17e'
                            },
                        timeout=20,  # seconds
                        )

# От извикването по-горе, библиотеката ще композира пълния URL:
print(response.url)

response_text = response.text
json_text = json.loads(response_text)
print(type(json_text))
print(json_text)

weather = json_text["weather"]
weather[0]['main']

print("Времето в София е {}".format(weather[0]['main']))

ts = json_text['dt']
dt = datetime.fromtimestamp(ts, tz=pytz.timezone('EET'))
print(dt)
