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

button_font = 'fonts/Boomboom.otf'
all_font = 'fonts/Charteritcblack.otf'

TheAnts1 = 'Collecting shops - VIP, free, and Alliance login rewards'
TheAnts2 = 'Collecting cells and purchasing the first slot in the shop.'
TheAnts3 = 'Feeders for wild creatures and leafcutter ants.'
TheAnts4 = 'Ant skills for development.'
TheAnts5 = 'Send a squad to the World Tree.'
TheAnts6 = 'Crystal Cave'
TheAnts7 = 'Pangolin Attack'
TheAnts8 = 'Gather and send Explorers'
TheAnts9 = 'Suricate Attack'

TheAnts1_rus = 'Собрать магазины - VIP, бесплатный, ЗП Альянса'
TheAnts2_rus = 'Сбор клетки, закуп клетки'
TheAnts3_rus = 'Кормушки и листорезы'
TheAnts4_rus = 'Навыки мурашей на ресурсы'
TheAnts5_rus = 'Отправить отряд на Мировое древо'
TheAnts6_rus = 'Кристальная пещера'
TheAnts7_rus = 'Панголин'
TheAnts8_rus = 'Отправка исследователей'
TheAnts9_rus = 'Сурок'

first_rule_eng = '''
    Squad names and in-game prompts should correspond to the language selected in the macro.

    Make sure that keyboard input is enabled in BlueStacks settings.
You can enable it using the keyboard shortcut Ctrl+Shift+F10.
If this doesn't work, go to settings and enable it manually.
If the keyboard is enabled, you will see the names of some keys on your screen.

    Your BlueStacks window is named "BlueStacks App Player."
You can find this out by looking at the upper left corner.
If you have just installed it, the window will have the necessary name.

    Disable the Simplification Mode Reminder in the game.
Profile -> Settings -> Options -> Simplification Mode Reminder(the button should turn gray).

'''

second_rule_eng = '''
1. Honeydew is sufficient for feeding wild creatures.
2. There are enough leaves on the wall to replenish the leafcutter ants.
3. If your squads are out gathering, send them home and wait for their return.
4. Also, it is recommended to create a separate group for macro squads.
5. If the Macro didn't complete its task and closed, simply run it again.
6. If an error occurs in the console, restart the macro.

'''

first_rule_rus = '''
    Имена отрядов и игровые подсказки должны соответствовать языку выбранному в макросе .

    Убедитесь что в настройках BlueStacks включен ввод с клавиатуры.
Его можно включить сочетанием клавиш Ctrl+Shift+F10.
Если ничего не получилось, зайдите в настройки и включите их вручную.
Если клавиатура включена, то у вас на экране будут видны названия некоторых клавиш.

    Ваше окно BlueStacks называется "BlueStacks App Player"
Это можно узнать посмотрев в верхний левый угол.
Если вы его только что установили, то окно имеет нужно название.

    Отключите Напомимение о Режиме Упрощения в игре.
Профиль -> Настройки -> Опции -> Напомимение о Режиме Упрощения (кнопка должна стать серой).
'''

second_rule_rus = '''
1. Медовой росы достаточно на Корм для диких существ.
2. Листьев на стенке хватает для пополнения муравьев листорезов.
3. Если ваши отряды на сборах то отправьте их домой и дождитесь возврата.
4. Так же для отрядов макроса рекомендуется сделать отдельную группу.
5. Если Макрос не закончил работу и закрылся, то просто запустите еще раз.
6. Если возникла ошибка в консоли, перезапустите макрос

'''

checkbox_count = 10
checkbox_states = [False] * checkbox_count
selected_checkboxes = []

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
W = 592
H = 980


def screenshot_eng_troops(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/W))
    y1 = int(h1 + (Y1-h1) * (wind[3]/H))
    x2 = int(w1 + (X2-w1) * (wind[2]/W))
    y2 = int(h1 + (Y2-h1) * (wind[3]/H))
    screen_eng_troops = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    screen_eng_troops = cv2.cvtColor(screen_eng_troops, cv2.COLOR_BGR2GRAY)
    ret, screen_eng_troops = cv2.threshold(screen_eng_troops, 75, 255, 0)
    scan_eng_troops = pytesseract.image_to_string(screen_eng_troops, config=config)
    scans_eng_troops.append(scan_eng_troops)
def moveTo(X, Y, duration):
    r = random.randint(1, 2)
    X1 = w1 + (X-w1) * (wind[2]/W)
    Y1 = h1 + (Y-h1) * (wind[3]/H)
    pg.moveTo(x=X1, y=Y1, duration=duration)
    time.sleep(0.65536 * r * delay)
def click(X, Y):
    r = random.randint(1, 2)
    X1 = w1 + (X-w1) * (wind[2]/W)
    Y1 = h1 + (Y-h1) * (wind[3]/H)
    pg.click(x=X1, y=Y1)
    time.sleep(0.65536 * r * delay)
def dragTo(X, Y, duration):
    r = random.randint(1, 2)
    X1 = w1 + (X-w1) * (wind[2]/W)
    Y1 = h1 + (Y-h1) * (wind[3]/H)
    pg.dragTo(x=X1, y=Y1, duration=duration)
    time.sleep(0.65536 * r * delay)
def screenshot(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/W))
    y1 = int(h1 + (Y1-h1) * (wind[3]/H))
    x2 = int(w1 + (X2-w1) * (wind[2]/W))
    y2 = int(h1 + (Y2-h1) * (wind[3]/H))
    screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan = pytesseract.image_to_string(screen, config=config1)
    scans.append(scan)
def screenshot_rus(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/W))
    y1 = int(h1 + (Y1-h1) * (wind[3]/H))
    x2 = int(w1 + (X2-w1) * (wind[2]/W))
    y2 = int(h1 + (Y2-h1) * (wind[3]/H))
    screen_rus = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan_rus = pytesseract.image_to_string(screen_rus, config=config, lang='rus')
    scans_rus.append(scan_rus)
    screens.append(screen_rus)
def screenshot_09(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    screen_09 = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan_09 = pytesseract.image_to_string(screen_09, config=config0)
    scans_09.append(scan_09)
def screenshot_09slash(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/W))
    y1 = int(h1 + (Y1-h1) * (wind[3]/H))
    x2 = int(w1 + (X2-w1) * (wind[2]/W))
    y2 = int(h1 + (Y2-h1) * (wind[3]/H))
    screen_09slash = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan_09slash = pytesseract.image_to_string(screen_09slash, config=config1)
    scans_09slash.append(scan_09slash)
def screenshot_09X(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/W))
    y1 = int(h1 + (Y1-h1) * (wind[3]/H))
    x2 = int(w1 + (X2-w1) * (wind[2]/W))
    y2 = int(h1 + (Y2-h1) * (wind[3]/H))
    screen_09X = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan_09X = pytesseract.image_to_string(screen_09X, config=config2)
    scans_09X.append(scan_09X)
def screenshot_shells(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    screen_shells = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    screen_shells = cv2.cvtColor(screen_shells, cv2.COLOR_BGR2GRAY)
    ret, screen_shells = cv2.threshold(screen_shells, 200, 255, 0)
    scan_shells = pytesseract.image_to_string(screen_shells, config=config2)
    scans_shells.append(scan_shells)
def screenshot_rus_troops(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/W))
    y1 = int(h1 + (Y1-h1) * (wind[3]/H))
    x2 = int(w1 + (X2-w1) * (wind[2]/W))
    y2 = int(h1 + (Y2-h1) * (wind[3]/H))
    screen_rus_troops = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    screen_rus_troops = cv2.cvtColor(screen_rus_troops, cv2.COLOR_BGR2GRAY)
    ret, screen_rus_troops = cv2.threshold(screen_rus_troops, 75, 255, 0)
    scan_rus_troops = pytesseract.image_to_string(screen_rus_troops, config=config, lang='rus')
    scans_rus_troops.append(scan_rus_troops)
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
def find_file_path_GM(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('GM'):
                return os.path.abspath(os.path.join(root))
def find_file_path_Pangolin(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('Pangolin'):
                return os.path.abspath(os.path.join(root))
def find_file_path_ETO(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('ETO'):
                return os.path.abspath(os.path.join(root))
file_path_Battle = find_file_path_Battle(path)
file_path_HandHelp = find_file_path_HandHelp(path)
file_path_Present = find_file_path_Present(path)
file_path_Web1 = find_file_path_Web1(path)
file_path_Web2 = find_file_path_Web2(path)
file_path_GM = find_file_path_GM(path)
file_path_Pangolin = find_file_path_Pangolin(path)
file_path_ETO = find_file_path_ETO(path)
def find_file_path_Marmot(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('Marmot'):
                return os.path.abspath(os.path.join(root))
file_path_Marmot = find_file_path_Marmot(path)
def Screenshot_Marmot(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
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

def Screenshot_Battle(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    os.chdir(file_path_Battle)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_HandHelp(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    os.chdir(file_path_HandHelp)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_Present(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    os.chdir(file_path_Present)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_Web1(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    os.chdir(file_path_Web1)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_Web2(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    os.chdir(file_path_Web2)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_GM(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    os.chdir(file_path_GM)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_Pangolin(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    os.chdir(file_path_Pangolin)
    base_screen = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    return base_screen
def Screenshot_ETO(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / W))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / H))
    x2 = int(w1 + (X2 - w1) * (wind[2] / W))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / H))
    os.chdir(file_path_ETO)
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
        for present_collection in range(10):
            pg.click(468, 417)  # кнопка получить
            pg.click(466, 523)  # кнопка получить
            pg.click(464, 631)  # кнопка получить
            time.sleep(0.4)
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
def Mypawnuk():
    global gm
    gm = False
    average_GM = [0, ]
    os.chdir(file_path_GM)
    for img_GM in os.listdir():
        if img_GM.startswith('GM'):
            if gm == True:
                break
            template_GM = cv2.imread(img_GM, 0)
            w_GM, h_GM = template_GM.shape[::-1]
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
def Workers_rus():
    click(38, 200)
    click(140, 369)
    screenshot_rus(218, 438, 302, 457)
    worker1 = scans_rus[-1]
    screenshot_rus(218, 541, 302, 560)
    worker2 = scans_rus[-1]
    screenshot_rus(218, 644, 302, 665)
    worker3 = scans_rus[-1]
    screenshot_rus(218, 745, 302, 768)
    worker4 = scans_rus[-1]
    index_worker1 = worker1.find("Свободен")
    index_worker2 = worker2.find("Свободен")
    index_worker3 = worker3.find("Свободен")
    index_worker4 = worker4.find("Свободен")
    click(490, 231)
    if index_worker1 == 0 or index_worker2 == 0 or index_worker3 == 0 or index_worker4 == 0:
        return True
    else:
        return False
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
def scr_use_skill_rus():
    screenshot_rus(390, 434, 550, 460)
    use_skill = scans_rus[-1]
    if '0' not in use_skill and use_skill != '':
        click(461, 410)
        click(264, 677)
def scr_use_skill_eng():
    screenshot(400, 434, 541, 455)
    use_skill = scans[-1]
    if '0' not in use_skill and use_skill != '':
        click(461, 410)
        click(264, 677)
def screenshot_eng(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/562))
    y1 = int(h1 + (Y1-h1) * (wind[3]/997))
    x2 = int(w1 + (X2-w1) * (wind[2]/562))
    y2 = int(h1 + (Y2-h1) * (wind[3]/997))
    screen_eng = np.array(scr.grab(bbox=(x1, y1, x2, y2)))
    scan_eng = pytesseract.image_to_string(screen_eng, config=config)
    scans_eng.append(scan_eng)


def checkbox_callback(sender, app_data, user_data):
    global selected_checkboxes
    if user_data not in selected_checkboxes:
        selected_checkboxes.append(user_data)
    else:
        selected_checkboxes.remove(user_data)
    checkbox_states[user_data] = app_data


'''
def update_visibility():
    for i in range(3):
        group_items = dpg.get_item_children(f"Row{i}")
        for item in group_items:
            item_user_data = dpg.get_item_user_data(item)
            if item_user_data in selected_checkboxes:
                dpg.configure_item(item, show=True)
            else:
                dpg.configure_item(item, show=False)
'''

window_width = 1000
window_height = 800

chin_lvl = 2
crystal_caves_lvl = 8
fast_attack_pangolin = False
shells = False
island = False
def select_chin_lvl_ru(sender, app_data):
    global chin_lvl
    if app_data == chin1_ru:
        chin_lvl = 1
    elif app_data == chin2_ru:
        chin_lvl = 2
    elif app_data == chin3_ru:
        chin_lvl = 3


def select_crystal_caves_lvl_ru(sender, app_data):
    global crystal_caves_lvl
    if app_data == plast3_ru:
        crystal_caves_lvl = 3
    elif app_data == plast4_ru:
        crystal_caves_lvl = 4
    elif app_data == plast5_ru:
        crystal_caves_lvl = 5
    elif app_data == plast6_ru:
        crystal_caves_lvl = 6
    elif app_data == plast7_ru:
        crystal_caves_lvl = 7
    elif app_data == plast8_ru:
        crystal_caves_lvl = 8

def Island_rus(sender, app_data):
    global island
    if app_data == YES:
        island = True
    elif app_data == NO:
        island = False

def Island_eng(sender, app_data):
    global island
    if app_data == Yes:
        island = True
    elif app_data == No:
        island = False

def if_fast_attack_pangolin_ru(sender, app_data):
    global fast_attack_pangolin
    if app_data == fast_True_ru:
        fast_attack_pangolin = True
    elif app_data == fast_False_ru:
        fast_attack_pangolin = False


def if_collect_shells_ru(sender, app_data):
    global shells
    if app_data == YES:
        shells = True
    elif app_data == NO:
        shells = False


chin1_ru = '1 Строка наград'
chin2_ru = '2 Строки наград'
chin3_ru = '3 Строки наград'

plast3_ru = 'Пласт 3'
plast4_ru = 'Пласт 4'
plast5_ru = 'Пласт 5'
plast6_ru = 'Пласт 6'
plast7_ru = 'Пласт 7'
plast8_ru = 'Пласт 8'

fast_False_ru = 'Рейд'
fast_True_ru = 'Вторжение'

YES = 'ДА'
NO = "Нет"


def select_chin_lvl_eng(sender, app_data):
    global chin_lvl
    if app_data == chin1_eng:
        chin_lvl = 1
    elif app_data == chin2_eng:
        chin_lvl = 2
    elif app_data == chin3_eng:
        chin_lvl = 3


def select_crystal_caves_lvl_eng(sender, app_data):
    global crystal_caves_lvl
    if app_data == plast3_eng:
        crystal_caves_lvl = 3
    elif app_data == plast4_eng:
        crystal_caves_lvl = 4
    elif app_data == plast5_eng:
        crystal_caves_lvl = 5
    elif app_data == plast6_eng:
        crystal_caves_lvl = 6
    elif app_data == plast7_eng:
        crystal_caves_lvl = 7
    elif app_data == plast8_eng:
        crystal_caves_lvl = 8


def if_fast_attack_pangolin_eng(sender, app_data):
    global fast_attack_pangolin
    if app_data == fast_True_eng:
        fast_attack_pangolin = True
    elif app_data == fast_False_eng:
        fast_attack_pangolin = False


def if_collect_shells_eng(sender, app_data):
    global shells
    if app_data == Yes:
        shells = True
    elif app_data == No:
        shells = False

chin1_eng = '1 Award String'
chin2_eng = '2 Award String'
chin3_eng = '3 Award String'

plast3_eng = 'Crystal mine 3'
plast4_eng = 'Crystal mine 4'
plast5_eng = 'Crystal mine 5'
plast6_eng = 'Crystal mine 6'
plast7_eng = 'Crystal mine 7'
plast8_eng = 'Crystal mine 8'

fast_False_eng = 'Raid'
fast_True_eng = 'Invasion'

Yes = 'Yes'
No = 'No'

# ======================================================================================================================

def Start_Start_eng():
    # Default Values
    global chin_lvl
    global crystal_caves_lvl
    global island
    global fast_attack_pangolin
    global shells
    global marmot
    fast_attack_marmot = fast_attack = fast_attack_pangolin

    # Программа
    win = ahk.find_window(title='BlueStacks App Player')
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
    Web()
    HandHelp()
    Present()
    if 0 in selected_checkboxes:
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
            click(102, 434)  # Собрать награду за 5 входов
            click(300, 70)  # свободный

        screenshot(121, 263, 160, 284)
        ETO10 = scans[-1]
        index_ETO10 = ETO10.find("10/80")
        if index_ETO10 == 0:
            click(159, 327)  # Собрать награду за 10 входов
            click(300, 70)  # свободный клик
        click(60, 70)
        # ----------------------------------------------
        click(382, 990)
        click(344, 646)
        click(463, 293)
        if chin_lvl == 1:  # 1
            click(530, 455)
            click(300, 50)
            click(193, 457)
            click(300, 50)
        elif chin_lvl == 2:  # 2
            click(530, 455)
            click(300, 50)
            click(193, 457)
            click(300, 50)
            click(530, 670)
            click(300, 50)
            click(193, 670)
            click(300, 50)
        elif chin_lvl == 3:  # 3
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
        if chin_lvl == 1:  # 1
            click(30, 455)
            click(300, 50)
            click(338, 455)
            click(300, 50)
            click(530, 455)
            click(300, 50)
        elif chin_lvl == 2:  # 2
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
        elif chin_lvl == 3:  # 3
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
    if 1 in selected_checkboxes:
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
        click(60, 70)

        HandHelp()
        Present()

        click(485, 613)
    if 2 in selected_checkboxes:
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
    if 3 in selected_checkboxes:
        click(126, 985)
        click(454, 972)
        time.sleep(1)
        for _ in range(10):
            scr_use_skill_eng()
            moveTo(291, 500, 1)
            dragTo(298, 302, 1)  # опуститься вниз
        for _ in range(3):
            moveTo(221, 334, 0.2)
            dragTo(226, 777, 0.2)  # подняться вверх на максимум
        click(60, 70)
        click(60, 70)
    if 4 in selected_checkboxes:
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
                            pg.click(60, 70)
        click(402, 450)  # Здание повадок
        click(402, 450)
        click(388, 574)  # Районное строительство
        moveTo(275, 344, 0.2)
        dragTo(262, 938, 0.2)
        click(60, 70)
        moveTo(119, 593, 1)
        dragTo(306, 199, 1)
        click(441, 176)
    if 5 in selected_checkboxes:
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
    if 6 in selected_checkboxes:
        click(385, 996)
        if island == False:
            click(465, 766)  # Для района
        else:
            click(103, 885)  # Для острова

        Pangolin()
        if fast_attack == False:
            if pangolin == False:
                pass
            else:
                time.sleep(1)
                ahk.key_down('LCtrl')
                ahk.key_down('LShift')
                ahk.key_press('F10')
                time.sleep(1)
                ahk.key_up('LCtrl')
                ahk.key_up('LShift')
                time.sleep(1)
                screenshot_09(530, 845, 552, 863)  # Просмотр оставшихся попыток на сегодня
                pangolin132 = scans_09[-1]
                time.sleep(1)
                ahk.key_down('LCtrl')
                ahk.key_down('LShift')
                ahk.key_press('F10')
                time.sleep(1)
                ahk.key_up('LCtrl')
                ahk.key_up('LShift')
                time.sleep(1)
                if int(pangolin132) > 0:
                    click(449, 974)  # Бросить вызов
                    time.sleep(10)
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
                        time.sleep(65)
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
                else:
                    pass
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
                pass
            else:
                time.sleep(1)
                ahk.key_down('LCtrl')
                ahk.key_down('LShift')
                ahk.key_press('F10')
                time.sleep(1)
                ahk.key_up('LCtrl')
                ahk.key_up('LShift')
                time.sleep(1)
                screenshot_09(530, 845, 552, 863)  # Просмотр оставшихся попыток на сегодня
                pangolin132 = scans_09[-1]
                time.sleep(1)
                ahk.key_down('LCtrl')
                ahk.key_down('LShift')
                ahk.key_press('F10')
                time.sleep(1)
                ahk.key_up('LCtrl')
                ahk.key_up('LShift')
                time.sleep(1)
                if int(pangolin132) > 0:
                    click(449, 974)  # Бросить вызов
                    time.sleep(10)
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
                        else:
                            screenshot_eng_troops(39, 233, 227, 247)  # Проверка отправленного отряда
                            squad_cheek_name132 = scans_eng_troops[-1]
                        time.sleep(12)
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
                else:
                    pass
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
            try:
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
            except ValueError:
                pass
            click(60, 70)
            moveTo(237, 287, 0.1)
            dragTo(558, 609, 3)
            click(342, 782)
    if 7 in selected_checkboxes:
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
    if 8 in selected_checkboxes:
        click(523, 271)  # События
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
            time.sleep(10)  # Загрузка с листьями

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
            if marmot[2] == '/':
                marmot_attempts = int(marmot[0]) * 10 + int(marmot[1])

            click(491, 176)  # Закрыть статистику
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
        click(60, 70)
        click(60, 70)
    dpg.destroy_context()

# ======================================================================================================================

def Start_Start_ru():
    # Default Values
    global chin_lvl
    global crystal_caves_lvl
    global island
    global fast_attack_pangolin
    global shells
    global marmot
    fast_attack_marmot = fast_attack = fast_attack_pangolin

    # Программа
    win = ahk.find_window(title='BlueStacks App Player')
    win.activate()
    Web()
    HandHelp()
    Present()
    if 0 in selected_checkboxes:
        click(80, 135)
        click(513, 144)
        click(513, 144)
        click(180, 416)
        click(283, 702)
        click(513, 144)
        click(60, 70)
        # ----------------------------------------------
        click(523, 350)
        for _ in range(2):
            moveTo(34, 175, 0.1)
            dragTo(550, 169, 1)
        click(60, 163)
        moveTo(255, 950, 0.1)
        dragTo(246, 543, 1)
        click(481, 979)
        click(300, 50)
        click(300, 50)

        # Events Temporary Offer - Событие Временное предложение
        ETO()

        moveTo(255, 950, 0.1)
        dragTo(246, 543, 1)
        click(481, 979)
        click(160, 61)
        click(300, 50)
        click(300, 50)

        screenshot(132, 259, 178, 284)
        ETO5 = scans[-1]
        index_ETO5 = ETO5.find("5/80")
        if index_ETO5 == 0:
            click(102, 434)  # Собрать награду за 5 входов
            click(300, 70)  # свободный

        screenshot(134, 263, 178, 284)
        ETO10 = scans[-1]
        index_ETO10 = ETO10.find("10/80")
        if index_ETO10 == 0:
            click(159, 327)  # Собрать награду за 10 входов
            click(300, 70)  # свободный клик
        click(60, 70)
        # ----------------------------------------------

        click(382, 990)
        time.sleep(1)
        click(344, 646)
        time.sleep(1)
        click(463, 293)
        time.sleep(1)
        if chin_lvl == 1:  # 1
            click(530, 455)
            click(300, 50)
            click(193, 457)
            click(300, 50)
        elif chin_lvl == 2:  # 2
            click(530, 455)
            click(300, 50)
            click(193, 457)
            click(300, 50)
            click(530, 670)
            click(300, 50)
            click(193, 670)
            click(300, 50)
        elif chin_lvl == 3:  # 3
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
        if chin_lvl == 1:  # 1
            click(30, 455)
            click(300, 50)
            click(338, 455)
            click(300, 50)
            click(530, 455)
            click(300, 50)
        elif chin_lvl == 2:  # 2
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
        elif chin_lvl == 3:  # 3
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
    if 1 in selected_checkboxes:
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
        click(296, 429)
        click(243, 537)
        click(284, 681)
        time.sleep(3)
        click(284, 681)
        moveTo(270, 112, 0.4)
        dragTo(278, 800, 0.4)
        screenshot_rus(452, 173, 534, 205)
        underground_cave1 = scans_rus[-1]
        if 'Снабжение' not in underground_cave1:
            click(460, 160)
            click(284, 681)
            click(300, 50)

        screenshot_rus(452, 376, 534, 411)
        underground_cave2 = scans_rus[-1]
        if 'Снабжение' not in underground_cave2:
            click(460, 360)
            click(284, 681)
            click(300, 50)

        screenshot_rus(452, 579, 534, 612)
        underground_cave3 = scans_rus[-1]
        if 'Снабжение' not in underground_cave3:
            click(460, 560)
            click(284, 681)
            click(300, 50)

        screenshot_rus(452, 780, 534, 816)
        underground_cave4 = scans_rus[-1]
        if 'Снабжение' not in underground_cave4:
            click(460, 760)
            click(284, 681)
            click(300, 50)

        moveTo(278, 800, 0.4)
        dragTo(270, 112, 0.4)

        screenshot_rus(454, 344, 534, 360)
        underground_cave5 = scans_rus[-1]
        if 'Снабжение' not in underground_cave5:
            click(460, 330)
            click(284, 681)
            click(300, 50)

        screenshot_rus(452, 545, 534, 581)
        underground_cave6 = scans_rus[-1]
        if 'Снабжение' not in underground_cave6:
            click(460, 530)
            click(284, 681)
            click(300, 50)

        screenshot_rus(452, 747, 534, 783)
        underground_cave7 = scans_rus[-1]
        if 'Снабжение' not in underground_cave7:
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
        click(60, 70)
        click(60, 70)

        HandHelp()
        Present()

        click(485, 613)
    if 2 in selected_checkboxes:
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
        moveTo(220, 416, 1)
        dragTo(492, 431, 3)

        if Workers_rus() == False:  # Отправили 1
            pass
        else:
            click(389, 426)
            click(415, 538)
            click(276, 685)
            if Workers_rus() == False:  # Отправили 2
                time.sleep(16)
            click(305, 485)
            click(369, 592)
            click(276, 685)
            if Workers_rus() == False:  # Отправили 3
                time.sleep(16)
            click(224, 485)
            click(291, 594)
            click(276, 685)
            if Workers_rus() == False:  # Отправили 4
                time.sleep(16)
            click(265, 426)
            click(337, 529)
            click(276, 685)
            if Workers_rus() == False:  # Отправили 5
                time.sleep(16)
            click(223, 369)
            click(298, 481)
            click(276, 685)
            if Workers_rus() == False:  # Отправили 6
                time.sleep(16)
            click(184, 432)
            click(292, 543)
            click(276, 685)
            if Workers_rus() == False:  # Отправили 7
                time.sleep(16)
            click(176, 490)
            click(293, 609)
            click(276, 685)
            if Workers_rus() == False:  # Отправили 8
                time.sleep(16)
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
    if 3 in selected_checkboxes:
        click(126, 985)
        click(454, 972)
        time.sleep(1)
        for _ in range(10):
            scr_use_skill_rus()
            moveTo(291, 500, 1)
            dragTo(298, 302, 1)  # опуститься вниз
        for _ in range(2):
            moveTo(221, 334, 0.2)
            dragTo(226, 777, 0.2)  # подняться вверх на максимум
        click(60, 70)
        click(60, 70)
    if 4 in selected_checkboxes:
        Mypawnuk()
        time.sleep(0.8)
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
        click(290, 524)  # королева

        if island == True:
            click(141, 557)  # повадки
        else:
            click(148, 580)
        click(138, 564)
        screenshot_rus(218, 781, 345, 799)
        habit1 = scans_rus[-1]
        index01 = habit1.find('Текущие Повадки')
        if index01 == 0:
            Habit = 'Cultivator'
        else:
            click(291, 452)
            screenshot_rus(218, 781, 345, 799)
            habit2 = scans_rus[-1]
            index02 = habit2.find('Текущие Повадки')
            if index02 == 0:
                Habit = 'Raider'
            else:
                click(420, 484)
                screenshot_rus(218, 781, 345, 799)
                habit3 = scans_rus[-1]
                index03 = habit3.find('Текущие Повадки')
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
        screenshot_09slash(436, 412, 483, 431)  # ГРИБЫ / ЯЩЕРИЦА / МЕД
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
            screenshot_09slash(436, 545, 483, 564)  # МЯСО / БОГОМОЛ / МЯСО
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
                screenshot_09slash(436, 680, 483, 699)  # ЛИСТЬЯ / СТАФИЛИНИДА / ЛИСТЬЯ
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
                    screenshot_09slash(436, 814, 483, 834)  # ГРУНТ / ЖУК-ДРОВОСЕК / ГРУНТ
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
                        screenshot_09slash(436, 950, 483, 970)  # ПЕСОК / ЖУК-СЛОН / ПЕСОК
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
                            pg.click(60, 70)
        click(402, 450)  # Здание повадок
        click(402, 450)
        click(388, 574)  # Районное строительство
        moveTo(275, 344, 0.2)
        dragTo(262, 938, 0.2)
        click(60, 70)
        moveTo(119, 593, 1)
        dragTo(306, 199, 1)
        click(441, 176)
    if 5 in selected_checkboxes:
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

        screenshot_rus(20, 318, 88, 332)
        revoke = scans_rus[-1]
        index_revoke = revoke.find('Отозвать')
        if index_revoke == 0:
            screenshot_rus(169, 50, 414, 88)
            crystal_caves = scans_rus[-1]
            click(60, 70)  # Назад
            click(398, 627)  # Отмена
            pass
        else:
            screenshot_rus(169, 50, 414, 88)
            crystal_caves = scans_rus[-1]
            index111_crystal_caves = crystal_caves.find('Кристальная Пещера')
            index112_crystal_caves = crystal_caves.find('Телепорт в Пещеру')
            index113_crystal_caves = crystal_caves.find('Пласт под номером 3')
            index114_crystal_caves = crystal_caves.find('Пласт под номером 4')
            index115_crystal_caves = crystal_caves.find('Пласт под номером 5')
            index116_crystal_caves = crystal_caves.find('Пласт под номером 6')
            index117_crystal_caves = crystal_caves.find('Пласт под номером 7')
            index118_crystal_caves = crystal_caves.find('Пласт под номером 8')
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
                    screenshot_rus(20, 318, 88, 332)
                    revoke = scans_rus[-1]
                    index_revoke = revoke.find('Отозвать')
                    if index_revoke == 0:
                        break
            time.sleep(0.65536 * delay)
            screenshot_rus(169, 50, 414, 88)
            crystal_caves = scans_rus[-1]
            index115_crystal_caves = crystal_caves.find('Пласт под номером 5')
            index116_crystal_caves = crystal_caves.find('Пласт под номером 6')
            index117_crystal_caves = crystal_caves.find('Пласт под номером 7')
            index118_crystal_caves = crystal_caves.find('Пласт под номером 8')
            if index115_crystal_caves == 0 or index116_crystal_caves or index117_crystal_caves or index118_crystal_caves:
                screenshot_rus(20, 318, 88, 332)
                revoke = scans_rus[-1]
                index_revoke = revoke.find('Отозвать')
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
            screenshot_rus(169, 50, 414, 88)
            crystal_caves = scans_rus[-1]
            click(60, 70)  # Назад
        click(60, 70)  # Назад

        HandHelp()
        Present()

        click(485, 623)
    if 6 in selected_checkboxes:
        click(385, 996)
        if island == False:
            click(465, 766)  # Для района
        else:
            click(103, 885)  # Для острова

        Pangolin()
        if fast_attack == False:
            if pangolin == False:
                pass
            else:
                time.sleep(1)
                screenshot(460, 845, 481, 863)  # Просмотр оставшихся попыток на сегодня
                pangolin132 = scans[-1]
                if int(pangolin132) > 0:
                    click(449, 974)  # Бросить вызов
                    time.sleep(10)
                    click(279, 459)  # Панголин клик
                    click(377, 536)  # Рейд
                    click(153, 734)  # Подтвердить
                    click(411, 977)  # Напасть
                    if island == True:
                        screenshot_rus_troops(39, 298, 227, 312)  # Сохранение имени отправляемого отряда
                        squad_name132 = scans_rus_troops[-1]
                    else:
                        screenshot_rus_troops(39, 233, 227, 247)  # Сохранение имени отправляемого отряда
                        squad_name132 = scans_rus_troops[-1]
                    while int(pangolin132) > 0:
                        if island == True:
                            screenshot_rus_troops(39, 298, 227, 312)  # Проверка отправленного отряда
                            squad_cheek_name132 = scans_rus_troops[-1]
                        else:
                            screenshot_rus_troops(39, 233, 227, 247)  # Проверка отправленного отряда
                            squad_cheek_name132 = scans_rus_troops[-1]
                        time.sleep(65)
                        if squad_name132 != squad_cheek_name132:
                            click(385, 996)
                            if island == False:
                                click(465, 766)  # Для района
                            else:
                                click(103, 885)  # Для острова
                            click(245, 187)  # Открыть Панголин ивент
                            click(449, 974)  # Бросить вызов
                            time.sleep(7)
                            click(279, 459)  # Панголин клик
                            click(373, 510)  # Рейд
                            click(183, 730)  # Подтвердить
                            click(427, 982)  # Напасть
                            pangolin132 = int(pangolin132) - 1
                click(60, 70)
                click(60, 70)
                click(60, 70)
                click(60, 70)
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
                pass
            else:
                time.sleep(1)
                screenshot(460, 845, 481, 863)  # Просмотр оставшихся попыток на сегодня
                pangolin132 = scans[-1]
                print(pangolin132)
                if int(pangolin132) > 0:
                    click(449, 974)  # Бросить вызов
                    time.sleep(10)
                    click(279, 459)  # Панголин клик
                    click(274, 572)  # Вторжение
                    click(427, 982)  # Напасть
                    if island == True:
                        screenshot_rus_troops(39, 298, 227, 312)  # Сохранение имени отправляемого отряда
                        squad_name132 = scans_rus_troops[-1]
                    else:
                        screenshot_rus_troops(39, 233, 227, 247)  # Сохранение имени отправляемого отряда
                        squad_name132 = scans_rus_troops[-1]
                    while int(pangolin132) > 0:
                        if island == True:
                            screenshot_rus_troops(39, 298, 227, 312)  # Проверка отправленного отряда
                            squad_cheek_name132 = scans_rus_troops[-1]
                        else:
                            screenshot_rus_troops(39, 233, 227, 247)  # Проверка отправленного отряда
                            squad_cheek_name132 = scans_rus_troops[-1]
                        time.sleep(12)
                        if squad_name132 != squad_cheek_name132:
                            click(385, 996)  # Aliance
                            if island == False:
                                click(465, 766)  # Для района
                            else:
                                click(103, 885)  # Для острова
                            click(245, 187)  # Открыть Панголин ивент
                            click(449, 974)  # Бросить вызов
                            time.sleep(7)
                            click(279, 459)  # Панголин клик
                            click(282, 542)  # Вторжение
                            click(427, 982)  # Напасть
                            pangolin132 = int(pangolin132) - 1
                click(60, 70)
                click(60, 70)
                click(60, 70)
                click(60, 70)
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
            moveTo(294, 408, 0.1)
            dragTo(252, 780, 3)
            click(390, 364)
            click(462, 453)
            try:
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
                click(518, 261)
            except ValueError:
                pass
            click(60, 70)
            moveTo(237, 287, 0.1)
            dragTo(558, 609, 3)
            click(342, 782)
    if 7 in selected_checkboxes:
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
            screenshot_rus(215, 569, 301, 590)  # Сканируем (Получить "Свободен")
            researcher_info151 = scans_rus[-1]
            screenshot_rus(146, 566, 190, 582)  # Сканируем (Занятость "Ищет")
            researcher_info152 = scans_rus[-1]
            index_researcher_info151 = researcher_info151.find('Свободен')
            index_researcher_info152 = researcher_info152.find('Ищет')
            if index_researcher_info151 != 0 and index_researcher_info152 != 0:
                click(438, 582)  # Получить награду
                click(60, 70)  # Свободный клик
            elif index_researcher_info151 == 0:
                click(438, 582)  # отправить 1/2
                click(279, 700)  # отправить 2/2
            else:
                click(60, 70)
                print('Исследователи еще не вернулись')
                break
    if 8 in selected_checkboxes:
        click(523, 271)  # События
        moveTo(264, 189, 0.2)
        dragTo(240, 500, 0.2)

        Marmot()
        if marmot == False:
            moveTo(309, 931, 0.1)
            dragTo(300, 225, 1)
            Marmot()
        time.sleep(1)
        screenshot_rus(189, 170, 374, 195)
        marmot_check = scans_rus[-1]
        index_scan = marmot_check.find('Репрессия Сурков')

        if index_scan == 0:
            click(260, 980)
            time.sleep(10)  # Загрузка с листьями

            click(278, 482)
            if island == True:
                click(178, 618)
            else:
                click(200, 555)
            click(408, 214)
            click(437, 359)
            time.sleep(3)

            screenshot_09slash(336, 464, 381, 478)
            marmot = scans_09slash[-1]
            if marmot[1] == '/':
                marmot_attempts = int(marmot[0])
                print('Осталось попыток на сурка:', str(marmot_attempts))
            if marmot[2] == '/':
                marmot_attempts = int(marmot[0]) * 10 + int(marmot[1])
                print('Осталось попыток на сурка:', str(marmot_attempts))

            click(491, 176)  # Закрыть статистику
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
                    screenshot_rus_troops(39, 298, 227, 312)  # Сохранение имени отправляемого отряда
                    squad_name14 = scans_rus_troops[-1]
                else:
                    screenshot_rus_troops(39, 233, 227, 247)  # Сохранение имени отправляемого отряда
                    squad_name14 = scans_rus_troops[-1]
                while int(marmot_attempts) > 0:
                    if island == True:
                        screenshot_rus_troops(39, 298, 227, 312)  # Проверка отправленного отряда
                        squad_cheek_name14 = scans_rus_troops[-1]
                    else:
                        screenshot_rus_troops(39, 233, 227, 247)  # Проверка отправленного отряда
                        squad_cheek_name14 = scans_rus_troops[-1]
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
            elif marmot_attempts == 0:
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
        click(60, 70)
        click(60, 70)
    dpg.destroy_context()

# ======================================================================================================================

dpg.create_context()

dpg.create_viewport(title='Macro TheAnts')
dpg.configure_viewport(0, x_pos=800, y_pos=100, width=window_width, height=window_height)
dpg.set_viewport_max_height(window_height)
dpg.set_viewport_max_width(window_width)

with dpg.font_registry():
    with dpg.font(file=all_font, size=21, default_font=True, tag="Font_Size_25"):
        default_font = dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    with dpg.font(file=all_font, size=55, tag="Font_Size_60"):
        font_size_big = dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    with dpg.font(file=all_font, size=65, tag="Font_Size_72"):
        font_size_biggest = dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    with dpg.font(file=button_font, size=30, tag="Font_Button"):
        font_button = dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

dpg.bind_font("Font_Size_25")

# All defs
# ======================================================================================================================
def open_select_language():
    dpg.configure_item("main_menu_eng", show=False)
    dpg.configure_item("main_menu_rus", show=False)
    dpg.configure_item("rule_window_eng", show=False)
    dpg.configure_item("rule_window_rus", show=False)
    dpg.configure_item("macro_window_eng", show=False)
    dpg.configure_item("macro_window_rus", show=False)
    dpg.configure_item("select_language_window", show=True)
    dpg.configure_item("input_menu_rus", show=False)
    dpg.configure_item("input_menu_eng", show=False)
    dpg.set_primary_window(select_language, value=True)


# English defs
# ======================================================================================================================
def open_rule_panel_eng():
    dpg.configure_item("select_language_window", show=False)
    dpg.configure_item("main_menu_eng", show=False)
    dpg.configure_item("main_menu_rus", show=False)
    dpg.configure_item("rule_window_eng", show=True)
    dpg.configure_item("rule_window_rus", show=False)
    dpg.configure_item("macro_window_eng", show=False)
    dpg.configure_item("macro_window_rus", show=False)
    dpg.configure_item("input_menu_rus", show=False)
    dpg.configure_item("input_menu_eng", show=False)
    dpg.set_primary_window(rule_panel_eng, value=True)


def open_TheAnts_macro_panel_eng():
    dpg.configure_item("select_language_window", show=False)
    dpg.configure_item("main_menu_eng", show=False)
    dpg.configure_item("main_menu_rus", show=False)
    dpg.configure_item("rule_window_eng", show=False)
    dpg.configure_item("rule_window_rus", show=False)
    dpg.configure_item("macro_window_eng", show=True)
    dpg.configure_item("macro_window_rus", show=False)
    dpg.configure_item("input_menu_rus", show=False)
    dpg.configure_item("input_menu_eng", show=False)
    dpg.set_primary_window(TheAnts_macro_window_eng, value=True)


def open_main_menu_eng():
    dpg.configure_item("select_language_window", show=False)
    dpg.configure_item("main_menu_eng", show=True)
    dpg.configure_item("main_menu_rus", show=False)
    dpg.configure_item("rule_window_eng", show=False)
    dpg.configure_item("rule_window_rus", show=False)
    dpg.configure_item("macro_window_eng", show=False)
    dpg.configure_item("macro_window_rus", show=False)
    dpg.configure_item("input_menu_rus", show=False)
    dpg.configure_item("input_menu_eng", show=False)
    dpg.set_primary_window(main_menu_window_eng, value=True)


def open_input_menu_eng():
    dpg.configure_item("select_language_window", show=False)
    dpg.configure_item("main_menu_eng", show=False)
    dpg.configure_item("main_menu_rus", show=False)
    dpg.configure_item("rule_window_eng", show=False)
    dpg.configure_item("rule_window_rus", show=False)
    dpg.configure_item("macro_window_eng", show=False)
    dpg.configure_item("macro_window_rus", show=False)
    dpg.configure_item("input_menu_eng", show=True)
    dpg.configure_item("input_menu_rus", show=False)
    dpg.set_primary_window(input_menu_eng, value=True)


# ======================================================================================================================
# Russian defs
# ======================================================================================================================
def open_rule_panel_rus():
    dpg.configure_item("select_language_window", show=False)
    dpg.configure_item("main_menu_eng", show=False)
    dpg.configure_item("main_menu_rus", show=False)
    dpg.configure_item("rule_window_eng", show=False)
    dpg.configure_item("rule_window_rus", show=True)
    dpg.configure_item("macro_window_eng", show=False)
    dpg.configure_item("macro_window_rus", show=False)
    dpg.configure_item("input_menu_rus", show=False)
    dpg.configure_item("input_menu_eng", show=False)
    dpg.set_primary_window(rule_panel_rus, value=True)


def open_TheAnts_macro_panel_rus():
    dpg.configure_item("select_language_window", show=False)
    dpg.configure_item("main_menu_eng", show=False)
    dpg.configure_item("main_menu_rus", show=False)
    dpg.configure_item("rule_window_eng", show=False)
    dpg.configure_item("rule_window_rus", show=False)
    dpg.configure_item("macro_window_eng", show=False)
    dpg.configure_item("macro_window_rus", show=True)
    dpg.configure_item("input_menu_rus", show=False)
    dpg.configure_item("input_menu_eng", show=False)
    dpg.set_primary_window(TheAnts_macro_window_rus, value=True)


def open_main_menu_rus():
    dpg.configure_item("select_language_window", show=False)
    dpg.configure_item("main_menu_eng", show=False)
    dpg.configure_item("main_menu_rus", show=True)
    dpg.configure_item("rule_window_eng", show=False)
    dpg.configure_item("rule_window_rus", show=False)
    dpg.configure_item("macro_window_eng", show=False)
    dpg.configure_item("macro_window_rus", show=False)
    dpg.configure_item("input_menu_rus", show=False)
    dpg.configure_item("input_menu_eng", show=False)
    dpg.set_primary_window(main_menu_window_rus, value=True)


def open_input_menu_rus():
    dpg.configure_item("select_language_window", show=False)
    dpg.configure_item("main_menu_eng", show=False)
    dpg.configure_item("main_menu_rus", show=False)
    dpg.configure_item("rule_window_eng", show=False)
    dpg.configure_item("rule_window_rus", show=False)
    dpg.configure_item("macro_window_eng", show=False)
    dpg.configure_item("macro_window_rus", show=False)
    dpg.configure_item("input_menu_eng", show=False)
    dpg.configure_item("input_menu_rus", show=True)
    dpg.set_primary_window(input_menu_rus, value=True)


# ======================================================================================================================
# All windows
# ======================================================================================================================
with dpg.window(tag="select_language_window", no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, no_move=True, show=True) as select_language:
    title_eng = dpg.add_text(default_value='Select Language',
                             pos=[window_width // 2 - 200, window_height // 2 - 100])
    dpg.bind_item_font(title_eng, "Font_Size_72")

    with dpg.group(horizontal=True, pos=[window_width // 2 - 150, window_height // 2]):
        button_rus = dpg.add_button(label="Русский", callback=open_main_menu_rus)
        button_eng = dpg.add_button(label="English", callback=open_main_menu_eng)

    dpg.bind_item_font(button_rus, "Font_Button")
    dpg.bind_item_font(button_eng, "Font_Button")

# ======================================================================================================================
# Russian windows
# ======================================================================================================================
with dpg.window(no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, no_move=True, tag="main_menu_rus", show=False) as main_menu_window_rus:
    with dpg.group(horizontal=True, pos=[window_width // 2 - 250, window_height // 2 - 220]):
        title_rus = dpg.add_text(default_value='Макрос для игры TheAnts')

        dpg.bind_item_font(title_rus, "Font_Size_72")

    with dpg.group(horizontal=True, pos=[window_width // 2 - 220, window_height // 2 - 80]):
        rule_btn_rus = dpg.add_button(label="Открыть Документацию", callback=open_rule_panel_rus)
        dpg.bind_item_font(rule_btn_rus, "Font_Button")

    with dpg.group(horizontal=True, pos=[window_width // 2 - 220, window_height // 2 - 120]):
        connect_btn_rus = dpg.add_button(label="Подключиться", callback=open_TheAnts_macro_panel_rus)
        language_btn_rus = dpg.add_button(label="Язык", callback=open_select_language)

        dpg.bind_item_font(connect_btn_rus, "Font_Button")
        dpg.bind_item_font(language_btn_rus, "Font_Button")

# ----------------------------------------------------------------------------------------------------------------------

with dpg.window(label="Rule", no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, tag="rule_window_rus", no_move=True, show=False) as rule_panel_rus:
    rule_title_rus = dpg.add_text(default_value='Правила использования Макроса', pos=[35, 30])

    dpg.add_spacer(width=300, height=72)
    dpg.add_separator()
    dpg.add_spacer(width=300, height=72)

    technical_settings_rus = dpg.add_text(default_value='Технические Настройки')

    text_rus1 = dpg.add_text(default_value=first_rule_rus)
    game_settings_rus = dpg.add_text(default_value='Игровые Настройки')
    text_rus2 = dpg.add_text(default_value=second_rule_rus)

    with dpg.group(horizontal=True):
        btn_connect_rus = dpg.add_button(label="Подключиться", callback=open_TheAnts_macro_panel_rus)
        btn_main_menu_rus = dpg.add_button(label="Назад", callback=open_main_menu_rus)

    dpg.bind_item_font(rule_title_rus, "Font_Size_72")

    dpg.bind_item_font(text_rus1, "Font_Size_25")
    dpg.bind_item_font(text_rus2, "Font_Size_25")

    dpg.bind_item_font(technical_settings_rus, "Font_Size_60")
    dpg.bind_item_font(game_settings_rus, "Font_Size_60")

    dpg.bind_item_font(btn_connect_rus, "Font_Button")
    dpg.bind_item_font(btn_main_menu_rus, "Font_Button")

# ----------------------------------------------------------------------------------------------------------------------
with dpg.window(label="Macro", no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, tag="macro_window_rus", no_move=True, show=False) as TheAnts_macro_window_rus:
    dpg.add_spacer(width=100, height=15)
    dpg.add_separator()
    dpg.add_spacer(width=100, height=15)

    dpg.add_checkbox(label=TheAnts1_rus, callback=checkbox_callback, user_data=0)
    dpg.add_checkbox(label=TheAnts2_rus, callback=checkbox_callback, user_data=1)
    dpg.add_checkbox(label=TheAnts3_rus, callback=checkbox_callback, user_data=2)
    dpg.add_checkbox(label=TheAnts4_rus, callback=checkbox_callback, user_data=3)
    dpg.add_checkbox(label=TheAnts5_rus, callback=checkbox_callback, user_data=4)
    dpg.add_checkbox(label=TheAnts6_rus, callback=checkbox_callback, user_data=5)
    dpg.add_checkbox(label=TheAnts7_rus, callback=checkbox_callback, user_data=6)
    dpg.add_checkbox(label=TheAnts8_rus, callback=checkbox_callback, user_data=7)
    dpg.add_checkbox(label=TheAnts9_rus, callback=checkbox_callback, user_data=8)

    start_btn_rus = dpg.add_button(label="Дальше", callback=open_input_menu_rus)
    btn_main_menu_rus = dpg.add_button(label="Назад", callback=open_main_menu_rus)
    dpg.bind_item_font(btn_main_menu_rus, "Font_Button")
    dpg.add_spacer(width=100, height=15)
    dpg.add_separator()
    dpg.add_spacer(width=100, height=15)

    dpg.bind_item_font(start_btn_rus, "Font_Button")

# ----------------------------------------------------------------------------------------------------------------------
with dpg.window(no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, no_move=True, tag="input_menu_rus", show=False) as input_menu_rus:
    with dpg.group():
        text_island_ru = dpg.add_text(default_value='''
Вы на острове?''')
        radio_btn_island_ru = dpg.add_radio_button((YES, NO), default_value=NO, callback=Island_rus)
        text_chin_ru = dpg.add_text(default_value='''
Сколько у вас доступно строк во вкладке - Зарплата Альянса
Это награды за Вклад и Посищяемость''', label="Row1")
        radio_btn_chin_ru = dpg.add_radio_button((chin1_ru, chin2_ru, chin3_ru), default_value=chin2_ru,
                                                 callback=select_chin_lvl_ru)

    with dpg.group():
        text_crystal_caves_ru = dpg.add_text(default_value='''
Выберите уровень пласта который хотите занять отрядом в кристальной пещере
Через большое колисчество неудачных попыток Макросс автоматически займет 4 Пласт''')
        radio_btn_plast_ru = dpg.add_radio_button((plast3_ru, plast4_ru, plast5_ru, plast6_ru, plast7_ru, plast8_ru),
                                                  default_value=plast8_ru, callback=select_crystal_caves_lvl_ru)

    with dpg.group():
        text_pangolin_ru = dpg.add_text(default_value='''
Атаковать Панголина/Сурка рейдом или вторжением?''')
        radio_btn_pangolin_ru = dpg.add_radio_button((fast_False_ru, fast_True_ru), default_value=fast_False_ru,
                                                     callback=if_fast_attack_pangolin_ru)

        text_shells = dpg.add_text(default_value='''
Открываем сундучки панголина или копите?''')
        radio_btn_shells_ru = dpg.add_radio_button((YES, NO), default_value=NO, callback=if_collect_shells_ru)


    start_btn_ru = dpg.add_button(label="Запустить Макрос", callback=Start_Start_ru)
    btn_main_menu_rus = dpg.add_button(label="Вернутся", callback=open_main_menu_rus)
    dpg.bind_item_font(start_btn_ru, "Font_Button")
    dpg.bind_item_font(btn_main_menu_rus, "Font_Button")

# ======================================================================================================================
# English windows
# ======================================================================================================================
with dpg.window(no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, no_move=True, tag="main_menu_eng", show=False) as main_menu_window_eng:
    with dpg.group(horizontal=True):
        title_eng = dpg.add_text(default_value='Macro for game TheAnts',
                                 pos=[window_width // 2 - 250, window_height // 2 - 100])

        dpg.bind_item_font(title_eng, "Font_Size_72")

    with dpg.group(horizontal=True, pos=[window_width // 2 - 220, window_height // 2 + 30]):
        rule_btn_eng = dpg.add_button(label="Open Rule", callback=open_rule_panel_eng)
        connect_btn_eng = dpg.add_button(label="Connect", callback=open_TheAnts_macro_panel_eng)
        language_btn_eng = dpg.add_button(label="Language", callback=open_select_language)

        dpg.bind_item_font(rule_btn_eng, "Font_Button")
        dpg.bind_item_font(connect_btn_eng, "Font_Button")
        dpg.bind_item_font(language_btn_eng, "Font_Button")

# ----------------------------------------------------------------------------------------------------------------------

with dpg.window(label="Rule", no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, tag="rule_window_eng", no_move=True, show=False) as rule_panel_eng:
    rule_title_eng = dpg.add_text(default_value='MACRO RULE USAGE', pos=[window_width // 2 - 220])

    dpg.add_spacer(width=300, height=72)
    dpg.add_separator()
    dpg.add_spacer(width=300, height=72)

    technical_settings_eng = dpg.add_text(default_value='Technical Settings')

    text_eng1 = dpg.add_text(default_value=first_rule_eng)
    game_settings_eng = dpg.add_text(default_value='Game Settings')
    text_eng2 = dpg.add_text(default_value=second_rule_eng)
    with dpg.group(horizontal=True):
        connect_btn_eng2 = dpg.add_button(label="Next", callback=open_TheAnts_macro_panel_eng)
        btn_main_menu_eng = dpg.add_button(label="Back", callback=open_main_menu_eng)
    dpg.bind_item_font(rule_title_eng, "Font_Size_72")

    dpg.bind_item_font(text_eng1, "Font_Size_25")
    dpg.bind_item_font(text_eng2, "Font_Size_25")

    dpg.bind_item_font(game_settings_eng, "Font_Size_60")
    dpg.bind_item_font(technical_settings_eng, "Font_Size_60")

    dpg.bind_item_font(connect_btn_eng2, "Font_Button")
    dpg.bind_item_font(btn_main_menu_eng, "Font_Button")

# ----------------------------------------------------------------------------------------------------------------------

with dpg.window(label="Macro", no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, tag="macro_window_eng", no_move=True, show=False) as TheAnts_macro_window_eng:
    dpg.add_spacer(width=100, height=15)
    dpg.add_separator()
    dpg.add_spacer(width=100, height=15)

    dpg.add_checkbox(label=TheAnts1, callback=checkbox_callback, user_data=0)
    dpg.add_checkbox(label=TheAnts2, callback=checkbox_callback, user_data=1)
    dpg.add_checkbox(label=TheAnts3, callback=checkbox_callback, user_data=2)
    dpg.add_checkbox(label=TheAnts4, callback=checkbox_callback, user_data=3)
    dpg.add_checkbox(label=TheAnts5, callback=checkbox_callback, user_data=4)
    dpg.add_checkbox(label=TheAnts6, callback=checkbox_callback, user_data=5)
    dpg.add_checkbox(label=TheAnts7, callback=checkbox_callback, user_data=6)
    dpg.add_checkbox(label=TheAnts8, callback=checkbox_callback, user_data=7)
    dpg.add_checkbox(label=TheAnts9, callback=checkbox_callback, user_data=8)

    start_btn_eng = dpg.add_button(label="Start", callback=open_input_menu_eng)
    btn_main_menu_eng = dpg.add_button(label="Back", callback=open_main_menu_eng)
    dpg.bind_item_font(btn_main_menu_eng, "Font_Button")
    dpg.add_spacer(width=100, height=15)
    dpg.add_separator()
    dpg.add_spacer(width=100, height=15)

    dpg.bind_item_font(start_btn_eng, "Font_Button")
# ----------------------------------------------------------------------------------------------------------------------
with dpg.window(no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, no_move=True, tag="input_menu_eng", show=False) as input_menu_eng:
    with dpg.group():
        text_island_eng = dpg.add_text(default_value='''
Are you on the island??''')
        radio_btn_island_eng = dpg.add_radio_button((Yes, No), default_value=No, callback=Island_eng)
    with dpg.group():
        text_chin_eng = dpg.add_text(default_value='''
How many rows are available in the Alliance Salary tab?
These are rewards for Contribution and Attendance''')
        radio_btn_chin_eng = dpg.add_radio_button((chin1_eng, chin2_eng, chin3_eng), default_value=chin2_eng,
                                                  callback=select_chin_lvl_eng)

    with dpg.group():
        text_crystal_caves_eng = dpg.add_text(default_value='''
Choose the layer level you want your squad to occupy in the Crystal Cave.
After a large number of unsuccessful attempts, the Macro will automatically occupy Layer 4.''')
        radio_btn_plast_eng = dpg.add_radio_button(
            (plast3_eng, plast4_eng, plast5_eng, plast6_eng, plast7_eng, plast8_eng), default_value=plast8_eng,
            callback=select_crystal_caves_lvl_eng)

    with dpg.group():
        text_pangolin_eng = dpg.add_text(default_value='''
Attack the Pangolin/Marmot with a raid or an invasion?''')
        radio_btn_pangolin_eng = dpg.add_radio_button((fast_False_eng, fast_True_eng), default_value=fast_False_eng,
                                                      callback=if_fast_attack_pangolin_eng)

    with dpg.group():
        text_shells_eng = dpg.add_text(default_value='''
Do we open the Pangolin chests or save them?''')
        radio_btn_shells_eng = dpg.add_radio_button((Yes, No), default_value=No, callback=if_collect_shells_eng)
    start_btn_eng = dpg.add_button(label="Start Macro", callback=Start_Start_eng)
    btn_main_menu_eng = dpg.add_button(label="Back", callback=open_main_menu_eng)
    dpg.bind_item_font(start_btn_eng, "Font_Button")
    dpg.bind_item_font(btn_main_menu_eng, "Font_Button")

# ======================================================================================================================
dpg.set_primary_window(window=select_language, value=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.render_dearpygui_frame()
dpg.destroy_context()