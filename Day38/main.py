import requests
from datetime import datetime
GENDER = "male"
WEIGHT_KG = 58
HEIGHT_CM = 176
AGE = 21
APP_ID = os.environ["f234b862"]
API_KEY = os.environ["3ef427927ab458b806b881a0f904e117"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


exercise_prompt = input("Tell me which exercises you did:")
sheety ="Get your  end  point of sheet post row"
headers = {
"x-app-id": APP_ID,
"x-app-key": API_KEY,
}
parameters = {
    "query":exercise_prompt,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
today = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date":today,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]

        }
    }

response = requests.post(url=sheety,json=sheet_inputs,auth=("parash","parash123"))
print(response.text)

# Bearer Token
# bearer_headers = {
#     "Authorization": f"Bearer {os.environ['TOKEN']}"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )
#
# print(sheet_response.text)
