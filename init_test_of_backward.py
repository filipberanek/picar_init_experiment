import picar_4wd as fc
import sys
import tty
import termios
import asyncio
import time


for i in range (90):
    fc.backward(i)
    print(f"current_angle {fc.current_angle()}")
    #print(f"get_distance_at {fc.get_distance_at(90)}")
    print(f"scan_step {fc.scan_step()}")
    time.sleep(0.05)
    print(i)
    id i == 90:
        time.sleep(1)
fc.stop()