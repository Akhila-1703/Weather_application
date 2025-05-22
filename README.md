# Weather Application

A simple Python console-based weather application that fetches real-time weather data from the OpenWeatherMap API.  
It displays temperature, humidity, and wind speed for a user-input city and stores search history in a local SQLite database.

---

## Features

- Fetch current weather information (temperature, humidity, wind speed) by city name  
- Stores search history persistently using SQLite (`weather_history.db`)  
- User-friendly console interface  
- Basic error handling for invalid city names and API errors  

---

## Prerequisites

- Python 3.x installed on your machine  
- An API key from [OpenWeatherMap](https://openweathermap.org/api) (free to sign up)  

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Akhila-1703/Weather_application.git
cd Weather_application
2. Install Dependencies
Install the required Python package using pip:

bash
pip install requests
3. Generate OpenWeatherMap API Key
Go to OpenWeatherMap Sign Up and create a free account.

After logging in, navigate to the API keys section in your account dashboard.

Copy the default API key or create a new one.

Open weather.py in a text editor.

Replace the line:

API_KEY = "YOUR_API_KEY"
with your actual API key, for example:

API_KEY = "86b13892c3af888c9f1fe382dfe8275d"
Running the Application
Run the application by executing:

python weather.py
When prompted, enter the city name to fetch the current weather.

Type exit to close the application.

Sample Input / Output
bash
Copy
Edit
Enter city name (or type 'exit' to quit): London
Weather in London:
Temperature: 15.0°C
Humidity: 72%
Wind Speed: 3.5 m/s

Enter city name (or type 'exit' to quit): InvalidCity
City not found. Please check the name and try again.

Enter city name (or type 'exit' to quit): exit
Exiting the program. Goodbye!


Gracefully handles invalid city names with a user-friendly message

Handles API and network errors to avoid crashing

Optional Features (Not Implemented)
GUI using Tkinter

Data analysis and reports with Pandas

Logging to a file

Contribution & Support
Feel free to open issues or submit pull requests.
For questions, mail: akhiladhachepally@gmail.com

Thank you for using the Weather Application!
