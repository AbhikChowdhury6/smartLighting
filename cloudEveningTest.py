#TODO
#test login
#query device functions for the bulb
#craft queries for brightness and color temp
#test those queries
#integrate those queries into Flask


import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

from secrets import ACCESS_ID, ACCESS_KEY, DEVICE_ID


API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"


# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init OpenAPI and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()



# Call APIs from Tuya
# Get the device information
#response = openapi.get("/v1.0/iot-03/devices/{}".format(DEVICE_ID))

# Get the instruction set of the device
#response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(DEVICE_ID))

# Send commands
commands = {'commands': [{'code': 'switch_led', 'value': True},{'code': 'bright_value_v2', 'value': 10},{'code': 'temp_value_v2', 'value': 10}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)

# Get the status of a single device
response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))




