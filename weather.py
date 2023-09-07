import tkinter as tk
import requests
from PIL import Image, ImageTk

def get_weather():
    city = city_entry.get()
    api_key = "043c0fd0d38edd55ee20eb7c58486080"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=043c0fd0d38edd55ee20eb7c58486080&units=metric"

    response = requests.get(url)
    data = response.json()

    try:
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity=data["main"]["humidity"]
        wind_data=data["wind"]["speed"]
        result_label.config(text=f"Temperature: {temperature}°C\nCondition: {weather_desc}\nHumidity: {humidity}%\nWind Speed: {wind_data}Kmph")
    except KeyError:
        result_label.config(text="City not found")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.maxsize(400,400)
root.minsize(400,400)


background_image = Image.open("background.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

heading = tk.Label(root, text="Weather App", font=("Arial", 20), bg='white')
heading.pack(pady=10)

city_label = tk.Label(root, text="Enter City:", font=("Arial", 12), bg='lightblue')
city_label.pack()

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(ipadx=10, ipady=10, padx=20)

search_button = tk.Button(
    root,
    text="Search",
    font=("Arial", 12),
    command=get_weather,
    bg='lightblue'
)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg='lightblue')
result_label.pack()

root.mainloop()
