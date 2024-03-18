from datetime import datetime
import requests


def nutrix_request():
    nutrix_headers = {
        "x-app-id": "bdc442cf",
        "x-app-key": "26d9f6dc90a6c1c7c1920fa3016dab80",
        "Content-Type": "application/json"
    }
    exercise_param = {
     # "query": input("What have you done today? "),
     "query": "ping pong for 1 hours",
     "gender": "female",
     "weight_kg": 72.5,
     "height_cm": 167.64,
     "age": 30
    }
    exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
    response = requests.post(url=exercise_endpoint, json=exercise_param, headers=nutrix_headers)
    # print(response.text)
    return response.json()["exercises"][0]


def excel_request(data):
    post_endpoint = "https://api.sheety.co/637ddc3f0065d623fb36a17f11a8a156/myWorkouts/workouts"
    date = datetime.now().strftime("%d/%m/%y")
    time = datetime.now().time().strftime("%H:%M")
    workout = {
        "date": date,
        "time": time,
        "exercise": data["name"].title(),
        "duration": data["duration_min"],
        "calories": data["nf_calories"]
    }
    excel_param = {
        "workout": workout
    }

    # basic  authn
    # response = requests.post(url=post_endpoint, json=excel_param, auth=("dzen", "droid"))
    # print(response.text)

    # bearer token authn
    bearer_header = {
        "Authorization": "Bearer ====muahahahahahahahah===="
    }
    response = requests.post(url=post_endpoint, json=excel_param,  headers=bearer_header)
    print(response.text)


excel_request(nutrix_request())
# get_endpoint = "https://api.sheety.co/637ddc3f0065d623fb36a17f11a8a156/myWorkouts/workouts"
# response = requests.get(url=get_endpoint)
# print(response.text)

