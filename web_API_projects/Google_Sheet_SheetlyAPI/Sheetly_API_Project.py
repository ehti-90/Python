import os
import requests
import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Nutritionix / Exercise API configuration
EXERCISE_ENDPOINT = os.getenv("EXERCISE_ENDPOINT", "https://app.100daysofpython.dev/v1/nutrition/natural/exercise")
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
APP_KEY = os.getenv("NUTRITIONIX_API_KEY")

# Sheety API configuration
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

# User details for calorie calculation
GENDER = os.getenv("USER_GENDER", "male")
WEIGHT_KG = float(os.getenv("USER_WEIGHT_KG"))
HEIGHT_CM = float(os.getenv("USER_HEIGHT_CM"))
AGE = int(os.getenv("USER_AGE"))

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

my_daily_work = input("What did you do Today : ")
current_date = datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

parameters = {
    "query": my_daily_work,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

exercise_response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
exercise_response.raise_for_status()

needed_data = exercise_response.json()

bearer_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

# Add each exercise to Google Sheets via Sheety API
for exercise_item in needed_data.get("exercises"):
    exercise = exercise_item["name"].title()
    duration = exercise_item["duration_min"]
    calories = exercise_item["nf_calories"]

    added_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    add_data_post_request = requests.post(url=SHEETY_ENDPOINT, json=added_data, headers=bearer_header)
    add_data_post_request.raise_for_status()
    print(f"Logged: {exercise} - {duration} mins, {calories} kcal")

print("updated sheet....Done!!")

# Get sheet data
get_sheet_data = requests.get(url=SHEETY_ENDPOINT, headers=bearer_header)
get_sheet_data.raise_for_status()
print(get_sheet_data.json())
