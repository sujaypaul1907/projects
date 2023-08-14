from tkinter import *
from tkinter import ttk
import requests


#Weather data using Weather API

def data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c1b530f4fc22333f95c4866ad661091f").json()  #weather api link to fetch data
    weather_label1.config(text=data["weather"][0]["main"])
    type_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15))+" "+ "°C")
    pressure_label1.config(text=str(data["main"]["temp"]) + " " + "hPa")


#GUI for Weather App

#GUI sizing and color
win = Tk()
win.title("Weather Forecaster")
win.config(bg="light blue")
win.geometry("600x600")

#GUI Label
name_label = Label(win,text="Weather Forcasting App", font=("Times New Roman", 34, "bold"))
name_label.place(x = 50, y = 50, height = 60, width = 500)

#List of cities to select to get weather data

list_city = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name = StringVar()
com = ttk.Combobox(win,text="Weather Forcasting App", values=list_city, font=("Times New Roman", 20, "bold"), textvariable=city_name)
com.place(x = 100, y = 160, height = 40, width = 400)


#Weather information data

weather_label = Label(win,text="Weather Climate", font=("Times New Roman", 20, "italic"))
weather_label.place(x = 50, y = 320, height = 50, width = 200)

weather_label1 = Label(win,text="", font=("Times New Roman", 20))
weather_label1.place(x = 280, y = 320, height = 50, width = 270)

type_label = Label(win,text="Weather Type", font=("Times New Roman", 20, "italic"))
type_label.place(x = 50, y = 390, height = 50, width = 200)

type_label1 = Label(win,text="", font=("Times New Roman", 20))
type_label1.place(x = 280, y = 390, height = 50, width = 270)

temp_label = Label(win,text="Temperature", font=("Times New Roman", 20, "italic"))
temp_label.place(x = 50, y = 460, height = 50, width = 200)

temp_label1 = Label(win,text="", font=("Times New Roman", 20))
temp_label1.place(x = 280, y = 460, height = 50, width = 270)

pressure_label = Label(win,text="Pressure", font=("Times New Roman", 20, "italic"))
pressure_label.place(x = 50, y = 530, height = 50, width = 200)
  
pressure_label1 = Label(win,text="", font=("Times New Roman", 20))
pressure_label1.place(x = 280, y = 530, height = 50, width = 270)

#Button to fetch data

submit = Button(win,text="Submit", font=("Times New Roman", 25, "bold"), command=data)
submit.place(x = 225, y = 230, height = 40, width = 150)


win.mainloop()