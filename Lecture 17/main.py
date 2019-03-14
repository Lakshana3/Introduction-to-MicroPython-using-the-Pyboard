from pyb import Pin
p1 = Pin('X1', Pin.IN, Pin.PULL_DOWN)
p2 = Pin('X2', Pin.IN, Pin.PULL_DOWN) 
p3 = Pin('X3', Pin.IN, Pin.PULL_DOWN)
p4 = Pin('X4', Pin.OUT_PP)
x = 1 
while 1: 
  if p1.value() == True:
    x = x+1
    print(x)	
    pyb.delay(200)
  if p2.value() == True:
		x = x-1
		print(x)
		pyb.delay(200)
  if x ==0:
    x = 1
    print(x) 
  while p3.value() == True:
		p4.high()
		pyb.delay(100)
		p4.low()
		pyb.delay(x*100) 

