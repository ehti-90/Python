import random
import datetime
import smtplib
from dotenv import load_dotenv
import os



# Load variables from .env
load_dotenv()

MY_EMAIL = os.getenv("my_email")
APP_PASSWORD = os.getenv("APP_PASSWORD")

print(APP_PASSWORD)

with open(file=r"practice projects\SMTP_Module\weekly_motivation_mail\quotes.txt",mode="r") as data:
    all_data = data.read()
    
