# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC75bb202fd9318488f0cdcd393131b945'
auth_token = 'a231daa663d0359b7322b3b9bb82d19b'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="Why couldn't it be reached?",
         from_='+13139864727',
         to='+821099921010'
     )

# print(message.sid)