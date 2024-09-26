import os
import requests
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]

SHEET_NAME = os.environ["SHEET_NAME"]
PROJECT_NAME = os.environ["PROJECT_NAME"]
USERNAME = os.environ["USERNAME"]
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

WEIGHT = 85
HEIGHT = 185
AGE = 24

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

query = input("Tell me which exercises you did: ")

data = {
    "query": query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

request = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=data)
request.raise_for_status()

request_data = request.json()
print(request_data)

today = datetime.today()

date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for exercise in request_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}
sheet_response = requests.post(
    url=SHEETY_ENDPOINT,
    json=sheet_inputs,
    headers=bearer_headers
)
print(sheet_response)
