from pyb import ADC, Pin, Servo
adc = ADC(Pin('X1'))
servo = Servo(2)
while 1:
  if adc.read() < 2840 and adc.read() > 2810:
    servo.angle(-90,1000)
  if adc.read() > 2840 and adc.read() < 2860:
    servo.angle(0,1000)	
  if adc.read() > 2860:
    servo.angle(90,1000)
