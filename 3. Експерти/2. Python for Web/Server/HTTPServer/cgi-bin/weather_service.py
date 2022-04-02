import requests
import pytz
from datetime import datetime
import json


def get_weather(city_name):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather',    # основен URL
                            params={   # GET параметри - dict
                                'q': city_name,
                                'appid': '4d1231103d3ac41e56becfa993f6e17e'
                            },
                            timeout=20,  # seconds
                            )

    # От извикването по-горе, библиотеката ще композира пълния URL:

    response_text = response.text
    json_text = json.loads(response_text)

    weather = json_text["weather"]

    return weather[0]['main']
