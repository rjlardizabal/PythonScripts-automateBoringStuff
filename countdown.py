#!usr/bin/python3
# countdown.py - A simple countdown script.

import time, subprocess  

timeLeft = 60
while timeLeft > 0:
    print(timeLeft,end='')
    time.sleep(1)
    timeLeft = timeLeft -1
