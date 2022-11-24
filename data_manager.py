import requests


class DataManager:
    def __init__(self):
        self.api_endpoint = "https://api.sheety.co/9bce717d4d00503b99ac5554c9944ba9/flightDeals/prices"
        self.response = requests.get(self.api_endpoint)
        self.ap = self.response.json()
        print(self.ap)
        self.bucket_list = []
        for item in self.ap['prices']:
            self.bucket_list.append(item['city'])

    def add_city(self, city):
        new_city = {
            "price": {
                'city': city,
                'iataCode': "",
                'lowestPrice': ""
            }
        }
        self.response = requests.post(url=self.api_endpoint, json=new_city)

    def refresh_cities(self):
        self.bucket_list = []
        for item in self.ap['prices']:
            self.bucket_list.append(item['city'])
        return self.bucket_list
