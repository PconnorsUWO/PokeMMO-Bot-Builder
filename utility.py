import pyautogui
import pydirectinput
import time
import random

from config import *

def pressKey(key, times = 1, interval = 1):
    for i in range(0, times):
        pydirectinput.press(key)
        time.sleep(interval)

def moveMouse(x, y):
    pydirectinput.moveTo(x, y)
    time.sleep(DELAY_BETWEEN_COMMANDS)

def moveMouseAndClick(x, y, button):
    pydirectinput.click(x=x, y=y, button=button)
    time.sleep(DELAY_BETWEEN_COMMANDS)

def holdKey(key, seconds=1):
    pydirectinput.keyDown(key)
    time.sleep(seconds)
    pydirectinput.keyUp(key)
    time.sleep(DELAY_BETWEEN_COMMANDS)

# General

def randomTime():
    return random.randrange(5, 100) / 100

def startCountDown():
    # Countdown timer
    print("Starting", end="")
    for i in range(0, START_DELAY):
        print(".", end="")
        time.sleep(1)
    print("Go")