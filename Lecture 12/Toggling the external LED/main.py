led = pyb.Pin(‘X2’, pyb.Pin.OUT_PP)
while True:
  led.high() 
  pyb.delay(1000)
  led.low()
  pyb.delay(1000)
