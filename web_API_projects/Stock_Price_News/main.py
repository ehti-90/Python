import requests_cache
import datetime
from dotenv import load_dotenv
import os
import smtplib as smtp



# Folder where this script (main.py) lives
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))


MY_EMAIL = os.getenv("my_email")
APP_PASSWORD = os.getenv("APP_PASSWORD")
recipent_email = os.getenv("my_email")  # YOU can send to yourself

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# free key donT WORRY nothing premium
API_KEY = "K1GT98SDBXLBZYBE"
NEWS_API_KEY = "205f04be5e914e0dbcbb4d97b4c0ad80"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": API_KEY,
}

session = requests_cache.CachedSession("stock_price_cache")
response = session.get(
    url=STOCK_ENDPOINT,
    params=parameters
)

response.raise_for_status()
data = response.json()

#  yestarday date 
yestarday = str(datetime.datetime.now().date() - datetime.timedelta(days=1))
#    Day before yestarday  date
before_yestarday = str(datetime.datetime.now().date() - datetime.timedelta(days=2))


# Taking out closing Prices
yestarday_closing = float(data["Time Series (Daily)"][yestarday]["4. close"])
before_yestarday_closing = float(data["Time Series (Daily)"][before_yestarday]["4. close"])

difference = (yestarday_closing) - (before_yestarday_closing) 
up_down  = ""

if difference > 0:
    up_down = "^"
else:
    up_down = "v"

diff_percent = abs((difference / before_yestarday_closing) * 100 )

#------------------------------------------ COMPANY NEWS --------------------------------#


if diff_percent > 1:
    
    parameters_2 = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    session_2 = requests_cache.CachedSession("Company_News_Cache")
    response_2 = session_2.get(url=NEWS_ENDPOINT,params=parameters_2)
    response_2.raise_for_status()

    
    title = response_2.json()["articles"][0]["title"]
    content = response_2.json()["articles"][0]["content"]
    uurl = response_2.json()["articles"][0]["url"]



    with smtp.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        
        title = title.encode("ascii", "ignore").decode()
        content = content.encode("ascii", "ignore").decode()
        
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipent_email,
            msg=f"Subject: Stock Alert !!! \n\n {COMPANY_NAME} : {up_down} {round((diff_percent),2)}\n Headline: {title}\n Breif: {content} \n source: {uurl}"
    )


