import requests
import time
from data_manager import DataManager


class FlightData(DataManager):
    def __init__(self):
        super().__init__()
        self.cities = self.refresh_cities()
        self.api_endpoint = "https://api.tequila.kiwi.com/"
        self.api_location = "locations/query"
        self.api_key = ":)"
        self.headers = {
            "apikey": self.api_key
        }
        self.IATA_list = []
        for i in range(len(self.cities)):
            self.parameters = {
                'term': self.cities[i],
                'limit': 1,
            }
            self.IATA_list.append(self.get_IATA())
        for i in range(len(self.cities)):
            new_data = {
                "price": {
                    'city': self.cities[i],
                    'iataCode': self.IATA_list[i],
                    'lowestPrice': ""
                }
            }
            self.response = requests.put(url=f"https://api.sheety.co/9bce717d4d00503b99ac5554c9944ba9/flightDeals/prices/{i + 2}", json=new_data)
        self.response = requests.get(url=f"{self.api_endpoint}{self.api_location}", headers=self.headers,
                                     params=self.parameters)

    def get_IATA(self):
        time.sleep(2)
        self.response = requests.get(url=f"{self.api_endpoint}{self.api_location}", headers=self.headers,
                                     params=self.parameters)
        data = self.response.json()
        print(data)
        return data['locations'][0]['code']
