import tkinter as tk
from tkinter import ttk
from tkinter import font
import requests
from PIL import Image, ImageTk
import io

API_KEY = 'd02de8e57f87d9e4e6e1981919ef146e'
CITY = 'Bangalore'


def get_weather(api_key, city):
    """
    Fetches weather data from OpenWeatherMap API.

    Parameters:
    api_key (str): API key for OpenWeatherMap
    city (str): City name for which to fetch the weather

    Returns:
    dict: Weather data containing city, temperature, description, humidity, pressure, and icon
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None


def update_weather():
    """
    Updates the weather information on the Tkinter window.
    """
    weather = get_weather(API_KEY, CITY)
    if weather:
        city_label.config(text=f"{weather['city']}")
        temperature_label.config(text=f"Temperature: {weather['temperature']}°C")
        description_label.config(text=f"Description: {weather['description']}")
        humidity_label.config(text=f"Humidity: {weather['humidity']}%")
        pressure_label.config(text=f"Pressure: {weather['pressure']} hPa")

        icon_url = f"http://openweathermap.org/img/wn/{weather['icon']}@2x.png"
        icon_response = requests.get(icon_url)
        icon_data = icon_response.content
        icon_image = Image.open(io.BytesIO(icon_data))
        icon_photo = ImageTk.PhotoImage(icon_image)
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo
    else:
        city_label.config(text="Error fetching weather data")


root = tk.Tk()
root.title("Weather App")
root.geometry("350x400")
root.configure(bg='#87CEEB')

title_font = font.Font(family="Comic Sans MS", size=16, weight="bold")
subtitle_font = font.Font(family="Helvetica", size=12, weight="bold")
cursive_font = font.Font(family="Lucida Handwriting", size=16, slant="italic", weight="bold")

title_label = ttk.Label(root, text="Weather Information", font=cursive_font, foreground="green", background='#87CEEB')
title_label.pack(pady=10)

icon_label = ttk.Label(root, background='#87CEEB')
icon_label.pack(pady=10)

city_label = ttk.Label(root, text="", font=title_font, background='#87CEEB')
city_label.pack(pady=5)

temperature_label = ttk.Label(root, text="", font=subtitle_font, background='#87CEEB')
temperature_label.pack(pady=5)

description_label = ttk.Label(root, text="", font=subtitle_font, background='#87CEEB')
description_label.pack(pady=5)

humidity_label = ttk.Label(root, text="", font=subtitle_font, background='#87CEEB')
humidity_label.pack(pady=5)

pressure_label = ttk.Label(root, text="", font=subtitle_font, background='#87CEEB')
pressure_label.pack(pady=5)

update_weather()

root.after(600000, update_weather)

root.mainloop()
