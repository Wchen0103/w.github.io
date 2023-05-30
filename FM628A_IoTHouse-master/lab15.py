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
        buzzer.duty(512)        # 50% 工作週期
        time.sleep(msec*0.001) # 播放 msec 豪秒
    buzzer.duty(0)             # 停止播放
    time.sleep(0.05)

music = "Moonheart:d=4,o=5,b=140:c.,8e,g.,8c,b.4,8e,g.,8g,a.,8b,c.6,8a,2g,8e,8d,c.,8c,8c,8p,8e,8d,c.,8c,8c,8p,8d,8e,d.,8a4,b.4,16c,16d,2c"
# tune = RTTTL("mario:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6")

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
    if value[0]=="60":
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