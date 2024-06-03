import pyautogui
import time
import sys

from utility import *
from config import *

def checkPokedex():
    time.sleep(.2)
    pressKey('n')
    time.sleep(1 + randomTime() * 3)
    pressKey('n')

def checkTrainer():
    time.sleep(.2)
    pressKey('c')
    time.sleep(1 + randomTime() * 3)
    pressKey('c')

def talkToReceptionist():
    print('Talking to receptionist')
    pressKey('space', 11, 1.1)
    time.sleep(1.4)

def walkToFishingSpot():
    print('Walk to fishing spot')
    holdKey('w', 2.2)
    holdKey('d', 1.4)
    holdKey('w', .4)

def catchFish():
    pressKey('s')
    pressKey('space')
    for i in range(0, 4):
        fledResult = pyautogui.locateOnScreen('poke_img/720_fled_from.png')
        if (fledResult != None):
            print('FLED:', fledResult)
            return 'failed'
    else:
        time.sleep(.5)
        pressKey('space')
        # verify pokemon summary is shown
        time.sleep(13)
        for i in range(3):
            pokeSummaryShown = pyautogui.locateOnScreen('poke_img/720_pokemon_summary_' + str(i) + '.png')
            if (pokeSummaryShown != None):
                print('Pokemon Summary', pokeSummaryShown)
                return 'success'
        return 'failed'

def tryToFish():
    print('Try to catch a fish')
    time.sleep(randomTime())
    pressKey(ROD_KEY)
    time.sleep(2.2)
    for i in range(4):
        noFishHooked = pyautogui.locateOnScreen('poke_img/720_not_even_a_nibble_' + str(i) + '.png')
        fishIsHooked = pyautogui.locateOnScreen('poke_img/720_landed_a_pokemon_' + str(i) + '.png')
        print('hooked', fishIsHooked, noFishHooked)
        if (noFishHooked != None or fishIsHooked != None):
            break
    hooked = False
    if (fishIsHooked != None):
        hooked = True
    elif (noFishHooked == None):
        return 'Failed to identify hook'
    if (hooked):
        print('Fish is hooked!')
        pressKey('space')
        time.sleep(5.9)
        result = catchFish()
        if (result == 'success'):
            time.sleep(randomTime())
            pressKey('esc')
            return result
    else:
        pressKey('space')
        return 'failed'

def simpleFishLoop():
    numFish = 0
    if (len(sys.argv) >= 3):
        numFish = int(sys.argv[2])
    else:
        numFish = 1
    while(numFish > 0):
        result = tryToFish()
        print('Fish result:', result)
        if (result == 'success'):
            numFish -= 1
        if (result == 'Failed to identify hook'):
            return

def kantoFish():
    print('Begin Kanto safari fish!')
    holdKey('w', .4)
    talkToReceptionist()
    walkToFishingSpot()
    numFish = 30
    while(numFish > 0):
        num = randomTime()
        if (num < .08):
            checkPokedex()
        elif (num > .95):
            checkTrainer()
        result = tryToFish()
        print('Fish result:', result)
        if (result == 'success'):
            numFish -= 1
        if (result == 'Failed to identify hook'):
            return
    time.sleep(1)
    pressKey('esc')
    pressKey('space', 3)

def teleport():
    print("Teleporting")
    x,y = pyautogui.locateCenterOnScreen('assets/abra.png')
    pydirectinput.click(x=x, y=y, button='left')
    time.sleep(1)
    xTeleport, yTeleport = pyautogui.locateCenterOnScreen('assets/teleport.png')
    pydirectinput.click(x=xTeleport, y=yTeleport, button='left')