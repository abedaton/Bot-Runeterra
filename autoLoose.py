from python_imagesearch.imagesearch import imagesearch
import pyautogui
import random
import cv2
import time
import sys
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


keyboard = Controller()

num = 10
if (len(sys.argv) == 2):
    num = sys.argv[1]

pos = imagesearch(r"images/runeterraLogo.png", 0.7)
if pos[0] != -1:
    click_image("images/runeterraLogo.png", pos, "left", times=2)


print("Waiting for the Play Button")
pos2 = imagesearch_loop(r"images/PlayButton.png", 0.5, 0.9)
time.sleep(1)
click_image("images/PlayButton.png", pos2, "left")


pos3 = imagesearch_loop(r"images/VSIANotSelected.png", 0.5, 0.9)
if ((pos3[0] != -1) and (pos3[1] != -1)):
    click_image("images/VSIANotSelected.png", pos3, "left")

time.sleep(0.3)
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










#
