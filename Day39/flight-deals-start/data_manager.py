import requests
SHEETY_ENDP = "https://api.sheety.co/f9d79a13bbae31e69acbd53747aee9c6/flights/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDP)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for entry in self.destination_data:
            new_sheet = {
             "price": {
                 "iataCode": entry["iataCode"],
             }
            }
            response = requests.put(url = f"{SHEETY_ENDP}/{entry['id']}", json=new_sheet)
            print(response.text)







