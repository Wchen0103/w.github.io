# ●● 注意：
# 1. 請務必依照 https://reurl.cc/yrzQAE 教學更新 MicroPython 至 1.19.1 版 
# 2. 請務必依照 https://reurl.cc/QLyANo 教學上傳 BlynkLib.mpy 與 BlynkTimer.mpy 檔

from machine import Pin
import time, network
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")

while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

# door D4
door=Pin(2,Pin.IN)

while True :
    blynk.run()
    print(door.value())
    if door.value() == 0 :
        print('有人按門鈴')
        blynk.log_event("ring", "有人按門鈴")
    time.sleep(1)