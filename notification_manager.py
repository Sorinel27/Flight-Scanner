from twilio.rest import Client
from flight_search import FlightSearch


class NotificationManager(FlightSearch):
    def __init__(self):
        super().__init__()
        self.account_sid = 'AC75b71ff80d7412ed3f9a899bd27ddd7d'
        self.auth_token = ':)'
        self.client = Client(self.account_sid, self.auth_token)
        self.message = self.client.messages.create(
            body=self.sms,
            from_='+16293483487',
            to='+40761468119'
        )
        print(self.message.status)
