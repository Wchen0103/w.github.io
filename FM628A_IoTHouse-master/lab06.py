# ●● 注意：
# 1. 請務必依照 https://reurl.cc/yrzQAE 教學更新 MicroPython 至 1.19.1 版 
# 2. 請務必依照 https://reurl.cc/QLyANo 教學上傳 BlynkLib.mpy 與 BlynkTimer.mpy 檔

from machine import Pin
import time, network, urequests
import dht
import BlynkLib
from BlynkTimer import BlynkTimer

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")

while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

# temp D7
temp = dht.DHT11(Pin(13))

def timer_handler():
    res = urequests.get("AQI 網址")
    j=res.json()
    print(j['data']['city']['name'],'空污指數',j['data']['aqi'])
    blynk.virtual_write(1, j['data']['aqi'])
    res.close()
    
    try:
        temp.measure()
        print('溫度 濕度',temp.temperature(),temp.humidity())
        blynk.virtual_write(2, temp.temperature())
        blynk.virtual_write(3, temp.humidity())
    except OSError as e:
        print("尚未更新溫濕度")

timer = BlynkTimer()
timer.set_interval(5, timer_handler)

while True :
    blynk.run()
    timer.run()