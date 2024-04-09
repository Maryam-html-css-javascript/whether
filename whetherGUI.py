
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 06:40:53 2024

@author: Arooj
"""

from tkinter import *
import tkinter as tk

from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def getWeather():
    city=textfeild.get()
    
    geolocator= Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    #print(result)    #its mean its working
    home= pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.configure(text=current_time)
    name.configure(text="CURRENT WEATHER") 
    
    #WEATHER
    api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(location.latitude) + "&lon=" + str(location.longitude) + "&appid=b20dc427a5e34543f443e4f80e424a36"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    
    t.configure(text=(temp, "°"))
    c.configure(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
    w.configure(text=wind)
    h.configure(text=humidity)
    d.configure(text=description)
    p.configure(text=pressure)
 
    
  #except Exception as e:
      #messagebox.showerror("Weather App","Invalid Entry!! Check later")


root = Tk()
root.title("Weather App By Maryam Siddiqui (2021-BCS-027)")
root.geometry("900x500+300+200")
root.resizable(False,False)


#searchbox

search_image=PhotoImage(file="copy of search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)
textfeild=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfeild.place(x=50,y=40)
textfeild.focus()


#searchbox-icon
search_icon=PhotoImage(file="copy of search_icon.png")
my_image_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
my_image_icon.place(x=400,y=34)


#logo


logo_image=PhotoImage(file="copy of logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#bottom box

frame_image=PhotoImage(file="copy of box.png")
frame_myimage=Label(image=frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)


#time

name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(font=("Helvetica",20))
clock.place(x=30,y=130)


#lable


lable1=Label(root,text="Wind",font=("Helvetica",15,"bold"),fg="black",bg="#1ab5ef")
lable1.place(x=120,y=400)


lable2=Label(root,text="Humidity",font=("Helvetica",15,"bold"),fg="black",bg="#1ab5ef")
lable2.place(x=250,y=400)


lable3=Label(root,text="Discription",font=("Helvetica",15,"bold"),fg="black",bg="#1ab5ef")
lable3.place(x=430,y=400)


lable4=Label(root,text="Pressure",font=("Helvetica",15,"bold"),fg="black",bg="#1ab5ef")
lable4.place(x=650,y=400)


t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=130)

w=Label(text="...",font=("arial",15,"bold"),fg="white",bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",15,"bold"),fg="white",bg="#1ab5ef")
h.place(x=250,y=430)
d=Label(text="...",font=("arial",15,"bold"),fg="white",bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text="...",font=("arial",15,"bold"),fg="white",bg="#1ab5ef")
p.place(x=650,y=430)


root.mainloop()
