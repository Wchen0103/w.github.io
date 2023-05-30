from machine import Pin,PWM

# servo D1
servo = PWM(Pin(5), freq=50)
servo.duty(30) # 舵機角度設定
