import dearpygui.dearpygui as dpg
from ahk import AHK
from mss import mss
import pyautogui as pg
import numpy as np
import cv2
import pytesseract
import time
import random
import os
from PIL import ImageGrab as scr

ahk = AHK()
mss = mss()

def find_file_path_Tesseract():
    search_paths = ['C:\\', 'D:\\', 'E:\\']
    for paths in search_paths:
        try:
            for root, dirs, files in os.walk(paths):
                for file in files:
                    if file.lower() == 'tesseract.exe':
                        return os.path.abspath(os.path.join(root, file))
        except FileNotFoundError:
            continue
    raise FileNotFoundError("Tesseract executable not found on any specified drive.")

def Tesseract():
    try:
        file_path_Tesseract = find_file_path_Tesseract()
        return file_path_Tesseract
    except FileNotFoundError as e:
        return str(e)
    except PermissionError as e:
        return "Permission denied: " + str(e)
    except Exception as e:
        return "An error occurred: " + str(e)


pytesseract.pytesseract.tesseract_cmd = Tesseract()
config = r'--oem 3 --psm 6'
config0 = r'--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789'
config1 = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789/()'
config2 = r'--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789X'


our_color = [35, 38, 66]
path = 'C:'
screens = []
scans = []
scans_rus = []
scans_09slash = []
scans_09 = []
scans_shells = []
scans_09X = []
scans_rus_troops = []
delay = 1
a = 50
R = random.randint(50, 100)
scans_eng_troops = []
scans_eng = []


win = ahk.find_window(title='BlueStacks App Player 11')
for _ in range(65536):
    win.move(0, 0)
    window = win.get_position()
    if window[0] == 0 and window[1] == 0:
        win.activate()
        break
    else:
        time.sleep(0.8)
window = win.get_position()


def find_color(our_color, monitor={}):
    img = mss.grab(monitor)
    img_arr = np.array(img)
    our_map = (our_color[2], our_color[1], our_color[0], 255)
    indexes = np.where(np.all(img_arr == our_map, axis=-1))  # Сканирование пикселя MAP на карте ARR
    our_crd = np.transpose(indexes)  # Координаты нужных Пикселей найденных на карте ARR
    return our_crd


for _ in range(50):
    monitor = {"top": a, "left": 2, "width": 1, "height": 1}
    #           y1        x1        w = x2 - x1  h = y2 - y1
    result = find_color(our_color, monitor)
    if result.__len__():
        w1 = 1
        h1 = result[0][0] + monitor.get('top')
        break
    a = a - 1

wind = [0, 0, 0, 0]
wind[2] = window[2] - w1 - h1  # X
wind[3] = window[3] - w1 - h1  # Y
W = 592     # (-1)
H = 980     # (-40)

def click(X, Y):
    r = random.randint(1, 2)
    X1 = w1 + (X-w1) * (wind[2]/W)
    Y1 = h1 + (Y-h1) * (wind[3]/H)
    pg.click(x=X1, y=Y1)
    time.sleep(0.65536 * r * delay)
def moveTo(X, Y, duration):
    r = random.randint(1, 2)
    X1 = w1 + (X-w1) * (wind[2]/562)
    Y1 = h1 + (Y-h1) * (wind[3]/997)
    pg.moveTo(x=X1, y=Y1, duration=duration)
    time.sleep(0.65536 * r * delay)
def screenshot(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/562))
    y1 = int(h1 + (Y1-h1) * (wind[3]/997))
    x2 = int(w1 + (X2-w1) * (wind[2]/562))
    y2 = int(h1 + (Y2-h1) * (wind[3]/997))
    screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan = pytesseract.image_to_string(screen, config=config1)
    scans.append(scan)

time.sleep(2)
moveTo(513, 144, 1)
moveTo(60, 70, 1)

