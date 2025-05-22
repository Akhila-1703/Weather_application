# 🌤️ Weather Application

A simple yet powerful **Python console-based weather app** that fetches real-time weather data using the [OpenWeatherMap API](https://openweathermap.org/api).  
It displays temperature, humidity, and wind speed for any city and **stores search history** in a local **SQLite database**.

---

## 🚀 Features

✅ Real-time weather info (🌡️ temperature, 💧 humidity, 🌬️ wind speed)  
✅ City name input via console  
✅ History saved locally in `weather_history.db`  
✅ Handles API & network errors gracefully  
✅ Clean and beginner-friendly Python code

---

## 📦 Technologies Used

- **Python 3.x**
- **Requests** (HTTP requests)
- **SQLite** (database for search history)
- **OpenWeatherMap API** (data source)

---

## 🛠️ Setup Instructions

### 1. 🧬 Clone the Repository

```
git clone https://github.com/Akhila-1703/Weather_application.git
cd Weather_application
```
2. 📦 Install Dependencies
Install the required Python library:

```
pip install requests
```
3. 🔑 Get an API Key from OpenWeatherMap
Go to OpenWeatherMap Sign Up and create a free account.

After logging in, go to the API keys section.

Copy the default key or create a new one.

Open weather.py in any text editor.

Replace this line:
```
API_KEY = "YOUR_API_KEY"
```
with your actual key:
```
API_KEY = "your_actual_api_key_here"
```
▶️ Running the Application
Run the app using:
```
python weather.py
```
You'll be prompted to enter a city name. Type exit to quit the app.
🧪 Sample Input / Output
```
Enter city name (or type 'exit' to quit): London
Weather in London:
Temperature: 15.0°C
Humidity: 72%
Wind Speed: 3.5 m/s

Enter city name (or type 'exit' to quit): InvalidCity
City not found. Please check the name and try again.

Enter city name (or type 'exit' to quit): exit
Exiting the program. Goodbye!
```
🧠 Error Handling
❌ Invalid city → “City not found” message

🌐 Network/API issues → Proper error message (no crashing)

🔐 API key missing/wrong → Message guides user to fix it

🧰 Optional Features (Coming Soon)
🖼️ GUI using Tkinter

📊 Reports using Pandas

📝 Logging user activity to a log file
🙌 Contribution & Support
🛠️ Found a bug? Have a feature request?
Feel free to open an issue or submit a pull request.

📬 For questions or feedback, email:
akhiladhachepally@gmail.com
🙏 Thank You
Thank you for using the Weather Application!
