import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = "c1f2ea0d644fc0038868dfb3b5010fd7"
OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "Example_id"
auth_token = "some_auth_token"

weather_params = {
    "lat": 46.77,
    "lon": 23.58,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OMW_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain.",
        from="+15558675310",
        to="+15558675310"
    )
    print(message.status)

