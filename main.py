import requests
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

USER_ENDPOINT = "https://api.sheety.co/9bce717d4d00503b99ac5554c9944ba9/flightDeals/users"
print("Welcome to the Flight Scanner!")
print("We find the best flight deals and email you.")
first_name = input("Enter your first name:\n")
last_name = input("Enter your last name:\n")
email = input("Enter your email:\n")
confirm = input("Please confirm your email:\n")

if email == confirm:
    add_row = {
        "user": {
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
        }
    }
    response = requests.post(url=USER_ENDPOINT, json=add_row)
    if response.status_code == 200:
        print(f"Success {last_name} {first_name}! Your registration is complete :).")
    else:
        print(f"Error {response.status_code}. The registration is not complete!")
    data = DataManager()
    print("The current cities you want to visit are:")
    for i in data.bucket_list:
        print(i)
    another_city = input("Would you like to add another city?(Y/N): ")
    if another_city.lower() == "y":
        another_city = input("Name the city: ")
        data.add_city(another_city)
    fd = FlightData()
    fs = FlightSearch()
    notification = NotificationManager()
else:
    print("The emails you entered doesn't match!")
