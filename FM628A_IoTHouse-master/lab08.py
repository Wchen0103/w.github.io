from machine import Pin
import time 
import neopixel
import urandom

# RGB D5
np = neopixel.NeoPixel(Pin(14),1)

while True :
    r=urandom.getrandbits(8)
    g=urandom.getrandbits(8)
    b=urandom.getrandbits(8)
    np[0] = (r,g,b)
    np.write()
    time.sleep( 1)
