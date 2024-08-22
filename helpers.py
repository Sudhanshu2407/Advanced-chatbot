from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")
  
  
import requests
from geopy.geocoders import Nominatim

def get_location():
    response = requests.get("https://ipinfo.io/")
    data = response.json()
    loc = data['loc'].split(',')
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{loc[0]},{loc[1]}")
    return location.address


import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather_description = data["weather"][0]["description"]
        return f"Temperature: {main['temp']}°K\nWeather: {weather_description}"
    else:
        return "City not found."


from newsapi import NewsApiClient

def get_latest_news():
    api = NewsApiClient(api_key='your_newsapi_key')
    top_headlines = api.get_top_headlines(language='en', country='us')
    headlines = [article['title'] for article in top_headlines['articles']]
    return headlines

