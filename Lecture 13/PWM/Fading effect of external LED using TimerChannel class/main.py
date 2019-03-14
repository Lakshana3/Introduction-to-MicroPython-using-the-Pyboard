from pyb import Timer
from time import sleep
tim = pyb.Timer(5, freq=100)
tchannel = tim.channel(1, Timer.PWM, pin=pyb.Pin.board.X1, pulse_width=0)
max_width = 200000
min_width = 20000 
wstep = 1500
cur_width = min_width
while True:
    tchannel.pulse_width(cur_width)
    sleep(0.01)
    cur_width += wstep
    if cur_width > max_width:
      cur_width = min_width

