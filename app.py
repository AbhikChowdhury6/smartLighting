from flask import Flask
from flask import request


app = Flask(__name__)

import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

from secrets import ACCESS_ID, ACCESS_KEY, DEVICE_ID

#TODO:
#deploy and test locally
#Deploy on cloud service and test
#do write up and send out
#figure out how to do the git ignore for my keys and the Device 


API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"

#fakeKey = "sal3IXl4ZJ4R8OQNR6AYI52UBdT4ihah"

# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init OpenAPI and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

#


@app.route("/change/")
def change_light():
    brightness = request.args.get('brightness')
    temp = request.args.get('temp')

    # Send commands
    commands = {'commands': [{'code': 'switch_led', 'value': True},{'code': 'bright_value_v2', 'value': int(brightness)},{'code': 'temp_value_v2', 'value': int(temp)}]}
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)

    # Get the status of a single device
    response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))
    return response


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)