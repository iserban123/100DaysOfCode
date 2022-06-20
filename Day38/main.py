import time

import requests
import datetime
import os

print(os.getenv("GIGEL"))
#API_K = os.environ["API_KEY"] save API_KEY below to configured env

API_KEY = ""
API_ID = ""
#https://docs.google.com/spreadsheets/d/1Dd-o9Dkn0aYg7x4C5-sF1encgogBvk-OMK5em5kC8mA/edit#gid=488880965

end_p = "https://trackapi.nutritionix.com/v2/natural/exercise"

#Content-Type:application/json, x-app-id:NutritionixAppID, x-app-key:NutritionixAppKey

inp = input("What did you do today:")

headers = {
    "Content-Type":"application/json",
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
     }

query_p = {

    "query": inp,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 36
}

hea = {
    "Content-Type": "application/json",
    "Authorization": "Bearer rtrtfdf565jh232234"
     }


url_shet = "https://api.sheety.co/f9d79a13bbae31e69acbd53747aee9c6/iuli/workouts"
r = requests.post(url=end_p, headers=headers, json=query_p)
result = r.json()
lista_ex = result["exercises"]
date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")
for i in range(len(lista_ex)) :
    sheet_i = {
      "workout": {

         "exercise": lista_ex[i]["user_input"],
         "duration": lista_ex[i]["duration_min"],
         "date": date,
         "calories": lista_ex[i]["nf_calories"],
         "time": time,
     }
    }
    requests.post(url_shet, headers=hea, json=sheet_i)
print(result)




