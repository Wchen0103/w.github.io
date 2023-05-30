# ●● 注意：
# 1. 請務必依照 https://reurl.cc/yrzQAE 教學更新 MicroPython 至 1.19.1 版 
# 2. 請務必依照 https://reurl.cc/QLyANo 教學上傳 BlynkLib.mpy 與 BlynkTimer.mpy 檔

# import gc
# gc.enable()
# gc.threshold(1000)

from machine import Pin,PWM,ADC
import time, network, dht, urequests, neopixel
import BlynkLib
from BlynkTimer import BlynkTimer
from rtttl import RTTTL

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")

while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

# buzzer D8 
buzzer = PWM(Pin(15))
buzzer.duty(0)

def play_tone(freq, msec):
    if freq > 0:
        buzzer.freq(freq)   # Set frequency
        buzzer.duty(10)# 50% duty cycle
        time.sleep(msec*0.001)  # Play for a number of msec
    buzzer.duty(0)          # Stop playing
    time.sleep(0.05)

# door D4
door=Pin(2,Pin.IN)

# servo D1
servo = PWM(Pin(5), freq=50)
servo.duty(30)

# temp D7
temp = dht.DHT11(Pin(13))

# fan D3 
fan=Pin(0,Pin.OUT)
fan.value(0)

# RGB D5
np = neopixel.NeoPixel(Pin(14),1)

r=0
g=0
b=0

# light A0
light = ADC(0)

# laser D6
laser=Pin(12,Pin.OUT)
laser.value(1)

# sound D2
sound=Pin(4,Pin.IN)

# window D0
window=Pin(16,Pin.IN)

def v0_handler(value):
    print(value[0])
    if value[0]=="0":
        servo.freq(50)
        servo.duty(30)
        print('大門打開')
    else :
        servo.freq(50)
        servo.duty(100)
        print('大門關閉')
        
def timer_handler():
#     gc.collect()
    # 請把 AQI 網址中的 https 改為 http
    res= urequests.get("AQI 網址")
    j=res.json()
    print(j['data']['city']['name'],j['data']['aqi'])
    blynk.virtual_write(1, j['data']['aqi'])
    res.close()
    try:
        temp.measure()
        blynk.virtual_write(2, temp.temperature())
        blynk.virtual_write(3, temp.humidity())
        print('溫度 濕度',temp.temperature(),temp.humidity())
        if temp.humidity()>80:
            fan.value(1)
            print("濕度過高，開啟空調")
        else :
            fan.value(0)
    except :
        print("尚未更新溫濕度")

timer = BlynkTimer()
timer.set_interval(5, timer_handler)

def v4_handler(R_Value):
    global r
    r=int(R_Value[0])
    
def v5_handler(G_Value):
    global g
    g=int(G_Value[0])

def v6_handler(B_Value):
    global b
    b=int(B_Value[0])

music_moon = "Moonheart:d=4,o=5,b=140:c.,8e,g.,8c,b.4,8e,g.,8g,a.,8b,c.6,8a,2g,8e,8d,c.,8c,8c,8p,8e,8d,c.,8c,8c,8p,8d,8e,d.,8a4,b.4,16c,16d,2c"
music_mario = "mario:d=4,o=4,b=100:16e5,16e5,32p,8e5,16c5,8e5,8g5,8p,8g,8p,8c5,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e5,16g5,8a5,16f5,8g5,8e5,16c5,16d5,8b,16p,8c5"

def v7_handler(value):
    print(value[0])
    if value[0]=="60":
        print('play music')
        tune = RTTTL(music_moon)
        for freq, msec in tune.notes():
            play_tone(freq, msec) 
        buzzer.duty(0)
    if value[0]=="100":
        print('play music')
        tune = RTTTL(music_mario)
        for freq, msec in tune.notes():
            play_tone(freq, msec) 
        buzzer.duty(0)
    else:
        buzzer.duty(0)

blynk.on("V0", v0_handler)
blynk.on("V4", v4_handler)
blynk.on("V5", v5_handler)
blynk.on("V6", v6_handler)
blynk.on("V7", v7_handler)

count=0
while True :
    blynk.run()
    timer.run()

    if door.value() == 0 :
        print('有人按門鈴')
        blynk.log_event("ring", "有人按門鈴")
        time.sleep(5)
    
    if light.read() < 100 and laser.value()==1 :
        print("外面有人喔")
        blynk.log_event("someone", "外面有人喔")
        time.sleep(5)
        
    if sound.value()==1 :
        count+=1
    if sound.value()==0 :
        count=0
    if count==5 :
        print('嬰兒房有聲響，快去查看')
        blynk.log_event("sound", "嬰兒房有聲響，快去查看")
        count=0
        
    if window.value() == 1 :
        print('家裡遭小偷，請盡速查看')
        # 請把 IFTTT 網址中的 https 改為 http
        res = urequests.get("IFTTT 網址")
        res.close()
        time.sleep(10)
        
    np[0] = (r,g,b)
    np.write()