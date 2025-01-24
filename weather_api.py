import requests

def connect(city):

    with open ('api_key.txt', 'r') as file:
        API_KEY = file.read().strip()
    URL = 'http://api.weatherstack.com/current?access_key=' + API_KEY + '&query=' + city
    response = requests.get(URL)
    return response.json()
