from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/637ddc3f0065d623fb36a17f11a8a156/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=("dzen", "droid"))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=("dzen", "droid")
            )
            print(response.text)
