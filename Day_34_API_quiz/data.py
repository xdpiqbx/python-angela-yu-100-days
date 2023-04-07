import requests

def get_quiz_data():
    params = {
        "amount": 10,
        "type": "boolean"
    }
    response = requests.get(url="https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    return response.json()

question_data = get_quiz_data()["results"]
