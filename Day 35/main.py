import requests
from datetime import datetime
from twilio.rest import Client 
import os

API_KEY = os.environ.get("OWM_API_KEY")
LAT = 50.064651
LNG = 19.944981
API = f"https://api.openweathermap.org/data/2.5/forecast"
SID = 'AC775b092a1170804db07ba67fe6a85488' 
TOKEN = os.environ.get("TWILIO_TOKEN") 

params = {"lat" : LAT, "lon" : LNG, "appid" : API_KEY, "units" : "metric", "cnt" : 3}
response = requests.get(API, params)
response.raise_for_status()
json_data = response.json()
current_weather = json_data["list"][1]["weather"][0]["description"]
current_temp = json_data["list"][1]["main"]["feels_like"]


client = Client(SID, TOKEN) 
 
message = client.messages.create(  
                              messaging_service_sid='MGca6e1b32002184d2d6dbdb078e3d8efd', 
                              body=f"Current weather is: {current_weather} and temperature is: {current_temp}",      
                              to='+48512704484' 
                          )