import requests

# http://127.0.0.1:5000/?currency1=BGN&currency2=USD&amount=1000

response = requests.get('http://127.0.0.1:5000',
                        params={
                                'currency1': 'BGN',
                                'currency2': 'USD',
                                'amount': 500
                            })

print(response.text)
