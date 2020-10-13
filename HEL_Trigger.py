import time
import os
import board
import digitalio


button1 = digitalio.DigitalInOut(board.D23)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP


while True:

    if not button1.value:
        os.system('omxplayer --aspect-mode stretch /home/pi/HEL.mp4')
    else:
        os.system('omxplayer --aspect-mode stretch /home/pi/Standby.mp4')
        
    time.sleep(.25)
