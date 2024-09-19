import requests
from datetime import datetime
from smtplib import SMTP
import time

MY_LAT = 46.770920 # Your latitude
MY_LONG = 23.589920 # Your longitude
MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "vexnarxlphojwuszh"


def is_in_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

def is_night():
    response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    #If the ISS is close to my current position
    if is_in_range() and sunset < hour_now < sunrise:
        return True
    return False

while True:
    time.sleep(60)
    if is_in_range() and is_night():
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject: ISS ABOVE\n\n Something, haha!")
