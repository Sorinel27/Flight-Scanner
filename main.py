import requests
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch


data = DataManager()
print("Welcome to the Flight Scanner!")
print("The current cities are:")
for i in data.bucket_list:
    print(i)
another_city = input("Would you like to add another city?(Y/N): ")
if another_city.lower() == "y":
    another_city = input("Name the city: ")
    data.add_city(another_city)
fd = FlightData()
fs = FlightSearch()