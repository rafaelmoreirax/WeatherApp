import requests
import json

def get_weather(city):
    """Fetches weather information for a given city using wttr.in API."""
    # Using the JSON format from wttr.in
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        weather_data = response.json()

        # Extract relevant information
        current_condition = weather_data.get("current_condition", [{}])[0]
        nearest_area = weather_data.get("nearest_area", [{}])[0]
        
        location = nearest_area.get("areaName", [{}])[0].get("value", "N/A")
        region = nearest_area.get("region", [{}])[0].get("value", "N/A")
        country = nearest_area.get("country", [{}])[0].get("value", "N/A")
        
        temp_c = current_condition.get("temp_C", "N/A")
        feels_like_c = current_condition.get("FeelsLikeC", "N/A")
        description = current_condition.get("weatherDesc", [{}])[0].get("value", "N/A")
        humidity = current_condition.get("humidity", "N/A")
        wind_speed_kmph = current_condition.get("windspeedKmph", "N/A")

        print(f"Weather for: {location}, {region}, {country}")
        print(f"Temperature: {temp_c}°C (Feels like: {feels_like_c}°C)")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed_kmph} km/h")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except json.JSONDecodeError:
        print("Error: Could not decode weather data. The city might not be found or the API response changed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("--- Weather App (using wttr.in) ---")
    while True:
        city_name = input("Enter city name (or 'q' to quit): ")
        if city_name.lower() == 'q':
            break
        if city_name:
            get_weather(city_name)
        else:
            print("Please enter a city name.")
        print("---")
    print("Weather app closed.")

