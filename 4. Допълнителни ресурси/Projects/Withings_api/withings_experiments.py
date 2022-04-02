import requests

response = requests.get('http://api.openweathermap.org/data/2.5/weather',    # основен URL
                        params={   # GET параметри - dict
                            'q': 'Sofia',
                            'appid': '4d1231103d3ac41e56becfa993f6e17e'
                            },
                        timeout=20,  # seconds
                        )