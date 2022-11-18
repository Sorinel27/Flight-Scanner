import requests


class DataManager:
    def __init__(self):
        self.api_endpoint = "https://api.sheety.co/2ea6a3db5160e5151243478f56fd811d/flightDeals/prices"
        self.response = requests.get(self.api_endpoint)
        print(self.response.text)
        self.ap = self.response.json()
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
        print(self.response.text)

    def refresh_cities(self):
        self.bucket_list = []
        for item in self.ap['prices']:
            self.bucket_list.append(item['city'])
        return self.bucket_list
