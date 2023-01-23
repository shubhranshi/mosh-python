# Sending text messages using Twilio
# Twilio is a popular communication platform for adding voice, video, and messaging to our application.
# Useful for making/receiving video calls, send text messages for sending appointment reminders or
# for confirming reservation, and much more.
# They provide an API. We can directly communicate with this API by sending HTTP request using requests module.
# But first we need to create a Twilio account.

# install twilio (pip or pipenv)

# twilio library has a wrapper around their API. It has objects that internally take care of sending
# and receiving HTTP requests.

from twilio.rest import Client  # This class represents a client to twilio Rest API
import config

account_sid = "djoiwjqjrwpSecurityIdentifier32CanBeFoundOnTwilioConsole"
auth_token = "msakljf432urewi098AuthenticationToken8437CanBeFoundOnTwilioConsole"
# these 2 keys can be put into config.py file, which will be excluded by git.

client = Client(account_sid, auth_token)
# This client object has some attributes like messages (used to send text messages),
# calls (for making voice calls), fax, video, chat, and so on.

# This create() method takes care of sending the right HTTP request to twilio api, and returns a call object.
call = client.messages.create(
    to="",      # phone number
    from_="",   # twilio number (phone number generated on twilio)
    body="This is our first message"
)
# With this we can send message to any number in the world


