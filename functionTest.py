import sys
import tinytuya

from secrets import DEVICE_ID, LOCAL_IP, LOCAL_KEY

"""
RGB Bulb Device
"""
d = tinytuya.BulbDevice( DEVICE_ID, LOCAL_IP, LOCAL_KEY)
d.set_version(3.3)  # IMPORTANT to set this regardless of version
data = d.status()

# Show status of first controlled switch on device
print('Dictionary %r' % data)


d.set_white(10,10)



#literally the only thing is to set white :0 