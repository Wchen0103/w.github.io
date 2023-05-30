from machine import ADC,SPI,PWM,Pin
import time
import neopixel,dht

# buzzer D8 
buzz = PWM(Pin(15))
buzz.freq(392)
buzz.duty(0)

# door D4
door=Pin(2,Pin.IN)

# window D0
window=Pin(16,Pin.IN)

# servo D1
servo = PWM(Pin(5), freq=50)
duty_cycle = 0

# temp D7
temp= dht.DHT11(Pin(13))

# fan D3 
fan=Pin(0,Pin.OUT)

# RGB D5
np = neopixel.NeoPixel(Pin(14),1)

# light A0
light = ADC(0)

# laser D6
laser=Pin(12,Pin.OUT)

# sound D2
sound=Pin(4,Pin.IN)

while True:
    try:
        temp.measure()
    except OSError as e:
        print("can't get temp")
    print("光感測:"+str(light.read())+" 溫度:"+str(temp.temperature())+" 濕度:"+str(temp.humidity()))
    print("按鈕:"+str(door.value())+" 磁簧:"+str(window.value())+" 聲音:"+str(sound.value()) )
    print('--------')

    fan.value(1)
    laser.value(1)
    np[0] = (10,10,10)
    np.write()
    buzz.freq(392)
    buzz.duty(500)
    time.sleep(.5)
    
    try:
        temp.measure()
    except OSError as e:
        print("can't get temp")
    print("光感測:"+str(light.read())+" 溫度:"+str(temp.temperature())+" 濕度:"+str(temp.humidity()))
    print("按鈕:"+str(door.value())+" 磁簧:"+str(window.value())+" 聲音:"+str(sound.value()) )
    print('--------')
    
    fan.value(0)
    laser.value(0)
    servo.duty(30)
    np[0] = (0,0,0)
    np.write()
    buzz.duty(0)
    servo.freq(50)
    servo.duty(30 + duty_cycle)
    duty_cycle = 60 - duty_cycle
    time.sleep(.5)
    