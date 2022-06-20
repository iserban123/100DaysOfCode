import requests

FLIGHT_API = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_KEY = "ZOJ-pGI1Z_N59bGHxtVmG-W37k8vkBcR"

class FlightSearch:

    def get_flight_info(self, city_name):
        par = {
            "term": city_name,
            "location_types": "city"
        }

        hea = {
    "apikey": TEQUILA_KEY,
     }
        LINK = f"{FLIGHT_API}"
        resp = requests.get(url=FLIGHT_API, headers=hea, params=par)
        result = resp.json()["locations"]
        code = result[0]["code"]
        return code


     def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        FLIGHT_API_2 = "https://tequila-api.kiwi.com/v2/search"
        head = {
         "apikey": TEQUILA_KEY,
          }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": ""
        }

