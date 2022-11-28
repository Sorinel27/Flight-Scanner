import requests
from twilio.rest import Client
from flight_search import FlightSearch
import smtplib


class NotificationManager(FlightSearch):
    def __init__(self, ):
        super().__init__()
        self.account_sid = 'AC75b71ff80d7412ed3f9a899bd27ddd7d'
        self.auth_token = ':)'
        self.client = Client(self.account_sid, self.auth_token)
        self.message = self.client.messages.create(
            body=self.sms,
            from_='+16293483487',
            to='+40761***'
        )
        print(self.message.status)

        self.USER_ENDPOINT = "https://api.sheety.co/9bce717d4d00503b99ac5554c9944ba9/flightDeals/users"
        self.response = requests.get(self.USER_ENDPOINT)
        self.response = self.response.json()
        for item in self.response['users']:
            self.my_email = "soringrape@gmail.com"
            self.my_password = ":)"
            self.connection = smtplib.SMTP("smtp.gmail.com", 587)
            self.connection.ehlo()
            self.connection.starttls()
            self.connection.login(user=self.my_email, password=self.my_password)
            self.connection.sendmail(from_addr=self.my_email,
                                     to_addrs=item['email'],
                                     msg=f"Subject:Flight deal for {item['lastName']} {item['firstName']}!\n\n{self.sms}"
                                     )
            self.connection.close()
