from flask import Flask, request, redirect
from src.food_truck_info import get_n_closest_trucks
from twilio.twiml.messaging_response import MessagingResponse
import re

app = Flask(__name__)    

@app.route("/sms", methods=['POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    
    body = request.values.get('Body', None)

    resp = MessagingResponse()

    exp = re.compile("-?\d{1,3}(\.\d+)?,-?\d{1,3}(\.\d+)?")
    regex_check = exp.match(body)
    if regex_check != None:
        vals = body.split(",")
        lat = float(vals[0].strip())
        lon = float(vals[1].strip())
        resp.message(get_n_closest_trucks(lat,lon,5))
    else:
        resp.message("Please enter a message in the format <latitude,longitude> (i.e. 37,-140)")

    return str(resp)
