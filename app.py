from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    
    body = request.values.get('Body', None)

    resp = MessagingResponse()

    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")

    return str(resp)
