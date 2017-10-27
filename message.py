# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
import os
# Find these values at https://twilio.com/user/account
#account_sid = "AC364cb68f42e19d3d5e380c24f4fe4c7f"
#auth_token = "701f71763807396d6a56bf1c6f8ea198"

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/token', methods=['GET'])
def get_capability_token():
    """Respond to incoming requests."""


    capability = ClientCapabilityToken(account_sid, auth_token)

    # Twilio Application Sid
    application_sid = 'APd61b3c6d763920a89ea883da47b69aa9'
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming('jenny')
    token = capability.generate()

    return Response(token, mimetype='application/jwt')


def send():
	client.api.account.messages.create(
	    to=os.environ["MY_PHONE_NUMBER"],
	    from_="+12898000264",
	    body="Hello there!")

send()
#resp = twiml.Response()
#resp.message('urgay kid')


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")
    #response.redirect('https://demo.twilio.com/sms/welcome')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
