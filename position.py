import pyautogui as pg
import time
import pytesseract
import os
import numpy as np
from PIL import ImageGrab as scr
import cv2
print(pg.position())

def troops():
    for _ in range(1000):
        pg.click(390, 977)
        time.sleep(0.6)
        pg.click(390, 977)
        time.sleep(0.6)
        pg.click(480, 206)
        time.sleep(0.6)
        pg.click(161, 717)
        time.sleep(0.6)


def find_file_path_Tesseract():
    search_paths = ['C:\\', 'D:\\', 'E:\\']
    for paths in search_paths:
        try:
            for root, dirs, files in os.walk(paths):
                for file in files:
                    if file.lower() == 'tesseract.exe':
                        return os.path.abspath(os.path.join(root, file))
        except FileNotFoundError:
            pass
def Tesseract():
    try:
        file_path_Tesseract = find_file_path_Tesseract()
        return file_path_Tesseract
    except FileNotFoundError:
        pass
    except PermissionError:
        pass
    except Exception:
        pass

pytesseract.pytesseract.tesseract_cmd = Tesseract()
config = r'--oem 3 --psm 6'
config0 = r'--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789'
config1 = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789/()'
config2 = r'--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789X'

for i in range(14):
    pg.click(60, 70)

#screen = np.array(scr.grab(bbox=(0, 0, 50, 50)))
#scan = pytesseract.image_to_string(screen, config=config)
#print(scan)
#cv2.imwrite('111.png', screen)