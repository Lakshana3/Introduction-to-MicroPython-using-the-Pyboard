from pyb import Accel, Servo
servo = Servo(1)
accel = Accel()
while 1:
  servo.angle(accel.x(), 100) 
  pyb.delay(200)
