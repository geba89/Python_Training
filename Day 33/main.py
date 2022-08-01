from sqlite3 import paramstyle
from urllib import response
import requests

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# iss_position = (response.json()["iss_position"]["latitude"], response.json()["iss_position"]["longitude"])
# print(iss_position)
parameters = {"lat":50.064651, "lng":19.944981, "formatted":0}
response = requests.get("https://api.sunrise-sunset.org/json", verify=False, params=parameters)


print(response.json())