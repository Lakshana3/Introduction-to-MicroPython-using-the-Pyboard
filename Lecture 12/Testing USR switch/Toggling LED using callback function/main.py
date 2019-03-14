sw = pyb.Switch()
sw.callback(lambda:pyb.LED(3).toggle())
