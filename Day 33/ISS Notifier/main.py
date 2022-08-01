import requests
from datetime import datetime

MY_LAT = 50.064651 # Your latitude
MY_LONG = 19.944981 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

lat_diff = abs(MY_LAT - iss_latitude)
long_diff = abs(MY_LONG - iss_longitude)

if lat_diff < 10 and long_diff < 10:
    if time_now.hour > int(sunset) and time_now.hour < int(sunrise):
        print("Check ISS. Look up")




