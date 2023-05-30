# ●● 注意：
# 1. 請務必依照 https://reurl.cc/yrzQAE 教學更新 MicroPython 至 1.19.1 版 
# 2. 請務必依照 https://reurl.cc/QLyANo 教學上傳 BlynkLib.mpy 與 BlynkTimer.mpy 檔

from machine import Pin
import time, network, urequests

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")
while not sta_if.isconnected():
    pass
print('wifi connect')

# window D0
window=Pin(16,Pin.IN)

while True :
    print(window.value())
    if window.value() == 1 :
        print('家裡遭小偷，請盡速查看')
        res = urequests.get("IFTTT 的 HTTP 請求網址")
        res.close()
        time.sleep(10)
    time.sleep(1)