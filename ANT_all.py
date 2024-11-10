import os
import base64
import numpy as np
import pyautogui as pg
import cv2
import pytesseract
from ahk import AHK
import datetime
import time
import random
from mss import mss
from PIL import ImageGrab

ahk = AHK()
m = mss()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
config = r'--oem 3 --psm 6'
config0 = r'--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789'

our_color = [35, 38, 66]
path = 'C:'
scans_09 = []
scans_rus = []
delay = 1
a = 50

win = ahk.find_window(title=b'BlueStacks App Player')
window = win.get_pos()
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
"""
599 - 37 = 562 игровое окно по оси X
1034- 37 = 997 игровое окно по оси Y
"""
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
def screenshot_rus(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1-w1) * (wind[2]/562))
    y1 = int(h1 + (Y1-h1) * (wind[3]/997))
    x2 = int(w1 + (X2-w1) * (wind[2]/562))
    y2 = int(h1 + (Y2-h1) * (wind[3]/997))
    screen_rus = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    global scan_rus
    scan_rus = pytesseract.image_to_string(screen_rus, config=config, lang='rus')
    scans_rus.append(scan_rus)


def find_file_path_HandHelp(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('HandHelp'):
                return os.path.abspath(os.path.join(root))

file_path_HandHelp = find_file_path_HandHelp(path)

def Screenshot_HandHelp(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir(file_path_HandHelp)
    base_screen = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    return base_screen


def date_time():
    print(datetime.datetime.now())                         # Точное время и дата
    print(datetime.date.today())                           # Сегоднешний день

    date_time = datetime.datetime.now()
    current_time = date_time.time()
    print(current_time)                                    # Настоящее время

    print(datetime.time(23, 59, 59))                       # Время
    print(datetime.datetime(2022, 12, 31, 23, 59, 59))     # Дата и время

    object_datetime = datetime.timedelta(seconds=36, milliseconds=99, microseconds=11, minutes=28, hours=14, days=3, weeks=8)
    print(object_datetime)

    date = datetime.datetime.today() - datetime.timedelta(days=7)
    print(date)     # День прошлой недели

    date1 = '06/05/21 11:29:58'
    date1_obj = datetime.datetime.strptime(date1, '%m/%d/%y %H:%M:%S')
    print(date1_obj)

    ds1 = 'Friday, April 1, 2022'
    ds2 = '4/1/22'
    ds3 = '4-1-22'
    print(datetime.datetime.strptime(ds1, '%A, %B %d, %Y'))
    print(datetime.datetime.strptime(ds2, '%m/%d/%y'))
    print(datetime.datetime.strptime(ds3, '%m-%d-%y'))

    date_1 = datetime.date(2023, 7, 29)
    date_2 = datetime.date(2023, 10, 7)
    print(date_2 - date_1)



#Переместить окно на нулевые координаты
def zero_window():
    win = ahk.find_window(title=b'BlueStacks App Player')
    win.activate()
    win.move(0, 0, 500, 862)


#Сканирование ячейки в диапазоне от 0 до 100
def vanish_hundred():
    b = '(100/100)'
    a = int(b[1])
    if b[2] == '/':
        print('Число однозначное (', a, ')')
        if a <= 9 and a >= 0:
            print('Идем Сюда')
    elif b[3] == '/':
        c = int(b[2])
        print('Число двузначное (', a*10 + c, ')')
        if a <= 9 and a >= 0:
            print('Идем Сюда')
    else: print('Ячейка заполнена, ищем дальше')

#Оставляет первые D числа списка
def best_four():
    c = list(map(int, input("Введите числа через пробел:\n").split()))
    d = input('Ведите количество элеметов вашего списка:\n')
    if len(c) > d:
        del c[d:len(c)]


def mysorka_chisel():
    burn = -1
    while burn < 0:
        try:
            burn = int(input('Please text here messange\n'))
        except ValueError:
            print('Error, send new messange')


def global_full_screen():
    win = ahk.find_window(title=b'BlueStacks App Player')
    win.activate()
    ahk.key_down('LWin')
    ahk.key_press('m')
    ahk.key_up('LWin')
    win.move(0, 0, 500, 862)
    #ahk.key_state('Control', mode=True)
    #ahk.key_down('down')
    #time.sleep(0.8)
    #ahk.key_up('down')
    #ahk.key_state('Control', mode=False)
    print(pg.position())

# клик с уникально случайной задержкой def

def ClickToTime(x, y):
    r = random.randint(1, 2)
    pg.click(x=x, y=y)
    time.sleep(0.65536 * r)


def Scan_Fragment(filename):
    average = [0, ]
    template = cv2.imread(filename, 0)
    w, h = template.shape[::-1]

    for _ in range(67):  # 1 минута = 67
        base_screen = np.array(ImageGrab.grab(bbox=(482, 575, 559, 891)))

        img_rgb = cv2.imread(base_screen)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
        loc = np.where(res >= 0.6)
        try:
            clean_screen = ImageGrab.grab(bbox=(x, y, x + w, y + h))
            mean = np.mean(clean_screen)
            diff = average[-1] - mean
            if diff >= 4:
                break
            average.append(mean)
        except:
            for pt in zip(*loc[::-1]):
                x = int(pt[0])
                y = int(pt[1])
                time.sleep(0.2)
        try:
            pg.moveTo(x + 508, y + 590, 2)
        except NameError:
            pass
        try:
            del (x)
            del (y)
        except:
            pass
        average = [0, ]


def Color_find():
    our_color = [66, 38, 35]
    # bgr
    monitor = {"top": 1, "left": 2, "width": 1, "height": 1}
    #     #           y1        x1        w = x2 - x1  h = y2 - y1
    def find_color(our_color, monitor={}):
        img = mss.grab(monitor)
        img_arr = np.array(img)
        our_map = (our_color[2], our_color[1], our_color[0], 255)
        indexes = np.where(np.all(img_arr == our_map, axis=-1))  # Сканирование пикселя MAP на карте ARR
        our_crd = np.transpose(indexes)  # Координаты нужных Пикселей найденных на карте ARR
        return our_crd
    for _ in range(20):
        result = find_color(our_color, monitor)
        if result.__len__():
            x = result[0][1] + monitor.get('left')
            y = result[0][0] + monitor.get('top')
            print(x, y)
Encryption_Decryption = 0
if Encryption_Decryption == 1:
    # шифровка файла через путь к файлу
    path = 'C:'
    def find_file_path_Battle(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.startswith('TheAntsBattle.png'):
                    return os.path.abspath(os.path.join(root, file))
        return None

    def image_to_string(file_path_Battle):
        image = cv2.imread(file_path_Battle)
        image_bytes = cv2.imencode('TheAntsBattle.png', image)[1].tobytes()
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')
        return encoded_image

    file_path_Battle = find_file_path_Battle(path)
    image_string = image_to_string(file_path_Battle)

    # Расшифровка файла из шифра
    image_strings = []
    image_strings.append(image_string)
    def string_to_image(image_string):
        image_bytes = base64.b64decode(image_string)
        image_array = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return image

    image = string_to_image(image_string)

    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Screenshot(X1, Y1, X2, Y2):
    x1 = int(w1 + (X1 - w1) * (wind[2] / 562))
    y1 = int(h1 + (Y1 - h1) * (wind[3] / 997))
    x2 = int(w1 + (X2 - w1) * (wind[2] / 562))
    y2 = int(h1 + (Y2 - h1) * (wind[3] / 997))
    os.chdir('TheAnts1')
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    return screenshot


# Поиск Тессеракт.ехе
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
