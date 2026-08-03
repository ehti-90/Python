import smtplib as smtp
import os
import datetime
import pandas
from dotenv import load_dotenv

# Folder where this script (main.py) lives
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

MY_EMAIL = os.getenv("my_email")
APP_PASSWORD = os.getenv("APP_PASSWORD")

my_data = pandas.read_csv(os.path.join(SCRIPT_DIR, "birthdays.csv"))

birthday_dict = {}
for (idx, row) in my_data.iterrows():
    birthday_dict[(row["month"], row["day"])] = [row["email"], row["name"]]

# Gives us today's month and day
today_date = datetime.datetime.now()
month = today_date.month
day = today_date.day

with open(os.path.join(SCRIPT_DIR, "letter_templete.txt"), "r") as data:
    templete_letter = data.read()

if (month, day) in birthday_dict:
    specific_letter = templete_letter.replace("[NAME]", birthday_dict[(month, day)][1])
    recipent_email = birthday_dict[(month, day)][0]

    with smtp.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipent_email,
            msg=f"Subject:One More YEAR Near To GOD!!!!!!!!!! \n\n {specific_letter} "
        )