import requests
import datetime
import time
from flight_data import FlightData


class FlightSearch(FlightData):
    def __init__(self):
        super().__init__()
        self.api_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.today = datetime.datetime.now()
        self.day_now = self.today.strftime("%d/%m/%Y")
        self.date_to = "30/09/2023"
        self.price_list = []
        self.money = 99999999
        self.sms = ""
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
            cheap_flight_data = self.data['data'][0]
            if int(cheap_flight_data['price']) < self.money:
                self.money = int(cheap_flight_data['price'])
                final_result = self.data['data'][0]
            time.sleep(2)
            try:
                self.price_list.append(self.data['data'][0]['price'])
            except KeyError:
                pass
            new_data = {
                "price": {
                    'city': self.cities[i],
                    'iataCode': self.IATA_list[i],
                    'lowestPrice': self.data['data'][0]['price']
                }
            }
            self.response = requests.put(url=f"https://api.sheety.co/9bce717d4d00503b99ac5554c9944ba9/flightDeals/prices/{i + 2}", json=new_data)
            print(self.response.text)
        self.sms = f"Low price alert! Only {final_result['price']} RON to fly from {final_result['cityFrom']}-{final_result['flyFrom']} to {final_result['cityTo']}-{final_result['flyTo']}, from {final_result['route'][0]['local_departure'].split('T')[0]} to {final_result['route'][1]['local_departure'].split('T')[0]}."