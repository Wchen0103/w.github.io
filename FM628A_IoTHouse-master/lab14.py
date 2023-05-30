# ●● 注意：
# 1. 請務必依照 https://reurl.cc/yrzQAE 教學更新 MicroPython 至 1.19.1 版 
# 2. 請務必依照 https://reurl.cc/QLyANo 教學上傳 BlynkLib.mpy 與 BlynkTimer.mpy 檔

from machine import Pin
import time,network
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("黃", "wheein0417")

while not sta_if.isconnected():
    pass
print('wifi connect')

token="1IHHM7vWKiDC9DoJ8bk4LucrCMvQSAVo"
blynk=BlynkLib.Blynk(token)

# sound D2
sound=Pin(4,Pin.IN)

count=0
while True :
    blynk.run()
    if sound.value()==1 :
        count+=1
    if sound.value()==0 :
        count=0
        
    if count==5 :
        print('嬰兒房有聲響，快去查看')
        blynk.log_event("sound", "嬰兒房有聲響，快去查看")
        count=0
            
    print(sound.value(),count)
    time.sleep(.2)

