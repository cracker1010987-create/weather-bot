from crawler import crawl_info
from llm import weather_forecast
import requests
import os

morning_weather, morning_rain, afternoon_rain, afternoon_weather, lowest_temp, highest_temp = crawl_info()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

message = weather_forecast(morning_weather,
                            morning_rain,
                            afternoon_rain,
                            afternoon_weather,
                            lowest_temp,
                            highest_temp)

requests.post(
    WEBHOOK_URL,
    json={
        "text": message
    }
)