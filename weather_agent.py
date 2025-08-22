import requests
import os
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler


# 1. Load the API key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# 2. Function to fetch weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"Weather in {city}: {weather}, {temp}°C"
    else:
        return f"Error: {data['message']}"

# 3. "Agent" role: ask user → call API → print result

def scheduled_weather_check():
    city = "Hyderabad"
    print(get_weather(city))

scheduler = BlockingScheduler()
@scheduler.scheduled_job('interval',hours=1)
def job():
    scheduled_weather_check()


if __name__ == "__main__":
    print("Starting Weather Agent...")
    scheduler.start()
