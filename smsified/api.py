"""
A simple wrapper for the SMSified API.
"""

import os
import requests as req
import simplejson as json

URL = "https://api.smsified.com/v1/smsmessaging"


def auth(username=None, password=None):
    """
    Get SMSified username and password authentication from environment
    variables.
    """
    if username and password:
        os.environ['SMS_USER'] = username
        os.environ['SMS_PASS'] = password
    else:
        username = os.environ.get('SMS_USER', '')
        password = os.environ.get('SMS_PASS', '')
    return (username, password)


def number(phone_number):
    """Store your SMS number as an environment variable."""
    if isinstance(phone_number, int):
        phone_number = str(phone_number)
    phone_number = phone_number.replace('-', '')
    os.environ['SMSIFIED_NUMBER'] = phone_number


def receive(data):
    """Process an incoming text message."""
    data = json.loads(data)
    text = data['inboundSMSMessageNotification']['inboundSMSMessage']
    return text


def send(to, message, **params):
    """Send an SMS message."""
    authentication = auth()
    number = os.environ.get('SMSIFIED_NUMBER', '')
    if 'callback' in params:
        callback = params.pop('callback')
        params['notifyURL'] = callback
    params['address'] = to
    params['message'] = message
    endpoint = '/'.join((URL, 'outbound', number, 'requests'))
    response = req.post(endpoint, auth=authentication, params=params)
    return response
