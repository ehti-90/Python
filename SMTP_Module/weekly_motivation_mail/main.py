import random
import datetime as dt
import smtplib as smtp
from dotenv import load_dotenv
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load variables from .env
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))


MY_EMAIL = os.getenv("my_email")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECEIPENT = os.getenv("my_email") #IF YOU WANT TO SEND IT TO YOURSELF 

with open(file=os.path.join(SCRIPT_DIR, "quotes.txt") ,mode="r") as data:
    all_data = data.readlines() #   gives us all lines in a list 
    
# # # # # # # # cleaned_quotes = [line.strip() for line in all_data] # takes out \n \t thing at end of each line

quote = random.choice(all_data)

# Get Date and Day
date = dt.datetime.now()
weekday = date.weekday()


with smtp.SMTP(host="smtp.gmail.com", port=587) as connection: #google host server and  STARTTLS (Port 587)
    connection.starttls()
    connection.login(user=MY_EMAIL,password=APP_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs=RECEIPENT,msg=f"Subject: Listen Boy!!! \n\n {quote} ")

    

