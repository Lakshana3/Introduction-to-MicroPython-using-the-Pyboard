from pyb import Pin, ADC
adc = ADC(Pin('X1')) # LDR
p_out1 = Pin('X2', Pin.OUT_PP) # Relay 
p_in = Pin('X3', Pin.IN, Pin.PULL_DOWN) # PIR
p_out2 = Pin('X4', Pin.OUT_PP) # Buzzer
while 1: 
  if adc.read() < 200:  
    p_out1.low()
  else:
    p_out1.high()
  if p_in.value()  == True:
    p_out2.high()	
    pyb.delay(2000) 
    p_out2.low()
