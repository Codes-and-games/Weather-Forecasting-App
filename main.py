from tkinter import messagebox
import requests
from configparser import ConfigParser
from datetime import *


url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


configfile = 'config.ini'
config = ConfigParser()
config.read(configfile)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        data = result.json()
        city = data["name"]
        country = data["sys"]["country"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = round(float(temp_kelvin) - 273.15)
        temp_fahrenheit = round(float(temp_kelvin) - 273.15 * 9/5 + 32, 2)
        icon = data["weather"][0]["icon"]
        weather = data["weather"][0]["main"]
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location["text"] = f"{weather[0]}, {weather[1]}"
        Weather["text"] = weather[5]
        img["file"] = f'Images//{weather[4]}.png'
        temperature["text"] = f"{weather[2]}°C, {weather[3]}°F"
    else:
        messagebox.showerror("Oops", f"Cannot find the city: {city}")



from tkinter import *
#
window = Tk()
window.geometry('700x350')
window.title("Weather Forecast")


city_text = StringVar()
entry = Entry(window,  textvariable=city_text)
entry.pack()

search_city = Button(text="Search For City", command=search, width=12)
search_city.pack()

location = Label(window, text="", width=12, font=("Bold", 20))
location.pack()

img = PhotoImage(file="")
Image = Label(window, image=img)
Image.pack()


temperature = Label(window, text="", width=330, font=("Bold", 20))
temperature.pack()

Weather = Label(window, text="", width=12, font=("Bold", 20))
Weather.pack()



window.mainloop()

########################################################################################################################




