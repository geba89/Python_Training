import requests
import datetime


neutronix_app_id = "66bc83a6"
neutronix_api_key = ""
natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
natural_exercise_headers = {"x-app-id":neutronix_app_id, "x-app-key":neutronix_api_key, "Content-Type":"application/json"}

sheety_endpoint = "https://api.sheety.co/7c9cb8f1c70d07d431d7ce92a7f6223a/myWorkouts/workouts"
sheety_headers = {"Authorization":"Bearer "}

exercises_input = input("What training did you do today?")
user_data = {"query":exercises_input, "gender":"male", "weight_kg":105, "height_cm":179, "age":33}
response = requests.post(natural_exercise_endpoint, json=user_data, headers=natural_exercise_headers)

for exercise in response.json()['exercises']:
    exercise_params = {"workout": {"date":str(datetime.datetime.today().strftime("%Y-%m-%d")),
     "time":str(datetime.datetime.today().strftime("%H:%M:%S")),
      "exercise":exercise['name'],
      "duration":exercise['duration_min'],
      "calories":exercise['nf_calories']}}
    response = requests.post(sheety_endpoint, json=exercise_params, headers=sheety_headers)
    print(response.json())

