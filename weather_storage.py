import sqlite3

def create_table():
    conn = sqlite3.connect("weather_history.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            wind_speed REAL
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(city, temperature, humidity, wind_speed):
    conn = sqlite3.connect("weather_history.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather VALUES (?, ?, ?, ?)", 
                   (city, temperature, humidity, wind_speed))
    conn.commit()
    conn.close()