import requests
from config import config


def extract_weather_data(cities, api_key):
    weather_data = []
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data.append(data)
        else:
            print(f"Failed to get data for {city}, status code: {response.status_code}")
    return weather_data
