led = pyb.LED(3)
intensity = 0
while True:
    intensity = (intensity + 1) % 255
    print(intensity)  
    led.intensity(intensity)
    pyb.delay(20)
