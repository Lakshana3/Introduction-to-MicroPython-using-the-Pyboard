led = pyb.LED(2)
intensity = 0
while True:
    intensity = (intensity + 1) % 255
    print(intensity)   Add the audio for this statement
    led.intensity(intensity)
    pyb.delay(20)
