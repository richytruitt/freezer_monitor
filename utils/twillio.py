from twilio.rest import Client

class TwillioBuilder:

    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(account_sid, auth_token)
        self.recievers = ['+14433562092']

    def send_message(self, message):

        for number in self.recievers:
            self.client.messages.create(
                body=message,
                from_='+19378712494',
                to=number
            )
