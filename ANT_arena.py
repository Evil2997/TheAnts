import pyautogui as pg
from ahk import AHK
import time
import numpy as np
import cv2
import pytesseract
import pyscreenshot as scr
from mss import mss
ahk = AHK()
mss = mss()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
config = r'--oem 3 --psm 6'
config0 = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
config1 = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789/'

shards_check = False
delay = -1
print('''
На сколько ужасен ваш компьютер от 1 до 3
1 - Очень хороший
2 - Игра работает хорошо
3 - Пойдет
''')
while delay < 1:
    try:
        delay = int(input())
    except ValueError:
        pass
if delay < 1:
    delay = 1
elif delay > 3:
    delay = 3

arena_market = -1
while arena_market < 0:
    try:
        arena_market = int(input('Сколько предметов в магазине арены покупать:\n'))
    except ValueError:
        pass
if arena_market > 5:
    arena_market = 5

ahk.key_down('down')
time.sleep(1)
ahk.key_up('down')

pg.moveTo(152, 370, 1)
pg.dragTo(549, 489, 3)
time.sleep(0.65536 * delay)
pg.moveTo(115, 482, 1)
pg.dragTo(541, 448, 3)
time.sleep(0.65536 * delay)
pg.moveTo(145, 346, 1)
pg.dragTo(385, 523, 3)
time.sleep(0.65536 * delay)
pg.click(164, 490)          # Арена
time.sleep(0.65536 * delay)
pg.click(167, 603)          # Войти на арену
time.sleep(0.65536 * delay)


screen101 = np.array(scr.grab(bbox=(15, 239, 230, 267)))
arena101 = pytesseract.image_to_string(screen101, config=config, lang='rus')
arena_index101 = arena101.find('Дуэль Королев')

if arena_index101 == 0:

    pg.click(150, 150)  # войти на арену Дуэль Королевы
    time.sleep(0.65536 * delay)

    pg.click(300, 50)
    time.sleep(2)
    pg.click(300, 50)
    # !!!
    screen101 = np.array(scr.grab(bbox=(106, 613, 205, 641)))
    arena103 = pytesseract.image_to_string(screen101, config=config)
    arena_index103 = arena103.find('Use')
    pg.click(156, 630)  # Use
    time.sleep(0.65536 * delay)
    pg.click(265, 990)  # напасть
    time.sleep(0.65536 * delay)
    pg.click(496, 832)  # ускорить
    time.sleep(0.65536 * delay)
    pg.click(496, 832)  # свободный клик
    time.sleep(0.65536 * delay)
    # !!!
    pg.click(394, 980)  # вызов
    time.sleep(0.65536 * delay)
    screen101 = np.array(scr.grab(bbox=(427, 343, 500, 369)))
    attempts = pytesseract.image_to_string(screen101, config=config, lang='rus')
    index_attempts = attempts.find('Бесплатно')
    if index_attempts == 0:
        pg.click(460, 355)  # атака
        time.sleep(0.65536 * delay)
        screen104 = np.array(scr.grab(bbox=(106, 618, 203, 631)))
        text101 = pytesseract.image_to_string(screen104, config=config, lang='rus')
        index1_text101 = text101.find('Использовать')
        if index1_text101 == 0:
            pg.click(150, 610)
            time.sleep(0.65536 * delay)
        pg.click(285, 987)  # напасть
        time.sleep(0.65536 * delay)
        pg.click(496, 832)  # ускорить
        time.sleep(0.65536 * delay)
        pg.click(496, 832)  # свободный клик
        time.sleep(0.65536 * delay)
        while index_attempts == 0:
            pg.click(394, 980)  # вызов
            time.sleep(0.65536 * delay)
            screen101 = np.array(scr.grab(bbox=(427, 343, 500, 369)))
            attempts = pytesseract.image_to_string(screen101, config=config, lang='rus')
            index_attempts = attempts.find('Бесплатно')
            if index_attempts == 0:
                pg.click(460, 355)  # атака
                time.sleep(0.65536 * delay)
                pg.click(285, 987)  # напасть
                time.sleep(0.65536 * delay)
                pg.click(496, 832)  # ускорить
                time.sleep(0.65536 * delay)
                pg.click(496, 832)  # свободный клик
                time.sleep(0.65536 * delay)
    pg.click(378, 691)  # плюсик
    time.sleep(0.65536 * delay)
    pg.click(289, 653)  # купить еще 5 попыток
    time.sleep(0.65536 * delay)
    pg.click(464, 792)  # свободный клик

    screen102 = np.array(scr.grab(bbox=(327, 679, 340, 694)))  # количество билетиков
    shards = pytesseract.image_to_string(screen102, config=config0)
    shards = int(shards)
    if shards > 0:
        pg.click(460, 355)  # атака
        time.sleep(0.65536 * delay)
        pg.click(285, 987)  # напасть
        time.sleep(0.65536 * delay)
        pg.click(496, 832)  # ускорить
        time.sleep(0.65536 * delay)
        pg.click(496, 832)  # свободный клик
        time.sleep(0.65536 * delay)
        shards -= 1
        shards_check = True
        while shards > 0:
            pg.click(394, 980)  # вызов
            time.sleep(0.65536 * delay)
            pg.click(460, 355)  # атака
            time.sleep(0.65536 * delay)
            pg.click(285, 987)  # напасть
            time.sleep(0.65536 * delay)
            pg.click(496, 832)  # ускорить
            time.sleep(0.65536 * delay)
            pg.click(496, 832)  # свободный клик
            time.sleep(0.65536 * delay)
            shards -= 1
    if shards_check == True:
        pg.click(394, 980)  # вызов
    "Если остались попытки с прошлого дня"
    pg.click(378, 691)  # плюсик
    time.sleep(0.65536 * delay)
    pg.click(289, 653)  # купить еще от 1 до 5 попыток
    time.sleep(0.65536 * delay)
    pg.click(464, 792)  # свободный клик

    screen102 = np.array(scr.grab(bbox=(327, 679, 340, 694)))  # количество билетиков
    shards = pytesseract.image_to_string(screen102, config=config0)
    shards = int(shards)
    if shards > 0:
        pg.click(460, 355)  # атака
        time.sleep(0.65536 * delay)
        pg.click(285, 987)  # напасть
        time.sleep(0.65536 * delay)
        pg.click(496, 832)  # ускорить
        time.sleep(0.65536 * delay)
        pg.click(496, 832)  # свободный клик
        time.sleep(0.65536 * delay)
        shards -= 1
        while shards > 0:
            pg.click(394, 980)  # вызов
            time.sleep(0.65536 * delay)
            pg.click(460, 355)  # атака
            time.sleep(0.65536 * delay)
            pg.click(285, 987)  # напасть
            time.sleep(0.65536 * delay)
            pg.click(496, 832)  # ускорить
            time.sleep(0.65536 * delay)
            pg.click(496, 832)  # свободный клик
            time.sleep(0.65536 * delay)
            shards -= 1
    for _ in range(5):
        pg.click(60, 70)
        time.sleep(0.256 * delay)

    pg.click(164, 490)          # Арена
    time.sleep(0.65536 * delay)
    pg.click(167, 603)          # Войти на арену
    time.sleep(0.65536 * delay)
    pg.click(150, 150)  # войти на арену Дуэль Королевы
    time.sleep(0.65536 * delay)
# НАГРАДЫ
    pg.click(450, 138)      # награды
    time.sleep(0.65536 * delay)
    pg.click(285, 987)      # получить все
    time.sleep(0.65536 * delay)
    pg.click(275, 629)      # получить
    time.sleep(0.65536 * delay)
    pg.click(285, 987)      # своб клик
    time.sleep(0.65536 * delay)
    pg.click(50, 49)        # назад
    time.sleep(0.65536 * delay)
    pg.click(524, 134)      # магазин
    time.sleep(0.65536 * delay)
    for _ in range(arena_market):
        pg.click(100, 693)      # покупка 1
        time.sleep(0.65536 * delay)
        pg.click(299, 741)      # купить
        time.sleep(0.65536 * delay)
        pg.click(277, 632)      # подтвердить покупку
        time.sleep(0.65536 * delay)
        pg.click(285, 987)      # своб клик
        time.sleep(0.65536 * delay)

    pg.click(50, 49)        # назад
    time.sleep(0.65536 * delay)
    pg.click(50, 49)        # назад
    time.sleep(0.65536 * delay)
    pg.click(50, 49)        # назад
    time.sleep(0.65536 * delay)

#screen = np.array(scr.grab(bbox=(427, 311, 500, 330)))     # 3*3 Арена 'Бесплатно'

present = False
average_present = [0, ]
template_present = cv2.imread('Present.png', 0)
w_present, h_present = template_present.shape[::-1]
for _present in range(67):
    base_screen_present = np.array(scr.grab(bbox=(493, 575, 557, 912)))
    cv2.imwrite('TheAntsPresent.png', base_screen_present)
    img_rgb_present = cv2.imread('TheAntsPresent.png')
    img_gray_present = cv2.cvtColor(img_rgb_present, cv2.COLOR_BGR2GRAY)
    res_present = cv2.matchTemplate(img_gray_present, template_present, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
    loc_present = np.where(res_present >= 0.4)
    try:
        clean_sreen_present = scr.grab(bbox=(x_present, y_present, x_present + w_present, y_present + h_present))
        mean_present = np.mean(clean_sreen_present)
        diff_present = average_present[-1] - mean_present
        if diff_present >= 4:
            break
        average_present.append(mean_present)
    except:
        for pt_present in zip(*loc_present[::-1]):
            x_present = int(pt_present[0])
            y_present = int(pt_present[1])
            time.sleep(0.65536 * delay)
        try:
            pg.click(x_present + 508, y_present + 590)
            present = True
            break
        except NameError:
            pass
    try:
        del(x_present)
        del(y_present)
    except:
        pass
    average_present = [0, ]

if present == True:
    time.sleep(2 * delay)
    pg.click(296, 987)  # получить все (слева)
    time.sleep(0.65536 * delay)
    pg.click(296, 987)  # свободный клик
    time.sleep(0.65536 * delay)
    pg.click(421, 341)  # тык правое окошко подарочков
    time.sleep(0.65536 * delay)
    for present_collection in range(256):
        pg.click(468, 417)  # кнопка получить
        pg.click(466, 523)  # кнопка получить
        pg.click(464, 631)  # кнопка получить
        time.sleep(0.16 * delay)
        pg.click(353, 48)  # свободный клик
        time.sleep(0.16 * delay)
        if present_collection % 4 == 0:
            screen_present = np.array(scr.grab(bbox=(436, 406, 506, 426)))
            text_present = pytesseract.image_to_string(screen_present, config=config, lang='rus')
            index_present = text_present.find('Получить')
            if index_present != 0:
                break
    present = False

pg.click(60, 70)
time.sleep(0.65536 * delay)

average_HandHelp = [0, ]
template_HandHelp = cv2.imread('HandHelp.png', 0)
w_HandHelp, h_HandHelp = template_HandHelp.shape[::-1]

for _ in range(67):     # 1 минута = 67
    base_screen_HandHelp = np.array(scr.grab(bbox=(493, 575, 557, 812)))
    cv2.imwrite('TheAntsHand.png', base_screen_HandHelp)

    img_rgb_HandHelp = cv2.imread('TheAntsHand.png')
    img_gray_HandHelp = cv2.cvtColor(img_rgb_HandHelp, cv2.COLOR_BGR2GRAY)

    res_HandHelp = cv2.matchTemplate(img_gray_HandHelp, template_HandHelp, cv2.TM_CCOEFF_NORMED)  # Поиск template на экране
    loc_HandHelp = np.where(res_HandHelp >= 0.6)
    try:
        clean_sreen_HandHelp = scr.grab(bbox=(x_HandHelp, y_HandHelp, x_HandHelp + w_HandHelp, y_HandHelp + h_HandHelp))
        mean_HandHelp = np.mean(clean_sreen_HandHelp)
        diff_HandHelp = average_HandHelp[-1] - mean_HandHelp
        if diff_HandHelp >= 4:
            break
        average_HandHelp.append(mean_HandHelp)
    except:
        for pt in zip(*loc_HandHelp[::-1]):
            x_HandHelp = int(pt[0])
            y_HandHelp = int(pt[1])
            time.sleep(0.2)
    try:
        pg.click(x_HandHelp + 508, y_HandHelp + 590)
    except NameError:
        pass
    try:
        del(x_HandHelp)
        del(y_HandHelp)
    except:
        pass
    average_HandHelp = [0, ]

pg.click(60, 70)
time.sleep(0.65536 * delay)

pg.click(486, 621)  # королева
time.sleep(0.65536 * delay)