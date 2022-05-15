import yaml

def send_text(text, phone_number):
    '''
    Use pip3 install twilio to install the correct module.
    send_text receives a string text message and a target phone number
    that uses the twilio rest API to send a notification.
    phone_number must be a string and include the country code (i.e. "+15551234567")
    '''

    with open(r"./twilio_auth.yaml") as file:
        auth_codes = yaml.load(file, Loader=yaml.FullLoader)

    from twilio.rest import Client
    # Account SID :
    account_sid = auth_codes["account_sid"]
    # Auth Token :
    auth_token  = auth_codes["auth_token"]
    # Message-receiving phone number :
    receiving_number = phone_number
    # Message-sending Twilio phone number :
    twilio_number = auth_codes["twilio_number"]

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to= phone_number,
        from_= twilio_number,
        body= text)
