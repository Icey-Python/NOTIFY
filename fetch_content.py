import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


PHONE_NUMBER = "+254702716555"
ACCU_KEY = "8QK6bvSZbM2nlcrmGzMFmm8dtTuUeQfN"
ACCUWEATHER_LOCATION_KEY = "828638"

TWILIO_ACCOUNT_SID = 'AC378ecf70f4815c5698aa80537f92ad92'
TWILIO_AUTH_TOKEN = '748da38c8c31cae2fa4ab6b3948dc490'  
TWILIO_MESSAGE_SERVICE_SID = "MG4c30546092c8388c574a14ab6596131a"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
print(client)

weather_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{ACCUWEATHER_LOCATION_KEY}?apikey={ACCU_KEY}&details=True&metric=True"

weather_data = requests.get(weather_url).json()

headline = weather_data["Headline"]["Text"]
date = weather_data['DailyForecasts'][0]["Date"][0:10]
min_temp = weather_data['DailyForecasts'][0]["Temperature"]["Minimum"]["Value"]
max_temp = weather_data['DailyForecasts'][0]["Temperature"]["Maximum"]["Value"]
day_weather = weather_data['DailyForecasts'][0]["Day"]
night_weather = weather_data['DailyForecasts'][0]["Night"]
air_quality = weather_data['DailyForecasts'][0]["AirAndPollen"][0]
sun_hours = weather_data['DailyForecasts'][0]["HoursOfSun"]
day_rain_hours = day_weather["HoursOfRain"]
night_rain_hours = night_weather["HoursOfRain"]

forecast_msg = f"""
Headline: {headline} 
Date: {date}
Temperature:
Minimum: {min_temp}°C
Maximum: {max_temp}°C
Weather: 
Day: {day_weather['IconPhrase']}, {day_weather['RainProbability']}% chance of rain, {day_rain_hours} hours of rain
Night: {night_weather['IconPhrase']}
Air Quality: {air_quality['Category']}
Sun Hours: {sun_hours} hours
Rain Hours:  
Day: {day_rain_hours} hours
Night: {night_rain_hours} hours
"""
message = client.messages.create(
    messaging_service_sid=TWILIO_MESSAGE_SERVICE_SID, 
    body=forecast_msg,
    to=PHONE_NUMBER
)
# message = client.messages.create(
#     messaging_service_sid=TWILIO_MESSAGE_SERVICE_SID, 
#     body=forecast_msg,
#     to=PHONE_NUMBER
# )
