from machine import Pin,PWM 
import time

buzzer = PWM(Pin(15)) # D8 腳位
buzzer.duty(512)      # 開始發聲

while True :
    buzzer.freq(261)  # 兩
    time.sleep(.5)    # 每一拍半秒鐘
    buzzer.freq(294)  # 隻
    time.sleep(.5)
    buzzer.freq(330)  # 老
    time.sleep(.5)
    buzzer.freq(261)  # 虎
    time.sleep(.5)
    buzzer.freq(261)  # 兩
    time.sleep(.5)    # 每一拍半秒鐘
    buzzer.freq(294)  # 隻
    time.sleep(.5)   
    buzzer.freq(330)  # 老
    time.sleep(.5)   
    buzzer.freq(261)  # 虎
    time.sleep(.5)

    buzzer.freq(330)  # 跑
    time.sleep(.5)    # 每一拍半秒鐘
    buzzer.freq(349)  # 得
    time.sleep(.5)   
    buzzer.freq(392)  # 快
    time.sleep(.5)   

    buzzer.duty(0)    # 停止發聲
    time.sleep(.5)    # 每一拍半秒鐘
    buzzer.duty(512)  # 恢復發聲
    
#     小蜜蜂
#     buzzer.freq(392)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
#  
#     buzzer.freq(330)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
#     
#     buzzer.freq(330)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.7)
#     buzzer.duty(512)
#     
#     buzzer.freq(349)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
#     
#     buzzer.freq(294)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
#     
#     buzzer.freq(294)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.7)
#     buzzer.duty(512)
#     
#     
#     buzzer.freq(261)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
#     
#     buzzer.freq(294)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
#     
#     buzzer.freq(330)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
#     
#     buzzer.freq(349)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
#     
#     buzzer.freq(392)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
#     
#     buzzer.freq(392)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.2)
#     buzzer.duty(512)
# 
#     buzzer.freq(392)
#     time.sleep(.3)
#     buzzer.duty(0)
#     time.sleep(.7)
#     buzzer.duty(512)    