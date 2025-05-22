import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_API_KEY"

def fetch_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            messagebox.showerror("Error", "City not found or API error.")
            return
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        result_label.config(text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", str(e))

# Setup GUI window
root = tk.Tk()
root.title("Weather Application")

tk.Label(root, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
