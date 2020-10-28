from python_imagesearch.imagesearch import imagesearch
import pyautogui
import random
import cv2
import time
from sys import argv
from pynput.keyboard import Key, Controller

def r(num, rand):
    return num + rand * random.random()

def click_image(image, pos, action, times = 1, offset=5):
    img = cv2.imread(image)
    height, width, channel = img.shape
    pyautogui.moveTo(pos[0] + r(width/2, offset), pos[1] + r(height/2, offset))
    if (times > 1):
        for i in range(times):
            pyautogui.click(button=action)
            time.sleep(0.1)
    else:
        pyautogui.click(button=action)

def imagesearch_loop(image, timesample, precision=0.8):
    pos = imagesearch(image, precision)
    while pos[0] == -1:
        time.sleep(timesample)
        pos = imagesearch(image, precision)
    return pos

def start():
    precision = 1
    pos = [-1]
    while pos[0] == -1:
        pos = imagesearch(r"images/runeterraLogo.png", precision)
        precision-=0.1
        if (precision<0.2):
            return 0
    print(pos)
    click_image("images/runeterraLogo.png", pos, "left", times=2)
    print("Waiting for the Play Button")
    pos2 = imagesearch_loop(r"images/PlayButton.png", 0.5, 0.9)
    time.sleep(1)
    click_image("images/PlayButton.png", pos2, "left")
    return 1

def playGame(num=10):
    pos4 = imagesearch_loop(r"images\Deck.png", 0.5, 0.9)
    time.sleep(0.3)
    click_image("images\Deck.png", pos4, "left")
    for i in range(int(num)):

        pos5 = imagesearch_loop(r"images\BigPlayButtonStatus.png", 0.5, 0.9)
        if ((pos5[0] != -1) and (pos5[1] != -1)):
            time.sleep(0.3)
            click_image("images\BigPlayButtonStatus.png", pos5, "left")
        else:
            pos6 = imagesearch_loop(r"images\BigPlayButton.png", 0.5, 0.9)
            time.sleep(0.3)
            click_image("images\BigPlayButton.png", pos6, "left")


        pos7 = imagesearch_loop(r"images\Reroll.png", 0.5, 0.9)

        # APPUYER SUR ESPACE
        time.sleep(0.5)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(0.5)

        pos8 = imagesearch_loop(r"images\Surrender.png", 0.5, 0.9)
        click_image("images\Surrender.png", pos8, "left")
        time.sleep(0.3)

        pos9 = imagesearch_loop(r"images\OK.png", 0.5, 0.9)
        click_image("images\OK.png", pos9, "left")
        time.sleep(0.3)

        pos10 = imagesearch_loop(r"images\Continue.png", 0.5, 0.9)
        click_image("images\Continue.png", pos10, "left")
        time.sleep(0.3)

if __name__=="__main__":
    keyboard = Controller()
    boolIA, boolPVP = False, True
    num = 10
    for i in range(len(argv)):
        if argv[i]=="-IA":
            boolIA = True
        elif argv[i]=="-PVP":
            boolPVP = True
        elif argv[i]=="-n":
            num = argv[i+1]
            i+=1

    if (not start()):
        print("ERROR")
    else:
        if boolIA:
            pos3 = imagesearch_loop(r"images/VSIANotSelected.png", 0.5, 0.9)
            if ((pos3[0] != -1) and (pos3[1] != -1)):
                click_image("images/VSIANotSelected.png", pos3, "left")
                time.sleep(0.3)
                playGame(num)
            pos = imagesearch_loop(r"images/VSIASelected.png", 0.5, 0.5)
            if ((pos3[0] != -1) and (pos3[1] != -1)):
                click_image("images/VSIASelected.png", pos3, "left")
        elif boolPVP:
            pos3 = imagesearch_loop(r"images/PVPNotSelected.png", 0.5, 0.6)
            if ((pos3[0] != -1) and (pos3[1] != -1)):
                 click_image("images/PVPNotSelected.png", pos3, "left")
                 time.sleep(0.3)
                 playGame(num)













#
