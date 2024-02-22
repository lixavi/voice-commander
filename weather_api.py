# weather_api.py

import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, location):
        try:
            params = {"q": location, "appid": self.api_key, "units": "metric"}
            response = requests.get(self.base_url, params=params)
            data = response.json()
            if response.status_code == 200:
                weather_description = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                return f"The weather in {location} is {weather_description} with a temperature of {temperature} degrees Celsius."
            else:
                return "Sorry, unable to fetch weather data at the moment."
        except Exception as e:
            return f"An error occurred: {e}"
