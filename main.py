import pyautogui
import pydirectinput
import time
import sys

from actions import *
from utility import *
from config import *

def main():
    pyautogui.FAILSAFE = True

    startCountDown()
    pressKey('s', 5)
    teleport()



if __name__ == "__main__":
    main()