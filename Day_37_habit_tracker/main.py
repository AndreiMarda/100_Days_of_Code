import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "andrei212223"
TOKEN = "h1djsa3kjs2hd5hs9kj"
GRAPH_ID = "graph1"
QUANTITY = 6.34
TODAY = datetime.datetime.today()
UPDATE_DISTANCE = 4

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint,json=graph_config, headers=headers)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

if TODAY.month < 10:
    current_month = f"0{TODAY.month}"
else:
    current_month = TODAY.month

if TODAY.day < 10:
    current_day = f"0{TODAY.day}"
else:
    current_day = TODAY.day

post_date = f"{TODAY.year}{current_month}{current_day}"

pixel_data = {
    # "date": post_date,
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": input("How many Km did you run today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
response.raise_for_status()
print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY.strftime("%Y%m%d")}"

update_data = {
    "quantity": str(UPDATE_DISTANCE),
}

# response = requests.put(url=update_endpoint, headers=headers, json=update_data)
# response.raise_for_status()
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY.strftime("%Y%m%d")}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

