import requests
import os
from twilio.rest import Client
#http://jsonviewer.stack.hu/

account_sid = "AC8fddf4724b23c0c6d6ca7e83ea0a2330"
auth_token = "66ce2331335d85f98450404c3cdd7c2d"


api_key = os.environ.get("OWM_API_KEY")
#https://api.openweathermap.org/data/2.5/onecall?lat=51.227741&lon=6.773456&appid=90b916ad8eea35c97292b7963be5300d
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_param = {
    "lat": 51.227741,
    "lon": 6.773456,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}



response = requests.get(OWM_Endpoint, params=weather_param)
#print(response.status_code)

#to raise an exception in case of error
response.raise_for_status()

will_rain = False
for x in range(0,8):
  weather_data = response.json()["hourly"][x]["weather"][0]["id"]
  if weather_data > 700:
      will_rain = True
      
if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella.",
        from_='+16074994596',
        to='+4915223386087'
    )

    print(message.status)

