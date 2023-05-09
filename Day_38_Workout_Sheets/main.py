import requests
import json
from datetime import datetime
from dotenv import dotenv_values

env = dotenv_values("../.env")
APP_ID = env["APP_ID_NUTRI"]
API_KEY = env["API_KEY_NUTRI"]
API_KEY_SHEETY = env["API_KEY_SHEETY"]
FILE_NAME = env["FILE_NAME"]
SHEETY_TOKEN = env["SHEETY_TOKEN"]
nutritionix = "https://trackapi.nutritionix.com"
sheety = "https://api.sheety.co"

exercise_query = input("Which exercise you did? ")
# ran 17 miles and walked 2 miles

def post_response_from_nutritionix(query):
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }

    request_body = {
     "query": query,
     "gender": "female",
     "weight_kg": 72.5,
     "height_cm": 167.64,
     "age": 30
    }

    url = f"{nutritionix}/v2/natural/exercise"

    return requests.post(url=url, json=request_body, headers=headers)
    # print(json.dumps(response.json(), indent=2))


def post_exercises_to_sheety(exercises):
    sheety_url = f"{sheety}/{API_KEY_SHEETY}/{FILE_NAME}/sheet1"
    now = datetime.now()
    for exercise in exercises:
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }
        request_body = {
            "sheet1": {
                "date": now.date().strftime("%d/%m/%Y"),
                "time": now.time().strftime("%H:%M:%S"),
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        requests.post(url=sheety_url, json=request_body, headers=headers)
        # response = requests.post(url=sheety_url, json=request_body)
        # print(response.text)

response = post_response_from_nutritionix(exercise_query)

post_exercises_to_sheety(response.json()["exercises"])
