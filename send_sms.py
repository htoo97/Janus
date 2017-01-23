from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"

client = TwilioRestClient(account_sid, auth_token)

filename = 'email_attachment.jpg'

# replace the string with your phone number used to validate in twilio
RECEIVING_PHONE = "##########"

# replace the string with the phone number you chose in twilio
TWILIO_NUMBER = "##########"

client.messages.create(to=RECEIVING_PHONE, from_=TWILIO_NUMBER, 
body="Looks like you have a guest. Reply 'unlock' to welcome.")
