# Import the necessary modules
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "your_account_sid"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

# Create a new client
client = Client(account_sid, auth_token)

# Send a message
message = client.messages.create(
    to="+15555555555", 
    from_="+15555555555",
    body="Your purchase confirmation code is: 123456")

print(message.sid)
