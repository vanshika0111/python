import os
import pytz
import pyowm
#from pyowm import OWM
import streamlit as st 
from matplotlib import dates
from datetime import datetime
from matplotlib import pyplot as plt 

#api key from OpenWeatherMap site 
owm = pyowm.OWM('d2e0d29a3c34333239a0bf46d66f04c1')   #generated api key from OWM
#mgr = owm.weather_manager()

#for streamlit frontend: title and placeholder
st.title("5 Day Weather Forecast")
st.write("### Enter name of the city, unit of temperature and graphical representation")

#input city name and storing it in variable place
place = st.text_input("NAME OF THE CITY: ", "")
if place == None:
    st.write("Enter a city!")

#selection form
unit = st.selectbox("Select temperature unit",("Celsius","Fahrenheit"))
g_type = st.selectbox("Select Graph Type", ("Line Graph","Bar Graph"))

#run the above code using the below command in the terminal
#streamlit run weather_app.py

#def getWeatherInfo(city: str):
 #   owm = OWM('d2e0d29a3c34333239a0bf46d66f04c1')
  #  mgr = owm.weather_manager()
   # obs = mgr.weather_at_place(place+',CZ')
    #w = obs.get_weather()
    #return w
    #observation = owm.weather_at_place('London,uk')
    #w = observation.get_weather()
    #w.get_wind()

#print(getWeatherInfo(place: str) )

#retrieving the forecast
#forecast_at_place(place, '3h', limit=None)
#forecast_at_id(5391959, '3h', limit=None)
#forecast_at_coords(lat=37.774929, lon=-122.419418, interval='3h', limit=None)

#creating an OWM object
#owm
#weatherMananger

#api.openweathermap.org/data/2.5/forecast?id=London,us&appid={'d2e0d29a3c34333239a0bf46d66f04c1'}

#api.openweathermap.org/data/2.5/forecast?q={city name},{state code}&appid={'d2e0d29a3c34333239a0bf46d66f04c1'}

#api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={'d2e0d29a3c34333239a0bf46d66f04c1'}
 

#class pyowm.weatherapi25.weather_manager.WeatherManager('d2e0d29a3c34333239a0bf46d66f04c1', config)

#la = owm.three_hours_forecast('Los Angeles, US')
#print(la.will_have_clouds())

#obs = mgr.weather_at_place(place)

owm = OWM(API_key='d2e0d29a3c34333239a0bf46d66f04c1')
forecast_at_place(place, '3h', limit=None)

