from dotenv import load_dotenv
import geocoder
import requests
import os

def get_current_location():
    g = geocoder.ip('me')  # Uses your public IP
    if g.ok:
        city = g.city
        state = g.state
        country = g.country
        lat = g.latlng[0]
        lon = g.latlng[1]

        print("📍 Your Location Info:")
        print(f"City: {city}")
        print(f"State: {state}")
        print(f"Country: {country}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")

        get_weather_forecast(lat, lon)
    else:
        print("❌ Could not determine location.")

def get_weather_forecast(lat, lon):
    load_dotenv()
    
    # Get the API key from environment variables
    api_key = os.getenv("OpenWeatherMap_API_key")
    
    if not api_key:
        raise ValueError("API key not found. Make sure it's set in the .env file.")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            print("❌ Weather data error:", data.get("message"))
            return

        print("\n🌦️ Current Weather Forecast:")
        print(f"🌡️ Temperature: {data['main']['temp']} °C")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        print(f"🌫️ Weather: {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
    except Exception as e:
        print("❌ Failed to fetch weather:", e)

if __name__ == "__main__":
    get_current_location()
