# Workout Tracker with Google Sheets & Sheety API 🏋️‍♂️

A Python script that tracks your workouts using Natural Language Processing. Simply type what exercises you did in plain English (e.g., *"Ran 3 miles in the mountains"*), and it will automatically calculate duration and calories burned, then log the entry directly into your Google Sheet.

---

##  How It Works

1. **Natural Language Processing (Nutritionix API)**: Analyzes your natural text query and computes calories burned based on your body weight, height, age, and gender.
2. **Google Sheets Sync (Sheety API)**: Automatically posts the workout details (Date, Time, Exercise, Duration, Calories) as a new row in your connected Google Sheet.
3. **Retrieval**: Fetches and displays all workout entries currently recorded in your sheet.

---

##  Getting Started

### 1. Prerequisites

Ensure you have Python installed, then install the required dependencies:

```bash
pip install requests python-dotenv
```

### 2. Environment Setup

Create a `.env` file in the project root (you can copy `.env.example`):

```env
# Nutritionix / Exercise API Credentials
NUTRITIONIX_APP_ID=your_nutritionix_app_id
NUTRITIONIX_API_KEY=your_nutritionix_api_key
EXERCISE_ENDPOINT=https://app.100daysofpython.dev/v1/nutrition/natural/exercise

# Sheety API Credentials
SHEETY_ENDPOINT=https://api.sheety.co/your_user_id/your_project/workouts
SHEETY_TOKEN=your_sheety_bearer_token

# User Stats (used for calorie calculations)
USER_GENDER=male
USER_WEIGHT_KG=70
USER_HEIGHT_CM=180
USER_AGE=23
---

**Example:**
```text
What did you do Today : Ran 5 km and cycled for 30 minutes
Logged: Running - 30.0 mins, 310.5 kcal
Logged: Cycling - 30.0 mins, 215.0 kcal
updated sheet....Done!!
```
