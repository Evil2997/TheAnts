import pyautogui as pg
from ahk import AHK
import time
import numpy as np
import cv2
import pytesseract
import pyscreenshot as scr
import random
from mss import mss
import os
ahk = AHK()
mss = mss()

def find_file_path_Tesseract():
    search_paths = ['C:\\', 'D:\\', 'E:\\']
    for path in search_paths:
        try:
            for root, dirs, files in os.walk(path):
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
scans_eng = []
scans_09slash = []
scans_09 = []
scans_shells = []
scans_09X = []
scans_eng_troops = []
scans_rus_troops = []
delay = 1
a = 50
R = random.randint(50, 100)
pangolin = False
eto = False
gm = False
battle = False
present = False
close = False

shards_check = False



win = ahk.find_window(title='BlueStacks App Player')
for _ in range(10):
    win.move(0, 0)
    time.sleep(0.02)

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

window = win.get_position()
wind = [0, 0, 0, 0]
wind[2] = window[2] - w1 - h1 # X
wind[3] = window[3] - w1 - h1 # Y
def moveTo(X, Y, duration):
    r = random.randint(1, 2)
    X1 = w1 + (X-w1) * (wind[2]/562)
    Y1 = h1 + (Y-h1) * (wind[3]/997)
    pg.moveTo(x=X1, y=Y1, duration=duration)
    time.sleep(0.65536 * r * delay)
def click(X, Y):
    r = random.randint(1, 2)
    X1 = w1 + (X-w1) * (wind[2]/562)
    Y1 = h1 + (Y-h1) * (wind[3]/997)
    pg.click(x=X1, y=Y1)
    time.sleep(0.65536 * r * delay)
def dragTo(X, Y, duration):
    r = random.randint(1, 2)
    X1 = w1 + (X-w1) * (wind[2]/562)
    Y1 = h1 + (Y-h1) * (wind[3]/997)
    pg.dragTo(x=X1, y=Y1, duration=duration)
    time.sleep(0.65536 * r * delay)
def screenshot_eng(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/562))
    y1 = int(h1 + (Y1-h1) * (wind[3]/997))
    x2 = int(w1 + (X2-w1) * (wind[2]/562))
    y2 = int(h1 + (Y2-h1) * (wind[3]/997))
    screen_eng = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan_eng = pytesseract.image_to_string(screen_eng, config=config)
    scans_eng.append(scan_eng)
def screenshot_09slash(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/562))
    y1 = int(h1 + (Y1-h1) * (wind[3]/997))
    x2 = int(w1 + (X2-w1) * (wind[2]/562))
    y2 = int(h1 + (Y2-h1) * (wind[3]/997))
    screen_09slash = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan_09slash = pytesseract.image_to_string(screen_09slash, config=config1)
    scans_09slash.append(scan_09slash)

def screenshot(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    global scan
    scan = pytesseract.image_to_string(screen, config=config)
    scans.append(scan)
def find_file_path_ETO(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('ETO'):
                return os.path.abspath(os.path.join(root))
file_path_ETO = find_file_path_ETO(path)
def Screenshot_ETO(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_ETO)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen

def ETO():
    global eto
    eto = False
    average_ETO = [0, ]
    os.chdir(file_path_ETO)
    for img_ETO in os.listdir():
        if img_ETO.startswith('ETO'):
            if eto == True:
                break
            template_ETO = cv2.imread(img_ETO, 0)
            w_ETO, h_ETO = template_ETO.shape[::-1]
            for _ in range(6):  # 1 минута = 67
                base_screen_ETO = Screenshot_ETO(50, 80, 500, 280)
                cv2.imwrite('TheAntsETO.png', base_screen_ETO)
                img_rgb_ETO = cv2.imread('TheAntsETO.png')
                img_gray_ETO = cv2.cvtColor(img_rgb_ETO, cv2.COLOR_BGR2GRAY)
                res_ETO = cv2.matchTemplate(img_gray_ETO, template_ETO, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
                loc_ETO = np.where(res_ETO >= 0.9)
                try:
                    clean_screen_ETO = scr.grab(bbox=(x_ETO, y_ETO, x_ETO + w_ETO, y_ETO + h_ETO))
                    mean_ETO = np.mean(clean_screen_ETO)
                    diff_ETO = average_ETO[-1] - mean_ETO
                    if diff_ETO >= 4:
                        break
                    average_ETO.append(mean_ETO)
                except:
                    for pt in zip(*loc_ETO[::-1]):
                        x_ETO = int(pt[0])
                        y_ETO = int(pt[1])
                try:
                    click(x_ETO + 85, y_ETO + 115)
                    eto = True
                    break
                except NameError:
                    pass
                try:
                    del(x_ETO)
                    del(y_ETO)
                except:
                    pass
                average_ETO = [0, ]
def find_file_path_Pangolin(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('Pangolin'):
                return os.path.abspath(os.path.join(root))
file_path_Pangolin = find_file_path_Pangolin(path)

def Screenshot_Pangolin(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_Pangolin)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen

def Pangolin():
    global pangolin
    pangolin = False
    average_Pangolin = [0, ]
    os.chdir(file_path_Pangolin)
    for img_Pangolin in os.listdir():
        if img_Pangolin.startswith('Pangolin'):
            template_Pangolin = cv2.imread(img_Pangolin, 0)
            w_Pangolin, h_Pangolin = template_Pangolin.shape[::-1]
            for _ in range(6):  # 1 минута = 67
                base_screen_Pangolin = Screenshot_Pangolin(170, 100, 620, 320)
                cv2.imwrite('TheAntsPangolin.png', base_screen_Pangolin)
                img_rgb_Pangolin = cv2.imread('TheAntsPangolin.png')
                img_gray_Pangolin = cv2.cvtColor(img_rgb_Pangolin, cv2.COLOR_BGR2GRAY)
                res_Pangolin = cv2.matchTemplate(img_gray_Pangolin, template_Pangolin, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
                loc_Pangolin = np.where(res_Pangolin >= 0.9)
                try:
                    clean_screen_Pangolin = Screenshot_Pangolin(x_Pangolin, y_Pangolin, x_Pangolin + w_Pangolin, y_Pangolin + h_Pangolin)
                    mean_Pangolin = np.mean(clean_screen_Pangolin)
                    diff_Pangolin = average_Pangolin[-1] - mean_Pangolin
                    if diff_Pangolin >= 4:
                        break
                    average_Pangolin.append(mean_Pangolin)
                except:
                    for pt in zip(*loc_Pangolin[::-1]):
                        x_Pangolin = int(pt[0])
                        y_Pangolin = int(pt[1])
                        time.sleep(0.2)
                try:
                    click(x_Pangolin + 200, y_Pangolin + 140)
                    pangolin = True
                    break
                except NameError:
                    pass
                try:
                    del (x_Pangolin)
                    del (y_Pangolin)
                except:
                    pass
                average_Pangolin = [0, ]
def find_file_path_GM(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('GM'):
                return os.path.abspath(os.path.join(root))
    return None
file_path_GM = find_file_path_GM(path)
def Screenshot_GM(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_GM)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def find_file_path_Battle(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('Battle'):
                return os.path.abspath(os.path.join(root))
def find_file_path_HandHelp(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('HandHelp'):
                return os.path.abspath(os.path.join(root))
def find_file_path_Present(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('Present'):
                return os.path.abspath(os.path.join(root))
def find_file_path_Web1(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('Web1'):
                return os.path.abspath(os.path.join(root))
def find_file_path_Web2(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('Web2'):
                return os.path.abspath(os.path.join(root))
file_path_Battle = find_file_path_Battle(path)
file_path_HandHelp = find_file_path_HandHelp(path)
file_path_Present = find_file_path_Present(path)
file_path_Web1 = find_file_path_Web1(path)
file_path_Web2 = find_file_path_Web2(path)
def Screenshot_Battle(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_Battle)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_HandHelp(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_HandHelp)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_Present(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_Present)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_Web1(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_Web1)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_Web2(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_Web2)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def HandHelp():
    average_HandHelp = [0, ]
    os.chdir(file_path_HandHelp)
    for img_HandHelp in os.listdir():
        if img_HandHelp.startswith('HandHelp'):
            template_HandHelp = cv2.imread(img_HandHelp, 0)
            w_HandHelp, h_HandHelp = template_HandHelp.shape[::-1]
            for _ in range(6):     # 1 минута = 67
                base_screen_HandHelp = Screenshot_HandHelp(482, 575, 559, 891)
                cv2.imwrite('TheAntsHand.png', base_screen_HandHelp)
                img_rgb_HandHelp = cv2.imread('TheAntsHand.png')
                img_gray_HandHelp = cv2.cvtColor(img_rgb_HandHelp, cv2.COLOR_BGR2GRAY)
                res_HandHelp = cv2.matchTemplate(img_gray_HandHelp, template_HandHelp, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
                loc_HandHelp = np.where(res_HandHelp >= 0.6)
                try:
                    clean_screen_HandHelp = Screenshot_HandHelp(x_HandHelp, y_HandHelp, x_HandHelp + w_HandHelp, y_HandHelp + h_HandHelp)
                    mean_HandHelp = np.mean(clean_screen_HandHelp)
                    diff_HandHelp = average_HandHelp[-1] - mean_HandHelp
                    if diff_HandHelp >= 4:
                        break
                    average_HandHelp.append(mean_HandHelp)
                except:
                    for pt in zip(*loc_HandHelp[::-1]):
                        x_HandHelp = int(pt[0])
                        y_HandHelp = int(pt[1])
                try:
                    click(x_HandHelp + 508, y_HandHelp + 590)
                    break
                except NameError:
                    pass
                try:
                    del(x_HandHelp)
                    del(y_HandHelp)
                except:
                    pass
                average_HandHelp = [0, ]
def Present():
    global present
    present = False
    average_Present = [0, ]
    os.chdir(file_path_Present)
    for img_Present in os.listdir():
        if img_Present.startswith('Present'):
            template_Present = cv2.imread(img_Present, 0)
            w_Present, h_Present = template_Present.shape[::-1]
            for _ in range(6):
                base_screen_Present = Screenshot_Present(482, 575, 559, 891)
                cv2.imwrite('TheAntsPresent.png', base_screen_Present)
                img_rgb_Present = cv2.imread('TheAntsPresent.png')
                img_gray_Present = cv2.cvtColor(img_rgb_Present, cv2.COLOR_BGR2GRAY)
                res_Present = cv2.matchTemplate(img_gray_Present, template_Present, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
                loc_Present = np.where(res_Present >= 0.4)
                try:
                    clean_screen_Present = Screenshot_Present(x_Present, y_Present, x_Present + w_Present, y_Present + h_Present)
                    mean_Present = np.mean(clean_screen_Present)
                    diff_Present = average_Present[-1] - mean_Present
                    if diff_Present >= 4:
                        break
                    average_Present.append(mean_Present)
                except:
                    for pt_Present in zip(*loc_Present[::-1]):
                        x_Present = int(pt_Present[0])
                        y_Present = int(pt_Present[1])
                    try:
                        click(x_Present + 508, y_Present + 590)
                        present = True
                        break
                    except NameError:
                        pass
                try:
                    del (x_Present)
                    del (y_Present)
                except:
                    pass
                average_Present = [0, ]
    if present == True:
        click(296, 987)  # получить все (слева)
        click(296, 987)  # свободный клик
        click(421, 341)  # тык правое окошко подарочков
        for present_collection in range(256):
            pg.click(468, 417)  # кнопка получить
            pg.click(466, 523)  # кнопка получить
            pg.click(464, 631)  # кнопка получить
            time.sleep(delay)
            click(353, 48)  # свободный клик
            if present_collection % 4 == 0:
                screenshot_eng(436, 406, 506, 426)
                text_present = scans_eng[-1]
                index_present = text_present.find('Claim')
                if index_present != 0:
                    break
        click(60, 70)

def Web():
    web1 = False
    average_Web1 = [0, ]
    os.chdir(file_path_Web1)
    for img_Web1 in os.listdir():
        if img_Web1.startswith('Web1'):
            template_Web1 = cv2.imread(img_Web1, 0)
            w_Web1, h_Web1 = template_Web1.shape[::-1]
            for _ in range(6):     # 1 минута = 67
                base_screen_Web1 = Screenshot_Web1(150, 175, 485, 500)
                cv2.imwrite('TheAntsWeb1.png', base_screen_Web1)
                img_rgb_Web1 = cv2.imread('TheAntsWeb1.png')
                img_gray_Web1 = cv2.cvtColor(img_rgb_Web1, cv2.COLOR_BGR2GRAY)
                res_Web1 = cv2.matchTemplate(img_gray_Web1, template_Web1, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
                loc_Web1 = np.where(res_Web1 >= 0.8)
                try:
                    clean_screen_Web1 = Screenshot_Web1(x_Web1, y_Web1, x_Web1 + w_Web1, y_Web1 + h_Web1)
                    mean_Web1 = np.mean(clean_screen_Web1)
                    diff_Web1 = average_Web1[-1] - mean_Web1
                    if diff_Web1 >= 4:
                        break
                    average_Web1.append(mean_Web1)
                except:
                    for pt in zip(*loc_Web1[::-1]):
                        x_Web1 = int(pt[0])
                        y_Web1 = int(pt[1])
                try:
                    click(x_Web1 + 160, y_Web1 + 185)
                    web1 = True
                    break
                except NameError:
                    pass
                try:
                    del(x_Web1)
                    del(y_Web1)
                except:
                    pass
                average_Web1 = [0, ]

    if web1 == True:
        average_Web2 = [0, ]
        os.chdir(file_path_Web2)
        for img_Web2 in os.listdir():
            if img_Web2.startswith('Web2'):
                template_Web2 = cv2.imread(img_Web2, 0)
                w_Web2, h_Web2 = template_Web2.shape[::-1]
                for _ in range(10):  # 1 минута = 67
                    base_screen_Web2 = Screenshot_Web2(15, 209, 544, 911)
                    cv2.imwrite('TheAntsWeb2.png', base_screen_Web2)
                    img_rgb_Web2 = cv2.imread('TheAntsWeb2.png')
                    img_gray_Web2 = cv2.cvtColor(img_rgb_Web2, cv2.COLOR_BGR2GRAY)
                    res_Web2 = cv2.matchTemplate(img_gray_Web2, template_Web2, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
                    loc_Web2 = np.where(res_Web2 >= 0.8)
                    try:
                        clean_screen_Web2 = Screenshot_Web2(x_Web2, y_Web2, x_Web2 + w_Web2, y_Web2 + h_Web2)
                        mean_Web2 = np.mean(clean_screen_Web2)
                        diff_Web2 = average_Web2[-1] - mean_Web2
                        if diff_Web2 >= 4:
                            break
                        average_Web2.append(mean_Web2)
                    except:
                        for pt in zip(*loc_Web2[::-1]):
                            x_Web2 = int(pt[0])
                            y_Web2 = int(pt[1])
                    try:
                        click(x_Web2 + 35, y_Web2 + 229)
                        click(300, 50)   # Свободный клик
                        web1 = True
                    except NameError:
                        pass
                    try:
                        del (x_Web2)
                        del (y_Web2)
                    except:
                        pass
                    average_Web2 = [0, ]
    if web1 == True:
        click(60, 70)
def Battle():
    global battle
    battle = False
    average_Battle = [0, ]
    os.chdir(file_path_Battle)
    for img_Battle in os.listdir():
        if img_Battle.startswith('Battle'):
            template_Battle = cv2.imread(img_Battle, 0)
            w_Battle, h_Battle = template_Battle.shape[::-1]
            for _ in range(6):  # 1 минута = 67
                base_screen_Battle = Screenshot_Battle(482, 575, 559, 891)
                cv2.imwrite('TheAntsBattle.png', base_screen_Battle)
                img_rgb_Battle = cv2.imread('TheAntsBattle.png')
                img_gray_Battle = cv2.cvtColor(img_rgb_Battle, cv2.COLOR_BGR2GRAY)
                res_Battle = cv2.matchTemplate(img_gray_Battle, template_Battle, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
                loc_Battle = np.where(res_Battle >= 0.6)
                try:
                    clean_screen_Battle = Screenshot_Battle(x_Battle, y_Battle, x_Battle + w_Battle, y_Battle + h_Battle)
                    mean_Battle = np.mean(clean_screen_Battle)
                    diff_Battle = average_Battle[-1] - mean_Battle
                    if diff_Battle >= 4:
                        break
                    average_Battle.append(mean_Battle)
                except:
                    for pt in zip(*loc_Battle[::-1]):
                        x_Battle = int(pt[0])
                        y_Battle = int(pt[1])
                        time.sleep(0.2)
                try:
                    pg.moveTo(x_Battle + 508, y_Battle + 590, 0.2)
                    battle = True
                    break
                except NameError:
                    pass
                try:
                    del (x_Battle)
                    del (y_Battle)
                except:
                    pass
                average_Battle = [0, ]
def Workers_eng():
    click(38, 200)
    click(140, 369)
    screenshot_eng(239, 438, 277, 457)
    worker1 = scans_eng[-1]
    screenshot_eng(239, 541, 277, 560)
    worker2 = scans_eng[-1]
    screenshot_eng(239, 644, 277, 665)
    worker3 = scans_eng[-1]
    screenshot_eng(239, 745, 277, 768)
    worker4 = scans_eng[-1]
    index_worker1 = worker1.find("Idle")
    index_worker2 = worker2.find("Idle")
    index_worker3 = worker3.find("Idle")
    index_worker4 = worker4.find("Idle")
    click(490, 231)
    if index_worker1 == 0 or index_worker2 == 0 or index_worker3 == 0 or index_worker4 == 0:
        return True
    else:
        return False
def Mypawnuk():
    global gm
    gm = False
    os.chdir(file_path_GM)
    for img_GM in os.listdir():
        if img_GM.startswith('GM'):
            if gm == True:
                break
            template_GM = cv2.imread(img_GM, 0)
            w_GM, h_GM = template_GM.shape[::-1]
        average_GM = [0, ]
        for _ in range(6):  # 1 минута = 67
            base_screen_GM = Screenshot_GM(0, 400, 100, 530)
            cv2.imwrite('TheAntsGM.png', base_screen_GM)

            img_rgb_GM = cv2.imread('TheAntsGM.png')
            img_gray_GM = cv2.cvtColor(img_rgb_GM, cv2.COLOR_BGR2GRAY)

            res_GM = cv2.matchTemplate(img_gray_GM, template_GM, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
            loc_GM = np.where(res_GM >= 0.9)
            try:
                clean_screen_GM = scr.grab(bbox=(x_GM, y_GM, x_GM + w_GM, y_GM + h_GM))
                mean_GM = np.mean(clean_screen_GM)
                diff_GM = average_GM[-1] - mean_GM
                if diff_GM >= 4:
                    break
                average_GM.append(mean_GM)
            except:
                for pt in zip(*loc_GM[::-1]):
                    x_GM = int(pt[0])
                    y_GM = int(pt[1])
            try:
                moveTo(x_GM + 10, y_GM + 410, 0.2)
                gm = True
                break
            except NameError:
                pass
            try:
                del(x_GM)
                del(y_GM)
            except:
                pass
            average_GM = [0, ]

def screenshot_09(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/562))
    y1 = int(h1 + (Y1-h1) * (wind[3]/997))
    x2 = int(w1 + (X2-w1) * (wind[2]/562))
    y2 = int(h1 + (Y2-h1) * (wind[3]/997))
    screen_09 = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan_09 = pytesseract.image_to_string(screen_09, config=config0)
    scans_09.append(scan_09)
def screenshot_eng_troops(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/562))
    y1 = int(h1 + (Y1-h1) * (wind[3]/997))
    x2 = int(w1 + (X2-w1) * (wind[2]/562))
    y2 = int(h1 + (Y2-h1) * (wind[3]/997))
    screen_eng_troops = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    screen_eng_troops = cv2.cvtColor(screen_eng_troops, cv2.COLOR_BGR2GRAY)
    ret, screen_eng_troops = cv2.threshold(screen_eng_troops, 75, 255, 0)
    scan_eng_troops = pytesseract.image_to_string(screen_eng_troops, config=config)
    scans_eng_troops.append(scan_eng_troops)
def find_file_path_Marmot(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('Marmot'):
                return os.path.abspath(os.path.join(root))
file_path_Marmot = find_file_path_Marmot(path)
def Screenshot_Marmot(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_Marmot)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Marmot():
    global marmot
    average_Marmot = [0, ]
    os.chdir(file_path_Marmot)
    for img_Marmot in os.listdir():
        if img_Marmot.startswith('Marmot'):
            template_Marmot = cv2.imread(img_Marmot, 0)
            w_Marmot, h_Marmot = template_Marmot.shape[::-1]

            for _ in range(6):     # 1 минута = 67
                base_screen_Marmot = Screenshot_Marmot(0, 101, 558, 1027)
                cv2.imwrite('TheAntsMarmot.png', base_screen_Marmot)
                img_rgb_Marmot = cv2.imread('TheAntsMarmot.png')
                img_gray_Marmot = cv2.cvtColor(img_rgb_Marmot, cv2.COLOR_BGR2GRAY)
                res_Marmot = cv2.matchTemplate(img_gray_Marmot, template_Marmot, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
                loc_Marmot = np.where(res_Marmot >= 0.6)
                try:
                    clean_screen_Marmot = Screenshot_Marmot(x_Marmot, y_Marmot, x_Marmot + w_Marmot, y_Marmot + h_Marmot)
                    mean_Marmot = np.mean(clean_screen_Marmot)
                    diff_Marmot = average_Marmot[-1] - mean_Marmot
                    if diff_Marmot >= 4:
                        break
                    average_Marmot.append(mean_Marmot)
                except:
                    for pt in zip(*loc_Marmot[::-1]):
                        x_Marmot = int(pt[0])
                        y_Marmot = int(pt[1])
                try:
                    click(x_Marmot + 10, y_Marmot + 116)
                    marmot = True
                    break
                except NameError:
                    pass
                try:
                    del(x_Marmot)
                    del(y_Marmot)
                except:
                    pass
                average_Marmot = [0, ]
def screenshot_shells(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/562))
    y1 = int(h1 + (Y1-h1) * (wind[3]/997))
    x2 = int(w1 + (X2-w1) * (wind[2]/562))
    y2 = int(h1 + (Y2-h1) * (wind[3]/997))
    screen_shells = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    screen_shells = cv2.cvtColor(screen_shells, cv2.COLOR_BGR2GRAY)
    ret, screen_shells = cv2.threshold(screen_shells, 200, 255, 0)
    scan_shells = pytesseract.image_to_string(screen_shells, config=config0)
    scans_shells.append(scan_shells)
def scr_use_skill():
    screenshot(400, 434, 541, 455)
    use_skill = scans[-1]
    if '0' not in use_skill and use_skill != '':
        click(461, 410)
        click(264, 677)
list_numbers = list(map(int, input("Введите числа через пробел:\n").split()))


island = input('''
Вы на острове?
Да --------- "0"
Нет -------- Все что угодно
''')
if island == '0':
    island = True
else:
    island = False

if 1 in list_numbers:
    print('''
Введите колиество строк (от 1 до 3)
доступных вам во вкладке - Зарплата Альянса
Это награды за Вклад и Посещяемость
''')
    chin_lvl = -1
    while chin_lvl < 1 or chin_lvl > 3:
        try:
            chin_lvl = int(input())
        except ValueError:
            pass
if 6 in list_numbers:
    print('''
Если вводимый вами пласт полностью занят
То через несколько попыток занять этот пласт Макросс автоматически займет 4 пласт
Введите уровень пласта (от 3 до 8)
        ''')
    crystal_caves_lvl = -1
    while crystal_caves_lvl < 3 or crystal_caves_lvl > 8:
        try:
            crystal_caves_lvl = int(input())
        except ValueError:
            pass
if 7 in list_numbers:
    print('''
ПАНГОЛИН (Ср / Чт / Пт)
Рекомендуется подойти поближе, что бы атаки на Панголина происходили как можно быстрее.
Атаки через рейд займут много времени, во время запущенного рейда заходить в муравейник Нельзя!
Это приведет к сбою программы!
    ''')
    fast_attack = input('''
    Атаковать Панголина рейдом или вторжением?
    Рейд ------------------ "0"
    Вторжение -------------  Все что угодно
    ''')
    if fast_attack == '0':
        fast_attack = False
    else:
        fast_attack = True

    shells = input('''
    Открываем сундучки панголина или копите?
    Коплю ----------------- "0"
    Открываем ------------- Все что угодно
    ''')
    if shells == '0':
        shells = False
    else:
        shells = True
if 9 in list_numbers:
    fast_attack_marmot = input('''
Атаковать Сурка рейдом или вторжением?
Рейд -------- " "   (1 Пробел/Space)
Вторжение ---  Все что угодно
''')
    if fast_attack_marmot == " ":
        fast_attack_marmot = False
    else:
        fast_attack_marmot = True

win = ahk.find_window(title='BlueStacks App Player')
win.activate()
win.move(0, 0)
Web()
HandHelp()
Present()
if 1 in list_numbers:
    click(80, 135)
    click(513, 144)
    click(513, 144)
    click(180, 416)
    click(283, 702)
    click(513, 144)
    click(60, 70)
    # ----------------------------------------------
    click(523, 350)
    moveTo(34, 175, 0.1)
    dragTo(550, 169, 1)
    moveTo(34, 175, 0.1)
    dragTo(550, 169, 1)
    click(60, 163)
    moveTo(255, 950, 0.1)
    dragTo(246, 543, 1)
    click(481, 979)
    click(481, 979)

    # Events Temporary Offer - Событие Временное предложение
    ETO()

    moveTo(255, 950, 0.1)
    dragTo(246, 543, 1)
    click(481, 979)
    click(160, 61)

    screenshot(121, 259, 160, 284)
    ETO5 = scans[-1]
    index_ETO5 = ETO5.find("5/80")
    if index_ETO5 == 0:
        click(102, 434)               #Собрать награду за 5 входов
        click(300, 70)               #свободный

    screenshot(121, 263, 160, 284)
    ETO10 = scans[-1]
    index_ETO10 = ETO10.find("10/80")
    if index_ETO10 == 0:
        click(159, 327)          # Собрать награду за 10 входов
        click(300, 70)               #свободный клик
    click(60, 70)
    # ----------------------------------------------
    click(382, 990)
    click(344, 646)
    click(463, 293)
    if chin_lvl == 1: # 1
        click(530, 455)
        click(300, 50)
        click(193, 457)
        click(300, 50)
    elif chin_lvl == 2: # 2
        click(530, 455)
        click(300, 50)
        click(193, 457)
        click(300, 50)
        click(530, 670)
        click(300, 50)
        click(193, 670)
        click(300, 50)
    elif chin_lvl == 3: # 3
        click(530, 455)
        click(300, 50)
        click(193, 457)
        click(300, 50)
        click(530, 670)
        click(300, 50)
        click(193, 670)
        click(300, 50)
        click(530, 885)
        click(300, 50)
        click(193, 885)
        click(300, 50)
    click(283, 293)
    if chin_lvl == 1: # 1
        click(30, 455)
        click(300, 50)
        click(338, 455)
        click(300, 50)
        click(530, 455)
        click(300, 50)
    elif chin_lvl == 2: # 2
        click(30, 455)
        click(300, 50)
        click(338, 455)
        click(300, 50)
        click(530, 455)
        click(300, 50)
        click(37, 673)
        click(300, 50)
        click(335, 670)
        click(300, 50)
        click(524, 671)
        click(300, 50)
    elif chin_lvl == 3: # 3
        click(30, 455)
        click(300, 50)
        click(338, 455)
        click(300, 50)
        click(530, 455)
        click(300, 50)
        click(37, 673)
        click(300, 50)
        click(335, 670)
        click(300, 50)
        click(524, 671)
        click(34, 885)
        click(300, 50)
        click(335, 885)
        click(300, 50)
        click(524, 885)
        click(300, 50)

    click(60, 70)
    click(60, 70)
if 2 in list_numbers:
    Mypawnuk()
    win.activate()
    if gm == True:
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')
    else:
        click(500, 980)
        time.sleep(3)
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')
    moveTo(152, 370, 0.1)
    dragTo(549, 489, 3)
    moveTo(115, 482, 0.1)
    dragTo(541, 448, 3)
    moveTo(145, 346, 0.1)
    dragTo(385, 523, 3)
    click(296, 429)
    click(243, 537)
    time.sleep(3)
    click(284, 681)
    moveTo(270, 112, 0.4)
    dragTo(278, 800, 0.4)

    screenshot_eng(452, 173, 534, 205)
    underground_cave1 = scans_eng[-1]
    if 'Supply' not in underground_cave1:
        click(460, 160)
        click(284, 681)
        click(300, 50)

    screenshot_eng(452, 376, 534, 411)
    underground_cave2 = scans_eng[-1]
    if 'Supply' not in underground_cave2:
        click(460, 360)
        click(284, 681)
        click(300, 50)

    screenshot_eng(452, 579, 534, 612)
    underground_cave3 = scans_eng[-1]
    if 'Supply' not in underground_cave3:
        click(460, 560)
        click(284, 681)
        click(300, 50)

    screenshot_eng(459, 780, 521, 818)
    underground_cave4 = scans_eng[-1]
    if 'Supply' not in underground_cave4:
        click(460, 760)
        click(284, 681)
        click(300, 50)

    moveTo(278, 800, 0.4)
    dragTo(270, 112, 0.4)

    screenshot_eng(460, 343, 521, 380)
    underground_cave5 = scans_eng[-1]
    if 'Supply' not in underground_cave5:
        click(460, 330)
        click(284, 681)
        click(300, 50)

    screenshot_eng(460, 536, 521, 581)
    underground_cave6 = scans_eng[-1]
    if 'Supply' not in underground_cave6:
        click(460, 530)
        click(284, 681)
        click(300, 50)

    screenshot_eng(460, 750, 521, 787)
    underground_cave7 = scans_eng[-1]
    if 'Supply' not in underground_cave7:
        click(460, 730)
        click(284, 681)
        click(300, 50)

    moveTo(270, 112, 0.4)
    dragTo(278, 800, 0.4)

    # Закуп
    click(91, 993)
    click(98, 700)
    click(288, 747)
    click(272, 635)
    click(60, 70)
    click(60, 70)
    click(60, 70)

    HandHelp()
    Present()

    click(485, 613)
if 3 in list_numbers:
    Mypawnuk()
    if gm == True:
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')
    else:
        click(500, 980)
        time.sleep(3)
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')
    moveTo(220, 416, 0.2)
    dragTo(492, 431, 3)

    if Workers_eng() == False:  # Отправили 1
        pass
    else:
        click(389, 426)
        click(415, 538)
        click(276, 685)
        if Workers_eng() == False:  # Отправили 2
            time.sleep(14)
        click(305, 485)
        click(369, 592)
        click(276, 685)
        if Workers_eng() == False:  # Отправили 3
            time.sleep(14)
        click(224, 485)
        click(291, 594)
        click(276, 685)
        if Workers_eng() == False:  # Отправили 4
            time.sleep(14)
        click(265, 426)
        click(337, 529)
        click(276, 685)
        if Workers_eng() == False:  # Отправили 5
            time.sleep(14)
        click(223, 369)
        click(298, 481)
        click(276, 685)
        if Workers_eng() == False:  # Отправили 6
            time.sleep(14)
        click(184, 432)
        click(292, 543)
        click(276, 685)
        if Workers_eng() == False:  # Отправили 7
            time.sleep(14)
        click(176, 490)
        click(293, 609)
        click(276, 685)
        if Workers_eng() == False:  # Отправили 8
            time.sleep(14)
        click(176, 440)
        click(292, 551)
        click(276, 685)

    moveTo(220, 416, 1)
    dragTo(492, 431, 1)

    HandHelp()
    Present()

    click(498, 568)
# Корм
    moveTo(357, 202, 1)
    dragTo(395, 581, 1)

    click(412, 506)
    click(412, 506)
    click(394, 499)
    click(390, 634)
    click(278, 786)

    click(311, 484)
    click(311, 484)
    click(311, 629)
    click(278, 786)

    click(230, 482)
    click(230, 482)
    click(227, 633)
    click(278, 786)

    click(152, 483)
    click(152, 483)
    click(170, 647)
    click(278, 786)

    click(292, 427)
    click(292, 427)
    click(295, 575)
    click(278, 786)

    click(333, 369)
    click(333, 369)
    click(332, 511)
    click(278, 786)

    moveTo(251, 214, 1)
    dragTo(535, 634, 1)
    click(350, 818)

    HandHelp()
    Present()
if 4 in list_numbers:
    click(126, 985)
    click(454, 972)
    time.sleep(1)
    for _ in range(10):
        scr_use_skill()
        moveTo(291, 500, 1)
        dragTo(298, 302, 1)  # опуститься вниз
    for _ in range(3):
        moveTo(221, 334, 0.2)
        dragTo(226, 777, 0.2)  # подняться вверх на максимум
    click(60, 70)
    click(60, 70)
if 5 in list_numbers:
    Mypawnuk()
    if gm == True:
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')
    else:
        click(500, 980)
        time.sleep(3)
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')

    click(290, 524)  # королева
    if island == True:
        click(131, 557)  # повадки
    else:
        click(148, 580)
    click(138, 564)
    screenshot_eng(231, 779, 332, 800)
    habit1 = scans_eng[-1]
    index01 = habit1.find('Current Class')
    if index01 == 0:
        Habit = 'Cultivator'
    else:
        click(291, 452)
        screenshot_eng(231, 779, 332, 800)
        habit2 = scans_eng[-1]
        index02 = habit2.find('Current Class')
        if index02 == 0:
            Habit = 'Raider'
        else:
            click(420, 484)
            screenshot_eng(231, 779, 332, 800)
            habit3 = scans_eng[-1]
            index03 = habit3.find('Current Class')
            if index03 == 0:
                Habit = 'Herder'
    click(262, 136)  # закрыть окно повадок, свободный клик

    # Отправить походный отряд на дерево
    moveTo(168, 709, 1)  # переместиться к зданиям повадок
    dragTo(428, 170, 3)
    click(402, 450)  # Здание повадок
    click(402, 450)
    click(388, 574)
    if Habit == 'Cultivator':
        moveTo(256, 788, 1)
        dragTo(217, 400, 1)
    elif Habit == 'Raider':
        moveTo(256, 788, 1)
        dragTo(217, 400, 1)
        moveTo(255, 861, 1)
        dragTo(295, 154, 1)
    elif Habit == 'Herder':
        moveTo(256, 788, 1)
        dragTo(217, 400, 1)
        moveTo(255, 861, 1)
        dragTo(295, 154, 1)
        moveTo(255, 861, 1)
        dragTo(295, 154, 1)
    screenshot_09slash(402, 412, 444, 433)  # ГРИБЫ / ЯЩЕРИЦА / МЕД
    tree61 = scans_09slash[-1]
    try:
        check_tree61 = int(tree61[1])
    except ValueError:
        pass
    if tree61[2] == '/':
        if check_tree61 <= 9 and check_tree61 >= 0:
            click(395, 458)
            moveTo(236, 708, 1)
            dragTo(271, 292, 1)
            click(233, 680)
            click(425, 993)
    else:
        screenshot_09slash(402, 545, 444, 566)  # МЯСО / БОГОМОЛ / МЯСО
        tree62 = scans_09slash[-1]
        try:
            check_tree62 = int(tree62[1])
        except ValueError:
            pass
        if tree62[2] == '/':
            if check_tree62 <= 9 and check_tree62 >= 0:
                click(395, 594)
                moveTo(236, 708, 1)
                dragTo(271, 292, 1)
                click(233, 680)
                click(425, 993)
        else:
            screenshot_09slash(402, 681, 444, 700)  # ЛИСТЬЯ / СТАФИЛИНИДА / ЛИСТЬЯ
            tree63 = scans_09slash[-1]
            try:
                check_tree63 = int(tree63[1])
            except ValueError:
                pass
            if tree63[2] == '/':
                if check_tree63 <= 9 and check_tree63 >= 0:
                    click(395, 724)
                    moveTo(236, 708, 1)
                    dragTo(271, 292, 1)
                    click(233, 680)
                    click(425, 993)
            else:
                screenshot_09slash(402, 816, 444, 836)  # ГРУНТ / ЖУК-ДРОВОСЕК / ГРУНТ
                tree64 = scans_09slash[-1]
                try:
                    check_tree64 = int(tree64[1])
                except ValueError:
                    pass
                if tree64[2] == '/':
                    if check_tree64 <= 9 and check_tree64 >= 0:
                        click(395, 857)
                        moveTo(236, 708, 1)
                        dragTo(271, 292, 1)
                        click(233, 680)
                        click(425, 993)
                else:
                    screenshot_09slash(402, 950, 444, 969)  # ПЕСОК / ЖУК-СЛОН / ПЕСОК
                    tree65 = scans_09slash[-1]
                    try:
                        check_tree65 = int(tree65[1])
                    except ValueError:
                        pass
                    if tree65[2] == '/':
                        if check_tree65 <= 9 and check_tree65 >= 0:
                            pg.click(395, 993)
                            pg.moveTo(236, 708, 1)
                            pg.dragTo(271, 292, 1)
                            pg.click(233, 680)
                            pg.click(425, 993)
                    else:
                        pg.moveTo(275, 344, 0.2)
                        pg.dragTo(262, 938, 0.2)
                        pg.moveTo(275, 344, 0.2)
                        pg.dragTo(262, 938, 0.2)
                        pg.moveTo(275, 344, 0.2)
                        pg.dragTo(262, 938, 0.2)
                        pg.click(60, 70)
                        close = True
    if close == False:
        click(402, 450)  # Здание повадок
        click(402, 450)
        click(388, 574)  # Районное строительство
        moveTo(275, 344, 0.2)
        dragTo(262, 938, 0.2)
        click(60, 70)
    moveTo(119, 593, 1)
    dragTo(306, 199, 1)
    click(441, 176)
if 6 in list_numbers:
    Mypawnuk()
    if gm == True:
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')
    else:
        click(500, 980)
        time.sleep(3)
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')
    moveTo(152, 370, 1)
    dragTo(549, 489, 3)
    moveTo(115, 482, 1)
    dragTo(541, 448, 3)
    moveTo(145, 346, 1)
    dragTo(385, 523, 3)
    click(408, 375)
    click(384, 482)

    click(468, 982)  # Войти в пещеру
    click(60, 70)  # Назад
    click(178, 630)  # Обновить пещеру
    click(468, 982)  # Войти в пещеру

    screenshot_eng(20, 318, 88, 332)
    revoke = scans_eng[-1]
    index_revoke = revoke.find('Recall')
    if index_revoke == 0:
        screenshot_eng(169, 50, 414, 88)
        crystal_caves = scans_eng[-1]
        click(60, 70)  # Назад
        pg.click(398, 627)  # Отмена
    else:
        screenshot_eng(169, 50, 414, 88)
        crystal_caves = scans_eng[-1]
        index111_crystal_caves = crystal_caves.find('Crystal Mine')
        index112_crystal_caves = crystal_caves.find('Mine Portal')
        index113_crystal_caves = crystal_caves.find('Crystal Mine Level 3')
        index114_crystal_caves = crystal_caves.find('Crystal Mine Level 4')
        index115_crystal_caves = crystal_caves.find('Crystal Mine Level 5')
        index116_crystal_caves = crystal_caves.find('Crystal Mine Level 6')
        index117_crystal_caves = crystal_caves.find('Crystal Mine Level 7')
        index118_crystal_caves = crystal_caves.find('Crystal Mine Level 8')
        if index112_crystal_caves == 0:
            if crystal_caves_lvl == 3:
                click(469, 398)  # 3 пласт
            if crystal_caves_lvl == 4:
                click(468, 516)  # 4 пласт
            if crystal_caves_lvl == 5:
                click(471, 626)  # 5 пласт
            if crystal_caves_lvl == 6:
                click(467, 747)  # 6 пласт
            if crystal_caves_lvl == 7:
                click(479, 861)  # 7 пласт
            if crystal_caves_lvl == 8:
                click(500, 976)  # 8 пласт
        for crystal_caves_attempts in range(R):
            click(518, 782)  # Быстрый захват
            click(78, 620)  # Подтвердить
            click(200, 990)  # Напасть поставленным отрядом
            if crystal_caves_attempts % 5 == 0:
                screenshot_eng(20, 318, 88, 332)
                revoke = scans_eng[-1]
                index_revoke = revoke.find('Recall')
                if index_revoke == 0:
                    break
        time.sleep(0.65536 * delay)
        screenshot_eng(169, 50, 414, 88)
        crystal_caves = scans_eng[-1]
        index115_crystal_caves = crystal_caves.find('Crystal Mine Level 5')
        index116_crystal_caves = crystal_caves.find('Crystal Mine Level 6')
        index117_crystal_caves = crystal_caves.find('Crystal Mine Level 7')
        index118_crystal_caves = crystal_caves.find('Crystal Mine Level 8')
        if index115_crystal_caves == 0 or index116_crystal_caves or index117_crystal_caves or index118_crystal_caves:
            screenshot_eng(20, 318, 88, 332)
            revoke = scans_eng[-1]
            index_revoke = revoke.find('Recall')
            if index_revoke == 0:
                pass
            else:
                click(60, 70)  # Назад
                click(178, 630)  # Обновить пещеру
                click(468, 982)  # Войти в пещеру
                click(468, 516)  # 4 пласт
                click(518, 782)  # Быстрый захват
                click(143, 620)  # Подтвердить
                click(200, 990)  # Напасть поставленным отрядом
        click(60, 70)  # Назад
    click(60, 70)  # Назад

    HandHelp()
    Present()

    click(485, 623)
if 7 in list_numbers: # TheAnts13
    click(385, 996)
    if island == False:
        click(465, 766)  # Для района
    else:
        click(103, 885)  # Для острова

    Pangolin()
    if fast_attack == False:
        if pangolin == False:
            print('Атаки на Панголина недоступны')
        else:
            time.sleep(1)
            ahk.key_down('LCtrl')
            ahk.key_down('LShift')
            ahk.key_press('F10')
            time.sleep(1)
            ahk.key_up('LCtrl')
            ahk.key_up('LShift')
            time.sleep(1)
            screenshot_09(525, 847, 544, 861)  # Просмотр оставшихся попыток на сегодня
            pangolin132 = scans_09[-1]
            time.sleep(1)
            ahk.key_down('LCtrl')
            ahk.key_down('LShift')
            ahk.key_press('F10')
            time.sleep(1)
            ahk.key_up('LCtrl')
            ahk.key_up('LShift')
            time.sleep(1)
            print('Попыток осталось: ', pangolin132)
            if int(pangolin132) > 0:
                click(449, 974)  # Бросить вызов
                time.sleep(4)
                click(279, 459)  # Панголин клик
                click(377, 536)  # Рейд
                click(153, 734)  # Подтвердить
                click(411, 977)  # Напасть
                if island == True:
                    screenshot_eng_troops(39, 298, 227, 312)  # Сохранение имени отправляемого отряда
                    squad_name132 = scans_eng_troops[-1]
                else:
                    screenshot_eng_troops(39, 233, 227, 247)  # Сохранение имени отправляемого отряда
                    squad_name132 = scans_eng_troops[-1]
                while int(pangolin132) > 0:
                    if island == True:
                        screenshot_eng_troops(39, 298, 227, 312)  # Проверка отправленного отряда
                        squad_cheek_name132 = scans_eng_troops[-1]
                    else:
                        screenshot_eng_troops(39, 233, 227, 247)  # Проверка отправленного отряда
                        squad_cheek_name132 = scans_eng_troops[-1]
                    time.sleep(24)
                    if squad_name132 != squad_cheek_name132:
                        click(385, 996)
                        if island == False:
                            click(465, 766)  # Для района
                        else:
                            click(103, 885)  # screenshot_eng_troopsДля острова
                        click(245, 187)  # Открыть Панголин ивент
                        click(449, 974)  # Бросить вызов
                        time.sleep(4)
                        click(279, 459)  # Панголин клик
                        click(373, 510)  # Рейд
                        click(183, 730)  # Подтвердить
                        click(427, 982)  # Напасть
                        pangolin132 = int(pangolin132) - 1
                        print('Попыток осталось: ', pangolin132)
            else:
                print('Попытки закончились')
            click(385, 996)  # Альянс
            if island == False:
                click(465, 766)  # Для района
            else:
                click(103, 885)  # Для острова
            click(245, 187)  # Открыть Панголин ивент
            click(142, 984)  # Награды
            click(204, 117)  # лево
            click(262, 997)  # Получить все
            click(263, 57)  # Свободный клик
            click(356, 118)  # право
            click(262, 997)  # Получить все
            click(263, 57)  # Свободный клик
        # Процесс закрытия

        click(60, 70)
        click(60, 70)
        click(60, 70)
        click(60, 70)

    else:  # fast_attack == True !  : Вторжение (не Рейд)
        if pangolin == False:
            print('Атаки на Панголина недоступны')
        else:
            time.sleep(1)
            ahk.key_down('LCtrl')
            ahk.key_down('LShift')
            ahk.key_press('F10')
            time.sleep(1)
            ahk.key_up('LCtrl')
            ahk.key_up('LShift')
            time.sleep(1)
            screenshot_09(525, 847, 544, 861)  # Просмотр оставшихся попыток на сегодня
            pangolin132 = scans_09[-1]
            time.sleep(1)
            ahk.key_down('LCtrl')
            ahk.key_down('LShift')
            ahk.key_press('F10')
            time.sleep(1)
            ahk.key_up('LCtrl')
            ahk.key_up('LShift')
            time.sleep(1)
            print('Попыток осталось: ', pangolin132)
            if int(pangolin132) > 0:
                click(449, 974)  # Бросить вызов
                time.sleep(4)
                click(279, 459)  # Панголин клик
                click(274, 572)  # Вторжение
                click(427, 982)  # Напасть
                if island == True:
                    screenshot_eng_troops(39, 298, 227, 312)  # Сохранение имени отправляемого отряда
                    squad_name132 = scans_eng_troops[-1]
                else:
                    screenshot_eng_troops(39, 233, 227, 247)  # Сохранение имени отправляемого отряда
                    squad_name132 = scans_eng_troops[-1]
                while int(pangolin132) > 0:
                    if island == True:
                        screenshot_eng_troops(39, 298, 227, 312)  # Проверка отправленного отряда
                        squad_cheek_name132 = scans_eng_troops[-1]
                        print(squad_cheek_name132)
                    else:
                        screenshot_eng_troops(39, 233, 227, 247)  # Проверка отправленного отряда
                        squad_cheek_name132 = scans_eng_troops[-1]
                    time.sleep(4)
                    if squad_name132 != squad_cheek_name132:
                        click(385, 996)  # Aliance
                        if island == False:
                            click(465, 766)  # Для района
                        else:
                            click(103, 885)  # Для острова
                        click(245, 187)  # Открыть Панголин ивент
                        click(449, 974)  # Бросить вызов
                        time.sleep(4)
                        click(279, 459)  # Панголин клик
                        click(282, 542)  # Вторжение
                        click(427, 982)  # Напасть
                        pangolin132 = int(pangolin132) - 1
                        print('Попыток осталось: ', pangolin132)
            else:
                print('Попытки закончились')
                click(385, 996)  # Альянс
                if island == False:
                    click(465, 766)  # Для района
                else:
                    click(103, 885)  # Для острова
                click(245, 187)  # Открыть Панголин ивент
                click(142, 984)  # Награды
                click(204, 117)  # лево
                click(262, 997)  # Получить все
                click(263, 57)  # Свободный клик
                click(356, 118)  # право
                click(262, 997)  # Получить все
                click(263, 57)  # Свободный клик
        # #Процесс закрытия

        click(60, 70)
        click(60, 70)
        click(60, 70)
        click(60, 70)

    # Открытие сундучков Панголина
    if shells == True:
        Mypawnuk()
        if gm == True:
            ahk.key_down('down')
            time.sleep(1)
            ahk.key_up('down')
        else:
            click(500, 980)
            time.sleep(3)
            ahk.key_down('down')
            time.sleep(1)
            ahk.key_up('down')
        moveTo(294, 408, 1)
        dragTo(252, 780, 1)
        click(390, 364)
        click(462, 453)

        screenshot_shells(125, 731, 177, 748)
        shells_number = scans_shells[-1]
        shell_quantity = shells_number[1:]
        shell_quantity = int(shell_quantity) - 1
        shell_quantity_remainder = int(shell_quantity) % 5
        shell_quantity_multiple = int(shell_quantity) // 5
        click(101, 982)  # Галочка "Открыть 1 раз"
        click(107, 725)  # Открыть ракушку
        for _ in range(int(shell_quantity_multiple)):
            click(394, 758)  # x5
            time.sleep(2)
        for _ in range(int(shell_quantity_remainder)):
            click(154, 758)  # x1
            time.sleep(1)
        shells = False
        click(518, 261)
        click(60, 70)
        moveTo(237, 287, 0.1)
        dragTo(558, 609, 3)
        click(342, 782)
if 8 in list_numbers:
    Mypawnuk()
    if gm == True:
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')
    else:
        click(500, 980)
        time.sleep(3)
        ahk.key_down('down')
        time.sleep(1)
        ahk.key_up('down')
    click(39, 191)  # Строители
    click(377, 370)  # Исследователи
    for _ in range(9):
        screenshot_eng(215, 569, 301, 590)  # Сканируем (Получить "Свободен")
        researcher_info151 = scans_eng[-1]
        screenshot_eng(146, 566, 220, 582)  # Сканируем (Занятость "Ищет")
        researcher_info152 = scans_eng[-1]
        index_researcher_info151 = researcher_info151.find('Idle')
        index_researcher_info152 = researcher_info152.find('Exploring')
        if index_researcher_info151 != 0 and index_researcher_info152 != 0:
            click(438, 582)  # Получить награду
            click(60, 70)  # Свободный клик
        elif index_researcher_info151 == 0:
            click(438, 582)  # отправить 1/2
            click(279, 700)  # отправить 2/2
        else:
            click(60, 70)
            break
if 9 in list_numbers:
    click(523, 271)             # События
    moveTo(264, 189, 0.2)
    dragTo(240, 500, 0.2)

    Marmot()
    if marmot == False:
        moveTo(309, 931, 1)
        dragTo(300, 225, 1)
        Marmot()

    screenshot_eng(189, 170, 374, 195)
    marmot_check = scans_eng[-1]
    index_scan = marmot_check.find('Restrain Groundhog')
    if index_scan == 0:
        click(260, 980)
        time.sleep(10)             # Загрузка с листьями

        click(278, 482)
        if island == True:
            click(178, 618)
        else:
            click(200, 555)
        click(408, 214)
        click(437, 359)
        time.sleep(4)

        screenshot_09slash(346, 464, 400, 478)
        marmot = scans_09slash[-1]
        if marmot[1] == '/':
            marmot_attempts = int(marmot[0])
            print('Осталось попыток на сурка:', str(marmot_attempts))
        if marmot[2] == '/':
            marmot_attempts = int(marmot[0]) * 10 + int(marmot[1])
            print('Осталось попыток на сурка:', str(marmot_attempts))

        click(491, 176)              # Закрыть статистику
        if int(marmot[0]) > 0:
            if fast_attack_marmot == True:
                click(278, 493)  # Сурок
                if island == True:
                    click(279, 652)
                else:
                    click(279, 583)  # Вторгаться
                click(440, 985)  # Напасть
            else:
                click(278, 493)  # Сурок
                if island == True:
                    click(383, 617)
                else:
                    click(364, 552)  # Рейд
                click(182, 737)  # Подтвердить
                click(440, 985)  # Напасть
            if island == True:
                screenshot_eng_troops(39, 298, 227, 312)  # Сохранение имени отправляемого отряда
                squad_name14 = scans_eng_troops[-1]
            else:
                screenshot_eng_troops(39, 233, 227, 247)  # Сохранение имени отправляемого отряда
                squad_name14 = scans_eng_troops[-1]
            while int(marmot_attempts) > 0:
                if island == True:
                    screenshot_eng_troops(39, 298, 227, 312)  # Проверка отправленного отряда
                    squad_cheek_name14 = scans_eng_troops[-1]
                else:
                    screenshot_eng_troops(39, 233, 227, 247)  # Проверка отправленного отряда
                    squad_cheek_name14 = scans_eng_troops[-1]
                time.sleep(24)
                if squad_name14 != squad_cheek_name14 and fast_attack_marmot == True:
                    click(523, 271)
                    moveTo(264, 189, 0.1)
                    dragTo(240, 500, 1)

                    Marmot()
                    if marmot == False:
                        moveTo(309, 931, 0.1)
                        dragTo(300, 225, 1)
                        Marmot()

                    click(260, 980)
                    time.sleep(4)
                    click(278, 493)  # Сурок
                    if island == True:
                        click(279, 652)
                    else:
                        click(279, 583)  # Вторгаться
                    click(440, 985)  # Напасть
                    marmot_attempts = int(marmot_attempts) - 1
                    print('Осталось попыток на сурка:', str(marmot_attempts))
                    if marmot_attempts == 0:
                        break
                elif squad_name14 != squad_cheek_name14 and fast_attack_marmot == False:
                    click(523, 271)
                    moveTo(264, 189, 0.1)
                    dragTo(240, 500, 1)

                    Marmot()
                    if marmot == False:
                        moveTo(309, 931, 0.1)
                        dragTo(300, 225, 1)
                        Marmot()

                    click(260, 980)
                    time.sleep(4)
                    click(278, 493)  # Сурок
                    if island == True:
                        click(383, 617)
                    else:
                        click(364, 552)  # Рейд
                    click(182, 737)  # Подтвердить
                    click(440, 985)  # Напасть
                    marmot_attempts = int(marmot_attempts) - 1
                    print('Осталось попыток на сурка:', str(marmot_attempts))
                    if marmot_attempts == 0:
                        break
        if marmot_attempts == 0:
            click(274, 639)
            click(60, 70)
        Mypawnuk()
        if gm == True:
            ahk.key_down('down')
            time.sleep(1)
            ahk.key_up('down')
        else:
            click(500, 980)
            time.sleep(3)
            ahk.key_down('down')
            time.sleep(1)
            ahk.key_up('down')



# 7, 9 Settings
# Works 1, 2, 3, 4, 5, 6, 8, 9
