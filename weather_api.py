import requests
#using weatherapi.com

WEATHER_API_KEY = "2874f6da88984480b06235045222004"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={asset}&aqi=no"

def generate_weather_url(city,api_key):
    new_url = WEATHER_API_URL.format(asset = city, WEATHER_API_KEY = api_key)
    return new_url

def generate_temp(url):
    response = requests.get(url)
    data = response.json()
    temp = data['current']['temp_f']
    return temp

def generate_condition(url):
    response = requests.get(url)
    data = response.json()
    condition = data['current']['condition']['text']
    return condition

def generate_name(url):
    response = requests.get(url)
    data = response.json()
    name = data['location']['name']
    return name

def generate_region(url):
    response = requests.get(url)
    data = response.json()
    region = data['location']['region']
    return region

if __name__ == '__main__':
    user_in = input("Enter city name: ")
    weather_url = generate_weather_url(user_in, WEATHER_API_KEY)
    print("The temperature outside is",generate_temp(weather_url),end=".\n")
    print("The condition is", generate_condition(weather_url), end=".\n")
    print("The city is", generate_name(weather_url) + ",", generate_region(weather_url), end=".\n")