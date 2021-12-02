# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

def check(s):
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
    account_sid = 'AC7862e1d5297ab7b7f7ecb6e38b6234c5'
    auth_token = 'ae5d0ea1360da9b9d8eb581e3b6d8a95'
    client = Client(account_sid, auth_token)

    add_ons_data = {"payfone_tcpa_compliance.RightPartyContactedDate": "20160101"}

    message = client.messages \
                    .create(
                        body="There is an emergency, please contact me asap! /n",
                        messaging_service_sid='MGebdde9c0b739667e40d45bcc7aa9a9c3',
                        from_='+18508012069',
                        to='+91'+s
                    )

    print(message.sid)
