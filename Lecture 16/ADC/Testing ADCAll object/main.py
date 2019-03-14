adcall = pyb.ADCAll(12, 0x70000) # 12 bit resolution, internal channels
temp = adcall.read_core_temp()
val1 = adc.read_channel(0x70000)
val2 = adc.read_core_temp()
val3 = adc.read_core_vbat()
val4 = adc.read_core_vref()
val5 = adc.read_vref()
print(temp, val1, val2, val3, val4, val5) 
