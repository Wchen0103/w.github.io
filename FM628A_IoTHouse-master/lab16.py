# ●● 注意：
# 1. 請務必依照 https://reurl.cc/yrzQAE 教學更新 MicroPython 至 1.19.1 版 
# 2. 請務必依照 https://reurl.cc/QLyANo 教學上傳 BlynkLib.mpy 與 BlynkTimer.mpy 檔

import network,time
from machine import Pin,PWM
from rtttl import RTTTL
import BlynkLib

buzzer = PWM(Pin(15))
buzzer.duty(0)

def play_tone(freq, msec):
    if freq > 0:
        buzzer.freq(freq)      # 設定頻率
        buzzer.duty(512)       # 50% 工作週期
        time.sleep(msec*0.001) # 播放 msec 豪秒
    buzzer.duty(0)             # 停止播放
    time.sleep(0.05)

music = "mario:d=4,o=4,b=100:16e5,16e5,32p,8e5,16c5,8e5,8g5,8p,8g,8p,8c5,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e5,16g5,8a5,16f5,8g5,8e5,16c5,16d5,8b,16p,8c5"

# Connect to Wi-Fi if not connected
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")

while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

def v7_handler(value):
    print(value[0])
    if value[0]=="100":
        print('play music')
        tune = RTTTL(music)
        for freq, msec in tune.notes():
            play_tone(freq, msec) 
        buzzer.duty(0)
    else:
        buzzer.duty(0)

blynk.on("V7", v7_handler)

while True:
    blynk.run()
