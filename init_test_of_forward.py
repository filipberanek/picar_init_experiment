import picar_4wd as fc
import sys
import tty
import termios
import asyncio
import time


for i in range (90):
    fc.forward(i)
    time.sleep(0.05)
    print(i)
    id i == 90:
        time.sleep(1)
fc.stop()