import requests
from weather_storage import create_table, save_to_db


def get_weather(city):
    API_KEY = "86b13892c3af888c9f1fe382dfe8275d"  # Replace with your actual OpenWeatherMap API key
    print(f"Using API key: {API_KEY}")
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        print("Request URL:", response.url)
        print("Status code:", response.status_code)
        print("Response text:", response.text)

        # Add your error handling here:
        if response.status_code != 200:
            print("Error: City not found or API issue. Please check your input and API key.")
            return
        
        data = response.json()

        if "main" in data:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            save_to_db(city, temperature, humidity, wind_speed)
        else:
            print("City not found. Please check the name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    create_table()
    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            break
        get_weather(city)
