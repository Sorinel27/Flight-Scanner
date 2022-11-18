import requests
import datetime
from data_manager import DataManager
from flight_data import FlightData


class FlightSearch(FlightData):
    def __init__(self):
        super().__init__()
        self.api_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.today = datetime.datetime.now()
        self.day_now = self.today.strftime("%d/%m/%Y")
        self.date_to = "30/09/2023"
        self.price_list = []
        for i in range(len(self.IATA_list)):
            self.parameters = {
                "fly_from": "CLJ",
                "fly_to": self.IATA_list[i],
                "date_from": self.day_now,
                "date_to": self.date_to,
                "nights_in_dst_from": 1,
                "nights_in_dst_to": 8,
                "flight_type": "round",
                # "max_stopovers": 0,          # uncomment this line if you want direct flights
                "adults": 1,
                "curr": "RON",
                "sort": "price",
                "limit": 20
            }
            self.response = requests.get(url=self.api_endpoint, params=self.parameters, headers=self.headers)
            self.data = self.response.json()
            print(self.cities[i])
            print(self.data)
            self.price_list.append(self.data['data'][0]['price'])
            new_data = {
                "price": {
                    'city': self.cities[i],
                    'iataCode': self.IATA_list[i],
                    'lowestPrice': self.data['data'][0]['price']
                }
            }
            self.response = requests.put(url=f"https://api.sheety.co/2ea6a3db5160e5151243478f56fd811d/flightDeals/prices/{i + 2}", json=new_data)
            print(self.response.text)
