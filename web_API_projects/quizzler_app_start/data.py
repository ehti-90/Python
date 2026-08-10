import requests

# parameters for specific types of questions
parameters = {
    "amount": 5,
    "category": 17,
    "type": "boolean"
}


responce = requests.get(url="https://opentdb.com/api.php", params=parameters)
responce.raise_for_status()

data = responce.json()
question_data = (data["results"])