import requests
from flight_data import FlightData

FLIGHT_API_2 = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_KEY = ""

def search_flight():
        head = {
            "apikey": TEQUILA_KEY,
        }
        query = {
            "fly_from": "DUS",
            "fly_to": "LON",
            "date_from": "02/06/2022",
            "date_to": "20/06/2022",
            "nights_in_dst_from": 1,
            "nights_in_dst_to": 2,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        resp = requests.get(url=FLIGHT_API_2, headers=head, params=query)
        result = resp.json()
        data = result["data"][0]
        print(result["data"][0])

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return(flight_data)