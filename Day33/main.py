# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()  # status are exceptions
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
import requests
from datetime import datetime

MY_LAT = 28.394857
MY_LNG = 84.124008
parameter = {
    "Lat": MY_LAT,
    "Lng": MY_LNG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)