import requests
from datetime import datetime
USERNAME = "eiulser"
TOKEN = ""
ID_PYTHON = "graph1"
p_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "sdsds23AS43a",
    "username": "eiulser",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=p_endpoint, json=user_params)
# print(response.text)

g_endpoint = f"{p_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Learning Python",
    "unit": "min",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()
date = today.strftime("%Y%m%d")
# response = requests.post(url=g_endpoint, json=graph_config, headers=headers)
# print(response.text)

v_endpoint = f"{p_endpoint}/{USERNAME}/graphs/{ID_PYTHON}/{date}"

v_config = {
   # "date": today.strftime("%Y%m%d"),
    "quantity": "100",
}

response = requests.delete(url=v_endpoint, json=v_config, headers=headers)
print(response.text)


