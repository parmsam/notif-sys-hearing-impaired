def send_text(text, phone_number,auth_token):
    '''
    Use pip3 install twilio to install the correct module.
    send_text receives a string text message and a target phone number
    that uses the twilio rest API to send a notification.
    phone_number must be a string and include the country code (i.e. "+15551234567")
    Requires Twilio auth_token.
    '''
    from twilio.rest import Client
    # Account SID :
    account_sid = "AC8490704432ab402ed61a4d743b961f17"
    # Message-receiving phone number :
    receiving_number = phone_number
    # Message-sending Twilio phone number :
    twilio_number = "+19379303467"


    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to= phone_number,
        from_= twilio_number,
        body= text)

    print(message.sid)