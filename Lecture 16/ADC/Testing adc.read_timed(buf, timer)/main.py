tim = pyb.Timer(9, freq=10)
buf = bytearray(100)
adc.read_timed(buf, tim)
for val in buf:
	print(val) 
