import os
import requests
import datetime as dt
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = "VVOX9DXNQC1J7SWS"

NEWS_KEY_API = "b54c2b0f5605488ca24572a2554eb919"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Twilio
account_sid = "Example_id"
auth_token = "some_auth_token"

alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=alphavantage_parameters)
response.raise_for_status()
data = response.json()

today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
last_date_before_yesterday = today-dt.timedelta(days=4)

yesterday_closing_price = float(data["Time Series (Daily)"][str(yesterday)]["4. close"])
last_date_before_yesterday_closing_price = float(data["Time Series (Daily)"][str(last_date_before_yesterday)]["4. close"])

difference = abs(yesterday_closing_price - last_date_before_yesterday_closing_price)
percentage_difference = (difference/last_date_before_yesterday_closing_price) * 100
# percentage_difference = 6

news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "apiKey": NEWS_KEY_API
}
response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response_news.raise_for_status()
news_data = response_news.json()
print(news_data)

articles = [article for article in news_data["articles"]]
first_three_articles = articles[:3]


# proxy_client = TwilioHttpClient()
# for article in first_three_articles:
#     print(article)
#     proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
#     client = Client(account_sid, auth_token, http_client=proxy_client)
#     message = client.messages \
#         .create(
#         body=article,
#         from="+15558675310",
#         to = "+15558675310"
#     )

for article in first_three_articles:
    Headline = articles[1]
    description = articles[2]
    if difference < 0:
        triangle = "🔻"
    else:
        triangle = "🔺"

    message = (f"{STOCK_NAME:} {triangle}{percentage_difference}%\n"
               f"Headline: {news_data} ({STOCK_NAME}?.)\n"
               f"Brief: {description}")
    print(message)
