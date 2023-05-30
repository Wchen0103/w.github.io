# ●● 注意：
# 1. 請務必依照 https://reurl.cc/yrzQAE 教學更新 MicroPython 至 1.19.1 版 
# 2. 請務必依照 https://reurl.cc/QLyANo 教學上傳 BlynkLib.mpy 與 BlynkTimer.mpy 檔

from machine import ADC, Pin
import time,network
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("lulu", "01100815")

while not sta_if.isconnected():
    pass
print('wifi connect')

token="1IHHM7vWKiDC9DoJ8bk4LucrCMvQSAVo"
blynk=BlynkLib.Blynk(token)

# light A0
light = ADC(0)

# laser D6
laser=Pin(12,Pin.OUT)
laser.value(1)

while True :
    blynk.run()
    print(light.read(),laser.value()==1)
    if light.read() < 200 and laser.value()==1 :
        print('外面有人喔')
        blynk.log_event("someone", "外面有人喔")
    time.sleep(1)