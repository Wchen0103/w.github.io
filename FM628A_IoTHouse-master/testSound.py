from machine import Pin
import time
import neopixel

# RGB D5
np = neopixel.NeoPixel(Pin(14),1)

# sound D2
sound=Pin(4,Pin.IN)

while True:
    if sound.value() == 1:
        np[0] = (255, 255 , 255)
    else:
        np[0] = (0,0,0)
    np.write()

