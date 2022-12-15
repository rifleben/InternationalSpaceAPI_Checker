import time

import requests
import datetime as dt

MY_LAT = 48.0
MY_LNG = -122.0


def is_overhead():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG:
        return True


def is_night():
    params = {
        "lat": 48.0,
        "lng": -122.0,
        "formatted": 0
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    sun_response.raise_for_status()

    sunrise = (sun_response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = (sun_response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(5)
    if is_overhead() and is_night():
        print("woohoo, look up!!!!!")
    else:
        print("Not yet")
