import requests
from twilio.rest import Client


client = Client(account_sid, auth_token)

weather_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{LOCATION_KEY}?apikey={ACCU_KEY}&details=True&metric=True"

req_data = requests.get(weather_url)
resp_data = req_data.json()

headline = resp_data["Headline"]["Text"]

date = resp_data['DailyForecasts'][0]["Date"][0:10]

temp_min = resp_data['DailyForecasts'][0]["Temperature"]["Minimum"]["Value"]
temp_max = resp_data['DailyForecasts'][0]["Temperature"]["Maximum"]["Value"]

weather_day = resp_data['DailyForecasts'][0]["Day"]
weather_night = resp_data['DailyForecasts'][0]["Night"]

air_quality = resp_data['DailyForecasts'][0]["AirAndPollen"][0]

sun_hours = resp_data['DailyForecasts'][0]["HoursOfSun"]
rain_hours_day = weather_day["HoursOfRain"]
rain_hours_night = weather_night["HoursOfRain"]

forecast = f"""
Headline: {headline}

Date: {date}

Temperature:
  Minimum: {temp_min}°C
  Maximum: {temp_max}°C

Weather:
  Day: {weather_day['IconPhrase']}, {weather_day['RainProbability']}% chance of rain, {rain_hours_day} hours of rain
  Night: {weather_night['IconPhrase']}

Air Quality: {air_quality['Category']}

Sun Hours: {sun_hours} hours

Rain Hours:
  Day: {rain_hours_day} hours
  Night: {rain_hours_night} hours
"""

message = client.messages.create(
    messaging_service_sid=MESSAGE__ID,
    body = forecast,
  to=PHONE_NUMBER
)


