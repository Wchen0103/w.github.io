# ●● 注意：
# 1. 請務必依照 https://reurl.cc/yrzQAE 教學更新 MicroPython 至 1.19.1 版 
# 2. 請務必依照 https://reurl.cc/QLyANo 教學上傳 BlynkLib.mpy 與 BlynkTimer.mpy 檔

import time, network, urequests
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

def v1_handler():
    res = urequests.get("AQI 網址")
    j=res.json()
    print(j['data']['city']['name'],j['data']['aqi'])
    blynk.virtual_write(1, j['data']['aqi'])
    res.close()

timer_aqi = BlynkTimer()
timer_aqi.set_interval(5, v1_handler)

while True :
    blynk.run()
    timer_aqi.run()
    