import datetime as dt
import requests
from twilio.rest import Client 
import os
import math

STOCK_API_KEY = os.environ.get("ALPHAVANTAGE")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_PARAMS = {"function":"TIME_SERIES_DAILY", "symbol":STOCK, "apikey":STOCK_API_KEY}
NEWS_API_KEY = os.environ.get("NEWSAPI")
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything?'
NEWS_PARAMS = {"apikey":NEWS_API_KEY, "q":COMPANY_NAME, "sortBy":"publishedAt", "pageSize":"3", "language":"en", "searchIn":"description"}
SID = 'AC775b092a1170804db07ba67fe6a85488' 
TOKEN = os.environ.get("TWILIO_TOKEN")



response = requests.get(STOCK_API_ENDPOINT, STOCK_PARAMS)
response.raise_for_status()

yesterday = dt.datetime.today() - dt.timedelta(days=5)
day_before = dt.datetime.today() - dt.timedelta(days=4)


recent_tsla = response.json()["Time Series (Daily)"][str(yesterday.date())]["4. close"]
day_before_tesla = response.json()["Time Series (Daily)"][str(day_before.date())]["4. close"]

change_tesla = (100 * float(day_before_tesla) / float(recent_tsla))

if change_tesla > 105 or change_tesla < 95:
    response = requests.get(NEWS_API_ENDPOINT, NEWS_PARAMS)
    response.raise_for_status()
    news_data = response.json()
    headlines = []
    for headline in news_data["articles"]:
        headlines.append(headline["title"])

    message_body = f"Tesla Stock change: {math.floor((100-change_tesla)*-1)}."
    for title in headlines:
        message_body = message_body + f"\nTitle: {title}"
    client = Client(SID, TOKEN) 
    message = client.messages.create(  
                              messaging_service_sid='MGca6e1b32002184d2d6dbdb078e3d8efd', 
                              body=message_body,      
                              to='+48512704484' 
                          )
 