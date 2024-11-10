import time
import numpy as np
import pyautogui as pg
import cv2
import pytesseract
import pyscreenshot as scr
import charset_normalizer.utils
from ahk import AHK
ahk = AHK()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
config = r'--oem 3 --psm 6'

#           Информация за отряды!
# Введите сколько отрядов из 4 могут атаковать Ящера/Геккона



last_attack = 0
gekkon = -1
lizard_lvl = -1
lizard_troops_attack = -1
energy_limit1 = energy_limit2 = energy_limit3 = energy_limit4 = 1


island = input('''
Вы на острове?
Да ---- " "     (1 Пробел/Space)
Нет --- "Все что угодно или ничего не вводить"
''')
if island == ' ':
    island = True
    pg.click(523, 271)      # События
    time.sleep(0.65536)
    pg.moveTo(264, 189, 1)
    pg.dragTo(240, 500, 1)
    time.sleep(0.65536)
    pg.click(263, 188)      # Остров
    time.sleep(0.65536)
    pg.click(108, 825)      # Вехи
    time.sleep(0.65536)
    screen_is1 = np.array(scr.grab(bbox=(9, 116, 232, 151)))
    text_is1 = pytesseract.image_to_string(screen_is1, config=config, lang='rus')
    screen_is1 = cv2.cvtColor(screen_is1, cv2.COLOR_BGR2GRAY)
    ret1, screen_is1 = cv2.threshold(screen_is1, 180, 255, 0)
    index_is1 = text_is1.find('Первый поход')
    index_is2 = text_is1.find('Взаимодействие')
    index_is3 = text_is1.find('Укрепление муравейника')  # 35lvl gekon + max lvl boundary 18
    index_is4 = text_is1.find('Истребитель')
    index_is5 = text_is1.find('Крепость')
    index_is6 = text_is1.find('Ужасные Пчелы')
    index_is7 = text_is1.find('Попытки на Отмели')
    index_is8 = text_is1.find('Глубокое Исследование') # max lvl boundary 19. 40
    index_is9 = text_is1.find('Путь Завоевания') # на следующем max lvl boundary 20. 40
    if index_is1 == 0 or index_is2 == 0 or index_is3 == 0:
        level_boundary_limit9 = 17
        gekkon = -1     # 0
        lizard_lvl = 7  # 35
        print('Начало всех начал, дикие 17 лвл, Геккона еще нет, Ящерица 35 лвл.')
    elif index_is4 == 0 or index_is5 == 0 or index_is6 == 0 or index_is7 == 0 or index_is8 == 0:
        level_boundary_limit9 = 18
        gekkon = 7  # 40
        print('Часть 2, дикие улучшены на 1 лвл (18), появление Геккона 35 лвл.')
    elif index_is9 == 0:
        level_boundary_limit9 = 19
        gekkon = 8
        print('Часть 3, дикие улучшаются на 2 лвл (19), усиление Геккона 40 лвл.')
    else:
        print('Заключительная часть. Дикие и Геккон не усиливаются, пока цель не будет достигнута.')
        screen_is = np.array(scr.grab(bbox=(14, 376, 146, 392)))
        text_is1 = pytesseract.image_to_string(screen_is, config=config, lang='rus')
        index_is10 = text_is1.find('Достигла цель')
        index_is11 = text_is1.find('Оставшееся время')
        if index_is10 == 0 or index_is11 == 0:
            level_boundary_limit9 = 20
            gekkon = 8
            print('Цель достигнута. Ждем открытие проходов на путь к Древу.')
            if index_is10 == 0:
                print('Проходы открыты. Этап 2 заключительной части - Продвижение к Древу')
            screen_is1 = np.array(scr.grab(bbox=(14,612, 116, 628)))
            text_is2 = pytesseract.image_to_string(screen_is1, config=config, lang='rus')
            index_is12 = text_is2.find('Достигла цель')
            if index_is12 == 0:
                print('Последний этап заключительной части - Захват Плодородного Дерева')
        else:
            level_boundary_limit9 = 19
            gekkon = 8
            print('Цель еще не достигнута')

    time.sleep(0.65536)
    pg.click(50, 50)  # Выход из Вех
    time.sleep(0.65536)
    pg.click(50, 50)  # Выход из вкладки Остров
    time.sleep(0.65536)
    pg.click(50, 50)  # Закрыть вкладку Событий
    time.sleep(0.65536)
else:
    island = False
    index_is4 = -1

if index_is4 == 0 or index_is5 == 0 or index_is6 == 0 or index_is7 == 0 or index_is8 == 0 or index_is9 == 0 or index_is10 == 0 or index_is11 == 0:
    gekkon_boolian = True
else:
    gekkon_boolian = False
if gekkon == -1:
    gekkon_boolian = False

while lizard_troops_attack < 0:
    try:
        lizard_troops_attack = int(input('''
Введите сколько отрядов из 4 вы хотите отправлять на Ящера/Геккона:
0 ---- Отряды не атакуют Ящеров/Гекконов
1 ---- Только особый отряд атакует их
2 ---- Атакуют только 1 и особый отряды
3 ---- Атакуют первые 3 отряда
4 ---- Все 4 отряда
'''))
    except ValueError:
        print('Error 9099')
if lizard_troops_attack > 4:
    lizard_troops_attack = 4
if lizard_troops_attack == 0:
    lizard_attack1 = False
    lizard_attack2 = False
    lizard_attack3 = False
    lizard_attack4 = False
elif lizard_troops_attack == 1:
    lizard_attack1 = True
    lizard_attack2 = False
    lizard_attack3 = False
    lizard_attack4 = False
elif lizard_troops_attack == 2:
    lizard_attack1 = True
    lizard_attack2 = True
    lizard_attack3 = False
    lizard_attack4 = False
elif lizard_troops_attack == 3:
    lizard_attack1 = True
    lizard_attack2 = True
    lizard_attack3 = True
    lizard_attack4 = False
elif lizard_troops_attack == 4:
    lizard_attack1 = True
    lizard_attack2 = True
    lizard_attack3 = True
    lizard_attack4 = True

if island == True and lizard_troops_attack != 0:
# Атака Ящериц/Гекконов
    print('''
Введите уровень Ящерицы/Геккона от 6 до 8:
6 --- 30
7 --- 35
8 --- 40
''')
    while lizard_lvl < 6 or lizard_lvl > 8:
        try:
            lizard_lvl = int(input())
        except ValueError:
            pass
    if lizard_lvl == 8 and gekkon_boolian == True:
        gekkon = 8
    elif lizard_lvl == 8 and gekkon_boolian == False:
        lizard_lvl = 7
    if lizard_lvl == 7 and gekkon_boolian == True:
        gekkon = 7
    elif lizard_lvl == 7 and gekkon_boolian == False:
        lizard_lvl = 7




elif island == False and lizard_troops_attack != 0:
    print('''
Введите уровень Ящерицы от 6 до 7:
1 ---- 5
2 --- 10
3 --- 15
4 --- 20
5 --- 25
6 --- 30
7 --- 35
''')
    while lizard_lvl < 1 or lizard_lvl > 7:
        try:
            lizard_lvl = int(input())
        except ValueError:
            pass

boundary_type9 = -1
while boundary_type9 < 1 or boundary_type9 > 5:
    try:
        boundary_type9 = int(input('''
Выберите тип диких существ для атаки:
Мясо ----- 1
Листья --- 2
Грунт ---- 3
Песок ---- 4
Мед ------ 5
'''))
    except ValueError:
        pass

tylesrss = input('''
Идем на плитки ресурсов?
Да ---- " "     (1 Пробел/Space)
Нет --- "Все что угодно или ничего не вводить"
''')
if tylesrss == ' ':
    tylesrss = True
else:
    tylesrss = False

boundary_type91 = int(input('type boundary: '))
lvl_boundary91 = int(input('lvl boundary: '))
tiles_type91 = int(input('tiles type: '))
tiles_level91 = int(input('tiles lvl: '))
lvl_boundary92 = 15
lvl_boundary93 = 15
lvl_boundary94 = 14


screen966 = np.array(scr.grab(bbox=(22, 356, 48, 372)))
mypawnuk = pytesseract.image_to_string(screen966, config=config)
index966 = mypawnuk.find('GM')
print(index966)
if index966 == 0:
    print('Выхожу из муравейника')
    pg.click(415, 813)
else:
    print('Мы уже на карте')
print('Приступаю к поиску диких существ')


number_lizard_attack = 10     # Количество атак по Ящерице/Геккону
tylesrss = False              # Идем на плитки или нет
boundary_type9 = 4            # Тип диких существ по их ресурсу
lizard_lvl = 7                # Уровень ящерицы
gekkon = 8                    # уровень Геккона
lizard_attack1 = True         # Атакуем Ящерецу или нет
gekkon_boolian = True         # Открыт Геккон или еще нет





bbb = 1
if bbb == 1:
    pg.click(29, 575)                                 # поиск диких существ
    pg.click(91, 826)                                 # Категория дикие существа
    pg.moveTo(448, 657)
    pg.dragTo(8, 660, 0.5)                            # переместиться к песку (существо)
    pg.moveTo(448, 657)
    pg.dragTo(8, 660, 0.5)                            # переместиться в самый конец (Ящерка/Геккон)
    if lizard_attack1 == False:                       # Особый отряд не атакует Ящера/Геккона
        print('Перехожу к диким существам')
        if gekkon_boolian == True:
            # Если мы на острове и отряд не бьет Геккона то переходим к ящерице и бьем диких существ
            pg.moveTo(124, 647)
            pg.dragTo(278, 657, 1)      # Если есть Геккон, то переместить обьектив на Ящерецу
            time.sleep(0.65536)
            # Переместиться на песок, все равно Ящерецу бить не надо
        if boundary_type9 == 1:
            print('Мясо')
        elif boundary_type9 == 2:
            print('Листья')
        elif boundary_type9 == 3:
            print('Грунт')
        elif boundary_type9 == 4:
            print('Песок')
        elif boundary_type9 == 5:
            print('Мед')


    elif lizard_attack1 == True and number_lizard_attack > 0 and energy_limit1 == 1:
        boolian_last_attack = 1         # Кто последний атаковал Ящерецу? отряд 1
        pg.click()  # обьектив на (Я/Г)
        pg.click()  # клик по обьекту (Я/Г)
        screen981 = np.array(scr.grab(bbox=(200, 200, 600, 600)))  # Количество атак оставшихся совершить на Ящерицу
        number_lizard_attack = pytesseract.image_to_string(screen981, config=config)
        number_lizard_attack = int(number_lizard_attack) - 1
        pg.click()  # рейд
        pg.click()  # подтвердить
        pg.click()  # напасть

        # тут проверка после 10 атак
        screen991 = np.array(scr.grab(bbox=(200, 200, 600, 600)))  # Количество атак осталось 0
        need_lizard_attack = pytesseract.image_to_string(screen991, config=config, lang='rus')
        index_need_lizard_attack = need_lizard_attack.find('Подтвердить')
        # Если высветилось окошко после атаки Я/Г
        if index_need_lizard_attack == 0:
            # совершено 10 атак
            number_lizard_attack = 0
            pg.click()  # закрыть вкладку
            pg.click()  # закрыть список с отрядами
            lizard_attack1 = False
            # всем отрядам False

    if energy_limit1 == 1 and last_attack == 0 and lizard_attack1 == False: # Первая атака
        # перейти к нужному дикому существу
        i101 = 0
        while i101 < 20:
            pg.click()  # a--
            i101 = i101 + 1
        i102 = 0
        while i102 < lvl_boundary91:
            pg.click()  # a++
            i102 = i102 + 1
        # отправка отряда
    elif energy_limit1 == 1 and last_attack == 1:  # остался только 1 отряд
        # перейти к нужному дикому существу
        # отправка отряда
        print(1)
    elif energy_limit1 == 1 and last_attack == 2:  # перед 1 отрядом атаковал 2 отряд
        # перейти к нужному дикому существу
        G = lvl_boundary92 - lvl_boundary91
        if G > 0:  # lvl_boudary2 > lvl_boudary1
            i121 = 0
            while i121 < G:
                pg.click()  # a--
                i121 = i121 + 1
        elif G < 0:  # lvl_boundary2 < lvl_boundary1
            G = abs(G)
            i122 = 0
            while i122 < G:
                pg.click()  # a++
                i122 = i122 + 1
        # отправка отряда
    elif energy_limit1 == 1 and last_attack == 3:  # перед 1 отрядом атаковал 3 отряд
        # перейти к нужному дикому существу
        G = lvl_boundary93 - lvl_boundary91
        if G > 0:  # lvl_boudary3 > lvl_boudary1
            i131 = 0
            while i131 < G:
                pg.click()  # a--
                i131 = i131 + 1
        elif G < 0:  # lvl_boundary3 < lvl_boundary1
            G = abs(G)
            i132 = 0
            while i132 < G:
                pg.click()  # a++
                i132 = i132 + 1
        # отправка отряда
    elif energy_limit1 == 1 and last_attack == 4:  # перед 1 отрядом атаковал 4 отряд
        # перейти к нужному дикому существу
        G = lvl_boundary94 - lvl_boundary91
        if G > 0:  # lvl_boudary4 > lvl_boudary1
            i141 = 0
            while i141 < G:
                pg.click()  # a--
                i141 = i141 + 1
        elif G < 0:  # lvl_boundary4 < lvl_boundary1
            G = abs(G)
            i142 = 0
            while i142 < G:
                pg.click()  # a++
                i142 = i142 + 1
        # отправка отряда

    pg.click(395, 742)     #перейти
    pg.click(233, 456)     #выбрать
    pg.click(225, 708)     #кнопка в поле 'атаковать'
    screen912 = np.array(scr.grab(bbox=(523, 63, 593, 78)))             # Энергия Отряда
    energy91 = pytesseract.image_to_string(screen912, config=config)

    #
    #
    #

    if energy91[3] == '/' or energy91[4] == '/':
        print('10 - 99')
        stm91 = int(energy91[1])
        stm92 = int(energy91[2])
        stamina91 = stm91 * 10 + stm92
        print(stamina91)
        if stamina91 >= 20:  #Начало Атаки
            pg.click()      # Отправить отряд в бой
            print('Атакуем диких')
            energy_limit91 = 1
        elif tylesrss == True and int(stamina91) < 20 and int(stamina91) >= 10:             #Плитки

            print('Идем на плитки')
            if island == False:
                if tiles_type91 == 1:
                    # pg.click       открыть поиск
                    # pg.click       выбрать категорию плитки ресурсов
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo      вернуться к мясу
                    # pg.click       выбрать плитку с мясом
                    tiles_level_go91 = 1
                    while tiles_level_go91 < tiles_level91:
                        screen913 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                        tiles_level_go913 = pytesseract.image_to_string(screen913, config=config)
                        # pg.dragTo      #a = a + 1
                    # pg.click       перейти к плитке на карте
                    # pg.click       атака (перейти к выбору отрядов)
                    # pg.click       отправить отряд
                if tiles_type91 == 2:  # ЛИСТОЧКИ
                    # pg.click       открыть поиск
                    # pg.click       выбрать категорию плитки ресурсов
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo      вернуться к мясу (если надо)
                    # pg.dragTo     перейти к листьям
                    # pg.click       выбрать плитку с листьями
                    tiles_level_go92 = 2
                    while tiles_level_go92 < tiles_level91:  # int!!!
                        screen923 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                        tiles_level_go923 = pytesseract.image_to_string(screen923, config=config)
                        # pg.dragTo      #a = a + 1
                if tiles_type91 == 3:  # ГРУНТ
                    # pg.click       открыть поиск
                    # pg.click       выбрать категорию плитки ресурсов
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo     перейти к грунтом
                    # pg.click       выбрать плитку с грунтом
                    tiles_level_go93 = 3
                    while tiles_level_go93 < tiles_level91:  # int!!!
                        screen933 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                        tiles_level_go933 = pytesseract.image_to_string(screen933, config=config)
                        # pg.dragTo      #a = a + 1
                if tiles_type91 == 4:  # ПЕСОК
                    # pg.click       открыть поиск
                    # pg.click       выбрать категорию плитки ресурсов
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo     перейти к песку
                    # pg.click       выбрать плитку с песком
                    tiles_level_go94 = 4
                    while tiles_level_go94 < tiles_level91:  # int!!!
                        screen943 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                        tiles_level_go943 = pytesseract.image_to_string(screen943, config=config)
                        # pg.dragTo      #a = a + 1
            elif island == True:
                pg.click()  # альянс
                pg.click()  # территория
                screen961 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                tiles91 = pytesseract.image_to_string(screen961, config=config)
                if tiles91 != 'Шахта брилиантов Альянса':  # Поменять проверочную фразу
                    pg.click()  # список с плитками
                if tiles_type91 == 1:
                    pg.click()  # Нужная плитка ресурсов
                    pg.click()  # нажать на плитку
                    pg.click()  # кнопка Сбор
                    pg.moveTo()
                    pg.dragTo()
                    pg.moveTo()
                    pg.dragTo()  # Перейти к нужному отряду
                    pg.click()  # нажать на нужный отряд
                    pg.click()  # кнопка отправить
                if tiles_type91 == 2:
                    pg.click()  # Нужная плитка ресурсов
                    pg.click()  # нажать на плитку
                    pg.click()  # кнопка Сбор
                    pg.moveTo()
                    pg.dragTo()
                    pg.moveTo()
                    pg.dragTo()  # Перейти к нужному отряду
                    pg.click()  # нажать на нужный отряд
                    pg.click()  # кнопка отправить
                if tiles_type91 == 3:
                    pg.click()  # Нужная плитка ресурсов
                    pg.click()  # нажать на плитку
                    pg.click()  # кнопка Сбор
                    pg.moveTo()
                    pg.dragTo()
                    pg.moveTo()
                    pg.dragTo()  # Перейти к нужному отряду
                    pg.click()  # нажать на нужный отряд
                    pg.click()  # кнопка отправить
                if tiles_type91 == 4:
                    pg.click()  # Нужная плитка ресурсов
                    pg.click()  # нажать на плитку
                    pg.click()  # кнопка Сбор
                    pg.moveTo()
                    pg.dragTo()
                    pg.moveTo()
                    pg.dragTo()  # Перейти к нужному отряду
                    pg.click()  # нажать на нужный отряд
                    pg.click()  # кнопка отправить

            energy_limit91 = 0
        elif int(stamina91) >= 10:                      # tylesrss == False and int(stamina91) < 20 and
            print('Атакуем дикое еще 1 раз')
            energy_limit91 = 1
        elif int(stamina91) < 10:
            print('Отряд спит дома, энергия закончилась')
            energy_limit91 = 0
    else:
        print('Недостаточно выносливости')
        energy_limit91 = 0



                    #else:
                    #    energy_limit91 = 0
                    #    # pg.click()        закрыть список с отрядами (нападение на дикое существо)






pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'
config = r'--oem 3 --psm 6'



def mypawnuk():
    screen966 = np.array(scr.grab(bbox=(30, 424, 55, 442)))
    mypawnuk = pytesseract.image_to_string(screen966, config=config)
    index_mypawnuk = mypawnuk.find('GM')
    print(index_mypawnuk)
    if index_mypawnuk == 0:
        mypawnuk = True
    else:
        mypawnuk = False


# 8 Проверить
#screen_gekkon_attempts10 = np.array(scr.grab(bbox=(337, 395, 386, 410)))      # Сканируем попытки Остров
#gekkon_attempts10 = pytesseract.image_to_string(screen_gekkon_attempts10, config=config1)
#print(gekkon_attempts10)
#screen_gekkon_attempts10 = np.array(scr.grab(bbox=(337, 432, 386, 447)))       # Сканируем попытки Район
#gekkon_attempts10 = pytesseract.image_to_string(screen_gekkon_attempts10, config=config1)
#print(gekkon_attempts10)
# На острове и на районе координаты отличаются



#screen0 = np.array(scr.grab(bbox=(39, 233, 227, 247)))
#screen0 = cv2.cvtColor(screen0, cv2.COLOR_BGR2GRAY)
#ret, screen0 = cv2.threshold(screen0, 75, 255, 0)
#text0 = pytesseract.image_to_string(screen0, config=config, lang='rus')

#screen1 = np.array(scr.grab(bbox=(39, 290, 227, 304)))
#screen1 = cv2.cvtColor(screen1, cv2.COLOR_BGR2GRAY)
#ret, screen1 = cv2.threshold(screen1, 75, 255, 0)
#text1 = pytesseract.image_to_string(screen1, config=config, lang='rus')

#screen2 = np.array(scr.grab(bbox=(39, 348, 227, 362)))
#screen2 = cv2.cvtColor(screen2, cv2.COLOR_BGR2GRAY)
#ret, screen2 = cv2.threshold(screen2, 75, 255, 0)
#text2 = pytesseract.image_to_string(screen2, config=config, lang='rus')

#screen3 = np.array(scr.grab(bbox=(39, 405, 227, 419)))
#screen3 = cv2.cvtColor(screen3, cv2.COLOR_BGR2GRAY)
#ret, screen3 = cv2.threshold(screen3, 75, 255, 0)
#text3 = pytesseract.image_to_string(screen3, config=config, lang='rus')



#while True:
#    # работает
#    screen_new = np.array(scr.grab(bbox=(39, 233, 227, 247)))
#    screen_new = cv2.cvtColor(screen_new, cv2.COLOR_BGR2GRAY)
#    ret, screen_new = cv2.threshold(screen_new, 75, 255, 0)
#    text_new = pytesseract.image_to_string(screen_new, config=config, lang='rus')
#    if text0 == text_new:
#        print('Отряд в пути')
#    else:
#        print('Отряд дома')
#    time.sleep(4)





# Пока не будет успешного теста с 1 отрядом, сюда можно не заходить

lizard_attack1 = False
lvl_boundary91 = 15
lvl_boundary92 = 17
lvl_boundary93 = 14
lvl_boundary94 = 16
energy_limit1 = 1
energy_limit2 = 1
energy_limit3 = 1
energy_limit4 = 1

#lvl_boundary91 = int(input('Уровень дикого существа для Особого отряда:\n'))

last_attack = 0

if energy_limit1 == 1 and last_attack == 0 and lizard_attack1 == False:  # Первая атака
    # перейти к нужному дикому существу
    for _ in range(20):
        pg.click()  # a--
        time.sleep(0.16)
    i102 = 1
    while i102 < lvl_boundary91:
        pg.click()  # a++
        i102 = i102 + 1
    # отправка отряда
elif energy_limit1 == 1 and last_attack == 1:  # остался только Особый отряд
    # перейти к нужному дикому существу
    # отправка отряда
    print(1)
elif energy_limit1 == 1 and last_attack == 2:  # перед 1 отрядом атаковал 2 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary92 - lvl_boundary91
    if G > 0:  # lvl_boudary2 > lvl_boudary1
        i121 = 0
        while i121 < G:
            pg.click()  # a--
            i121 = i121 + 1
    elif G < 0:  # lvl_boundary2 < lvl_boundary1
        G = abs(G)
        i122 = 0
        while i122 < G:
            pg.click()  # a++
            i122 = i122 + 1
    # отправка отряда
elif energy_limit1 == 1 and last_attack == 3:  # перед 1 отрядом атаковал 3 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary93 - lvl_boundary91
    if G > 0:  # lvl_boudary3 > lvl_boudary1
        i131 = 0
        while i131 < G:
            pg.click()  # a--
            i131 = i131 + 1
    elif G < 0:  # lvl_boundary3 < lvl_boundary1
        G = abs(G)
        i132 = 0
        while i132 < G:
            pg.click()  # a++
            i132 = i132 + 1
    # отправка отряда
elif energy_limit1 == 1 and last_attack == 4:  # перед 1 отрядом атаковал 4 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary94 - lvl_boundary91
    if G > 0:  # lvl_boudary4 > lvl_boudary1
        i141 = 0
        while i141 < G:
            pg.click()  # a--
            i141 = i141 + 1
    elif G < 0:  # lvl_boundary4 < lvl_boundary1
        G = abs(G)
        i142 = 0
        while i142 < G:
            pg.click()  # a++
            i142 = i142 + 1
print('===================')
if energy_limit2 == 1 and last_attack == 1:     # перед 2 отрядом атаковал 1 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary91 - lvl_boundary92
    if G > 0:
        i211 = 0
        while i211 < G:
            pg.click()      # a--
            i211 = i211 + 1
    elif G < 0:
        G = abs(G)
        i212 = 0
        while i212 < G:
            pg.click()      # a++
            i212 = i212 + 1
    # отправка отряда
elif energy_limit2 == 1 and last_attack == 2:       # остался только 2 отряд
    # перейти к нужному дикому существу
    # отправка отряда
    print(2)
elif energy_limit2 == 1 and last_attack == 3:       # перед 2 отрядом атаковал 3 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary93 - lvl_boundary92
    if G > 0:
        i231 = 0
        while i231 < G:
            pg.click()  # a--
            i231 = i231 + 1
    elif G < 0:
        G = abs(G)
        i232 = 0
        while i232 < G:
            pg.click()  # a++
            i232 = i232 + 1
    # отправка отряда
elif energy_limit2 == 1 and last_attack == 4:       # перед 2 отрядом атаковал 4 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary94 - lvl_boundary92
    if G > 0:
        i241 = 0
        while i241 < G:
            pg.click()  # a--
            i241 = i241 + 1
    elif G < 0:
        G = abs(G)
        i242 = 0
        while i242 < G:
            pg.click()  # a++
            i242 = i242 + 1
    # отправка отряда
print('===================')
if energy_limit3 == 1 and last_attack == 1:     # перед 2 отрядом атаковал 1 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary91 - lvl_boundary93
    if G > 0:
        i311 = 0
        while i311 < G:
            pg.click()      # a--
            i311 = i311 + 1
    elif G < 0:
        G = abs(G)
        i312 = 0
        while i312 < G:
            pg.click()      # a++
            i312 = i312 + 1
    # отправка отряда
elif energy_limit3 == 1 and last_attack == 2:       # остался только 2 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary92 - lvl_boundary93
    if G > 0:
        i321 = 0
        while i321 < G:
            pg.click()  # a--
            i321 = i321 + 1
    elif G < 0:
        G = abs(G)
        i322 = 0
        while i322 < G:
            pg.click()  # a++
            i322 = i322 + 1
    # отправка отряда
elif energy_limit3 == 1 and last_attack == 3:       # перед 2 отрядом атаковал 3 отряд
    # перейти к нужному дикому существу
    # отправка отряда
    print(3)
elif energy_limit3 == 1 and last_attack == 4:       # перед 2 отрядом атаковал 4 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary94 - lvl_boundary93
    if G > 0:
        i341 = 0
        while i341 < G:
            pg.click()  # a--
            i341 = i341 + 1
    elif G < 0:
        G = abs(G)
        i342 = 0
        while i342 < G:
            pg.click()  # a++
            i342 = i342 + 1
    # отправка отряда
print('===================')
if energy_limit4 == 1 and last_attack == 1:     # перед 4 отрядом атаковал 1 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary91 - lvl_boundary94
    if G > 0:
        i411 = 0
        while i411 < G:
            pg.click()      # a--
            i411 = i411 + 1
    elif G < 0:
        G = abs(G)
        i412 = 0
        while i412 < G:
            pg.click()      # a++
            i412 = i412 + 1
    # отправка отряда
elif energy_limit4 == 1 and last_attack == 2:       # перед 4 отрядом атаковал 2 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary92 - lvl_boundary94
    if G > 0:
        i421 = 0
        while i421 < G:
            pg.click()  # a--
            i421 = i421 + 1
    elif G < 0:
        G = abs(G)
        i422 = 0
        while i422 < G:
            pg.click()  # a++
            i422 = i422 + 1
    # отправка отряда
elif energy_limit4 == 1 and last_attack == 3:       # перед 4 отрядом атаковал 3 отряд
    # перейти к нужному дикому существу
    G = lvl_boundary93 - lvl_boundary94
    if G > 0:
        i431 = 0
        while i431 < G:
            pg.click()  # a--
            i431 = i431 + 1
    elif G < 0:
        G = abs(G)
        i432 = 0
        while i432 < G:
            pg.click()  # a++
            i432 = i432 + 1
    # отправка отряда
elif energy_limit4 == 1 and last_attack == 4:       # остался только 4
    # перейти к нужному дикому существу
    # отправка отряда
    print(4)



island = input('Если вы на острове, введите 0:\n')
if island == '0':
    island = True
else:
    island = False


if island == True:
    level_boundary_limit9 = 20
else:
    level_boundary_limit9 = 15

print('''
Тип дикого существа по выпадающему из него ресурса:
Мясо ----- 1
Листья --- 2
Грунт ---- 3
Песок ---- 4
Мед ------ 5
''')
boundary_type91 = -1
boundary_type92 = -1
boundary_type93 = -1
boundary_type94 = -1
while boundary_type91 < 0:
    try:
        boundary_type91 = int(input('Введите тип дикого существа для Особого отряда:\n'))
    except ValueError:
        print('Error 1009')
while boundary_type92 < 0:
    try:
        boundary_type92 = int(input('Введите тип дикого существа для 2 отряда:\n'))
    except ValueError:
        print('Error 2009')
while boundary_type93 < 0:
    try:
        boundary_type93 = int(input('Введите тип дикого существа для 3 отряда:\n'))
    except ValueError:
        print('Error 3009')
while boundary_type94 < 0:
    try:
        boundary_type94 = int(input('Введите тип дикого существа для 4 отряда:\n'))
    except ValueError:
        print('Error 4009')

if boundary_type91 > 5:
    boundary_type91 = 5
if boundary_type92 > 5:
    boundary_type92 = 5
if boundary_type93 > 5:
    boundary_type93 = 5
if boundary_type94 > 5:
    boundary_type94 = 5

level_boundary91 = -1
level_boundary92 = -1
level_boundary93 = -1
level_boundary94 = -1
while level_boundary91 < 0:
    try:
        level_boundary91 = int(input('Введите максимальный уровень дикого существа для вашего Особого отряда:\n'))
    except ValueError:
        print('Error 901')
while level_boundary92 < 0:
    try:
        level_boundary92 = int(input('Введите максимальный уровень дикого существа для вашего 1 отряда:\n'))
    except ValueError:
        print('Error 902')
while level_boundary93 < 0:
    try:
        level_boundary93 = int(input('Введите максимальный уровень дикого существа для вашего 2 отряда:\n'))
    except ValueError:
        print('Error 903')
while level_boundary94 < 0:
    try:
        level_boundary94 = int(input('Введите максимальный уровень дикого существа для вашего 3 отряда:\n'))
    except ValueError:
        print('Error 904')


if level_boundary91 >= level_boundary_limit9:
    level_boundary91 = level_boundary_limit9
if level_boundary92 >= level_boundary_limit9:
    level_boundary92 = level_boundary_limit9
if level_boundary93 >= level_boundary_limit9:
    level_boundary93 = level_boundary_limit9
if level_boundary94 >= level_boundary_limit9:
    level_boundary94 = level_boundary_limit9


tiles_level91 = -1
tiles_level92 = -1
tiles_level93 = -1
tiles_level94 = -1
while tiles_level91 < 0:
    try:
        tiles_level91 = int(input('Введите уровень плитки ресурсов для вашего Особого отряда:\n'))
    except ValueError:
        print('Error 911')
while tiles_level92 < 0:
    try:
        tiles_level92 = int(input('Введите уровень плитки ресурсов для вашего 1 отряда:\n'))
    except ValueError:
        print('Error 912')
while tiles_level93 < 0:
    try:
        tiles_level93 = int(input('Введите уровень плитки ресурсов для вашего 2 отряда:\n'))
    except ValueError:
        print('Error 913')
while tiles_level94 < 0:
    try:
        tiles_level94 = int(input('Введите уровень плитки ресурсов для вашего 3 отряда:\n'))
    except ValueError:
        print('Error 914')
if tiles_level91 >= 8:
    tiles_level91 = 8
if tiles_level92 >= 8:
    tiles_level92 = 8
if tiles_level93 >= 8:
    tiles_level93 = 8
if tiles_level94 >= 8:
    tiles_level94 = 8
print('''
Доступно 4 вида ресурсных плит:
Мясо-----1
Листья---2
Грунт----3
Песок----4
''')
tiles_type91 = -1
tiles_type92 = -1
tiles_type93 = -1
tiles_type94 = -1
while tiles_type91 < 0:
    try:
        tiles_type91 = int(input('Введите тип плитки для Особого отряда\n'))
    except ValueError:
        print('Error 9221')
while tiles_type92 < 0:
    try:
        tiles_type92 = int(input('Введите тип плитки для 1 отряда\n'))
    except ValueError:
        print('Error 9222')
while tiles_type93 < 0:
    try:
        tiles_type93 = int(input('Введите тип плитки для 2 отряда\n'))
    except ValueError:
        print('Error 9223')
while tiles_type94 < 0:
    try:
        tiles_type94 = int(input('Введите тип плитки для 3 отряда\n'))
    except ValueError:
        print('Error 9224')

if tiles_type91 > 4:
    tiles_type91 = 4
if tiles_type92 > 4:
    tiles_type92 = 4
if tiles_type93 > 4:
    tiles_type93 = 4
if tiles_type94 > 4:
    tiles_type94 = 4

if tiles_type91 <= 0:
    tiles_type91 = 1
if tiles_type92 <= 0:
    tiles_type92 = 1
if tiles_type93 <= 0:
    tiles_type93 = 1
if tiles_type94 <= 0:
    tiles_type94 = 1


energy_limit91 = energy_limit92 = energy_limit93 = energy_limit94 = 1
energy_limit9 = [energy_limit91, energy_limit92, energy_limit93, energy_limit94]


def first_squad_attack9():
    wild_creature_level91 = 1
    while wild_creature_level91 < level_boundary91:
        screen91 = np.array(scr.grab(bbox=(523, 63, 593, 78)))          # Полоса уровней диких существ
        wild_creature_level91 = pytesseract.image_to_string(screen91, config=config)
        #pg.dragTo       #a = a + 1
    while wild_creature_level91 > level_boundary91:
        screen91 = np.array(scr.grab(bbox=(523, 63, 593, 78)))          # Полоса уровней диких существ
        wild_creature_level91 = pytesseract.image_to_string(screen91, config=config)
        #pg.dragTo       #a = a - 1
    #pg.click()     перейти
    #pg.click()     выбрать
    #pg.click()     атаковать
    #pg.click()     Особый отряд
    screen912 = np.array(scr.grab(bbox=(523, 63, 593, 78)))             # Энергия Отряда
    energy91 = pytesseract.image_to_string(screen912, config=config)
    if int(energy91) >= 20:
        # pg.click()     атаковать выбранным отрядом
        energy_limit91 = 1
    elif int(energy91) < 20 and int(energy91) >= 10:
        energy_limit91 = 1
        # pg.click()        закрыть список с отрядами (нападение на дикое существо)
        if island == False:
            if tiles_type91 == 1:
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу
                # pg.click       выбрать плитку с мясом
                tiles_level_go91 = 1
                while tiles_level_go91 < tiles_level91:
                    screen913 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go913 = pytesseract.image_to_string(screen913, config=config)
                    # pg.dragTo      на еденицу
                # pg.click       перейти к плитке на карте
                # pg.click       атака (перейти к выбору отрядов)
                # pg.click
            if tiles_type91 == 2:
                # pg.click       выйти из муравейника
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу (если надо)
                # pg.dragTo     перейти к листьям
                # pg.click       выбрать плитку с листьями
                tiles_level_go92 = 2
                while tiles_level_go92 < tiles_level92:
                    screen923 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go923 = pytesseract.image_to_string(screen923, config=config)
                    # pg.dragTo      на еденицу
            if tiles_type91 == 3:
                # pg.click       выйти из муравейника
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу
                # pg.dragTo     перейти к грунтом
                # pg.click       выбрать плитку с грунтом
                tiles_level_go93 = 3
                while tiles_level_go93 < tiles_level93:
                    screen933 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go933 = pytesseract.image_to_string(screen933, config=config)
                    # pg.dragTo      на еденицу
            if tiles_type91 == 4:
                # pg.click       выйти из муравейника
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу
                # pg.dragTo     перейти к песку
                # pg.click       выбрать плитку с песком
                tiles_level_go94 = 4
                while tiles_level_go94 < tiles_level94:
                    screen943 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go943 = pytesseract.image_to_string(screen943, config=config)
                    # pg.dragTo      на еденицу
        elif island == True:
            pg.click()  # альянс
            pg.click()  # территория
            screen961 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
            tiles91 = pytesseract.image_to_string(screen961, config=config)
            if tiles91 != 'Шахта брилиантов Альянса':
                pg.click()  # список с плитками
            if tiles_type91 == 1:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type91 == 2:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type91 == 3:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type91 == 4:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
    else:
        energy_limit91 = 0
        # pg.click()        закрыть список с отрядами (нападение на дикое существо)
def second_squad_attack9():
    wild_creature_level92 = 2
    while wild_creature_level92 < level_boundary92:
        screen92 = np.array(scr.grab(bbox=(523, 63, 593, 78)))      # Полоса уровней диких существ
        wild_creature_level92 = pytesseract.image_to_string(screen92, config=config)
        # pg.dragTo     #a = a + 1
    while wild_creature_level92 > level_boundary92:
        screen92 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса уровней диких существ
        wild_creature_level92 = pytesseract.image_to_string(screen92, config=config)
        # pg.dragTo       #a = a - 1
    # pg.click()     перейти
    # pg.click()     выбрать
    # pg.click()     атаковать
    # pg.dragTo      перейти ко 2 отряду
    # pg.click()     2 отряд
    screen922 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
    energy92 = pytesseract.image_to_string(screen922, config=config)
    if int(energy92) >= 20:
        # pg.click()     атаковать выбранным отрядом
        energy_limit92 = 1
    elif int(energy92) < 20 and int(energy92) >= 10:
        energy_limit92 = 1
        # pg.click()        закрыть список с отрядами (нападение на дикое существо)
        if island == False:
            if tiles_type92 == 1:
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу
                # pg.click       выбрать плитку с мясом
                tiles_level_go91 = 1
                while tiles_level_go91 < tiles_level91:
                    screen913 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go913 = pytesseract.image_to_string(screen913, config=config)
                    # pg.dragTo      на еденицу
                # pg.click       перейти к плитке на карте
                # pg.click       атака (перейти к выбору отрядов)
                # pg.click
            if tiles_type92 == 2:
                # pg.click       выйти из муравейника
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу (если надо)
                # pg.dragTo     перейти к листьям
                # pg.click       выбрать плитку с листьями
                tiles_level_go92 = 2
                while tiles_level_go92 < tiles_level92:
                    screen923 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go923 = pytesseract.image_to_string(screen923, config=config)
                    # pg.dragTo      на еденицу
            if tiles_type92 == 3:
                # pg.click       выйти из муравейника
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу
                # pg.dragTo     перейти к грунтом
                # pg.click       выбрать плитку с грунтом
                tiles_level_go93 = 3
                while tiles_level_go93 < tiles_level93:
                    screen933 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go933 = pytesseract.image_to_string(screen933, config=config)
                    # pg.dragTo      на еденицу
            if tiles_type92 == 4:
                # pg.click       выйти из муравейника
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу
                # pg.dragTo     перейти к песку
                # pg.click       выбрать плитку с песком
                tiles_level_go94 = 4
                while tiles_level_go94 < tiles_level94:
                    screen943 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go943 = pytesseract.image_to_string(screen943, config=config)
                    # pg.dragTo      на еденицу
        else:
            pg.click()  # альянс
            pg.click()  # территория
            screen961 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
            tiles91 = pytesseract.image_to_string(screen961, config=config)
            if tiles91 != 'Шахта брилиантов Альянса':
                pg.click()  # список с плитками
            if tiles_type92 == 1:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type92 == 2:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type92 == 3:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type92 == 4:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
    else:
        energy_limit92 = 0
        # pg.click()        закрыть список с отрядами (нападение на дикое существо)
def third_squad_attack9():
    wild_creature_level93 = 3
    while wild_creature_level93 < level_boundary93:
        screen93 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса уровней диких существ
        wild_creature_level93 = pytesseract.image_to_string(screen93, config=config)
        # pg.dragTo     #a = a + 1
    while wild_creature_level93 > level_boundary93:
        screen93 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса уровней диких существ
        wild_creature_level93 = pytesseract.image_to_string(screen93, config=config)
        # pg.dragTo       #a = a - 1
    # pg.click()     перейти
    # pg.click()     выбрать
    # pg.click()     атаковать
    # pg.dragTo      перейти к 3 отряду
    # pg.click()     3 отряд
    screen932 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
    energy93 = pytesseract.image_to_string(screen932, config=config)
    if int(energy93) >= 20:
        # pg.click()     атаковать выбранным отрядом
        energy_limit93 = 1
    elif int(energy93) < 20 and int(energy93) >= 10:
        energy_limit93 = 1
        # pg.click()        закрыть список с отрядами (нападение на дикое существо)
        if island == False:
            if tiles_type93 == 1:
                    # pg.click       открыть поиск
                    # pg.click       выбрать категорию плитки ресурсов
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo      вернуться к мясу
                    # pg.click       выбрать плитку с мясом
                    tiles_level_go91 = 1
                    while tiles_level_go91 < tiles_level91:
                        screen913 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                        tiles_level_go913 = pytesseract.image_to_string(screen913, config=config)
                        # pg.dragTo      на еденицу
                    # pg.click       перейти к плитке на карте
                    # pg.click       атака (перейти к выбору отрядов)
                    # pg.click
            if tiles_type93 == 2:
                    # pg.click       открыть поиск
                    # pg.click       выбрать категорию плитки ресурсов
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo      вернуться к мясу (если надо)
                    # pg.dragTo     перейти к листьям
                    # pg.click       выбрать плитку с листьями
                    tiles_level_go92 = 2
                    while tiles_level_go92 < tiles_level92:
                        screen923 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                        tiles_level_go923 = pytesseract.image_to_string(screen923, config=config)
                        # pg.dragTo      на еденицу
            if tiles_type93 == 3:
                    # pg.click       открыть поиск
                    # pg.click       выбрать категорию плитки ресурсов
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo     перейти к грунтом
                    # pg.click       выбрать плитку с грунтом
                    tiles_level_go93 = 3
                    while tiles_level_go93 < tiles_level93:
                        screen933 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                        tiles_level_go933 = pytesseract.image_to_string(screen933, config=config)
                        # pg.dragTo      на еденицу
            if tiles_type93 == 4:
                    # pg.click       открыть поиск
                    # pg.click       выбрать категорию плитки ресурсов
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo      вернуться к мясу
                    # pg.dragTo     перейти к песку
                    # pg.click       выбрать плитку с песком
                    tiles_level_go94 = 4
                    while tiles_level_go94 < tiles_level94:
                        screen943 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                        tiles_level_go943 = pytesseract.image_to_string(screen943, config=config)
                        # pg.dragTo      на еденицу
        else:
            pg.click()  # альянс
            pg.click()  # территория
            screen961 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
            tiles91 = pytesseract.image_to_string(screen961, config=config)
            if tiles91 != 'Шахта брилиантов Альянса':
                pg.click()  # список с плитками
            if tiles_type93 == 1:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type93 == 2:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type93 == 3:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type93 == 4:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
    else:
        energy_limit93 = 0
        # pg.click()        закрыть список с отрядами (нападение на дикое существо)
def fourth_squad_attack9():
    wild_creature_level94 = 4
    while wild_creature_level94 < level_boundary94:
        screen94 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса уровней диких существ
        wild_creature_level94 = pytesseract.image_to_string(screen94, config=config)
        # pg.dragTo     #a = a + 1
    while wild_creature_level94 > level_boundary94:
        screen94 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса уровней диких существ
        wild_creature_level94 = pytesseract.image_to_string(screen94, config=config)
        # pg.dragTo       #a = a - 1
    # pg.click()     перейти
    # pg.click()     выбрать
    # pg.click()     атаковать
    # pg.dragTo      перейти к 4 отряду
    # pg.click()     4 отряд
    screen942 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
    energy94 = pytesseract.image_to_string(screen942, config=config)
    if int(energy94) >= 20:
        # pg.click()     атаковать выбранным отрядом
        energy_limit94 = 1
    elif int(energy94) < 20 and int(energy94) >= 10:
        energy_limit94 = 1
        # pg.click()        закрыть список с отрядами (нападение на дикое существо)
        if island == False:
            if tiles_type94 == 1:
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу
                # pg.click       выбрать плитку с мясом
                tiles_level_go91 = 1
                while tiles_level_go91 < tiles_level91:
                    screen913 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go913 = pytesseract.image_to_string(screen913, config=config)
                    # pg.dragTo      на еденицу
                # pg.click       перейти к плитке на карте
                # pg.click       атака (перейти к выбору отрядов)
                # pg.click
            if tiles_type94 == 2:
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу (если надо)
                # pg.dragTo     перейти к листьям
                # pg.click       выбрать плитку с листьями
                tiles_level_go92 = 2
                while tiles_level_go92 < tiles_level92:
                    screen923 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go923 = pytesseract.image_to_string(screen923, config=config)
                    # pg.dragTo      на еденицу
            if tiles_type94 == 3:
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу
                # pg.dragTo     перейти к грунтом
                # pg.click       выбрать плитку с грунтом
                tiles_level_go93 = 3
                while tiles_level_go93 < tiles_level93:
                    screen933 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go933 = pytesseract.image_to_string(screen933, config=config)
                    # pg.dragTo      на еденицу
            if tiles_type94 == 4:
                # pg.click       открыть поиск
                # pg.click       выбрать категорию плитки ресурсов
                # pg.dragTo      вернуться к мясу
                # pg.dragTo      вернуться к мясу
                # pg.dragTo     перейти к песку
                # pg.click       выбрать плитку с песком
                tiles_level_go94 = 4
                while tiles_level_go94 < tiles_level94:
                    screen943 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
                    tiles_level_go943 = pytesseract.image_to_string(screen943, config=config)
                    # pg.dragTo      на еденицу
        else:
            pg.click()  # альянс
            pg.click()  # территория
            screen961 = np.array(scr.grab(bbox=(523, 63, 593, 78)))
            tiles91 = pytesseract.image_to_string(screen961, config=config)
            if tiles91 != 'Шахта брилиантов Альянса':
                pg.click()  # список с плитками
            if tiles_type94 == 1:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type94 == 2:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type94 == 3:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
            if tiles_type94 == 4:
                pg.click()  # Нужная плитка ресурсов
                pg.click()  # нажать на плитку
                pg.click()  # кнопка Сбор
                pg.dragTo()  # Перейти к нужному отряду
                pg.click()  # нажать на нужный отряд
                pg.click()  # кнопка отправить
    else:
        energy_limit94 = 0
        # pg.click()        закрыть список с отрядами (нападение на дикое существо)

#pg.click()     выйти за пределы муравейника
#pg.click()     поиск диких существ
#pg.dragTo      1/3
#pg.dragTo      2/3
#pg.dragTo      3/3 переместиться к Ящерке (Геккону)
#pg.dragTo      переместиться к валюте Песок

first_squad_attack9()
second_squad_attack9()
third_squad_attack9()
fourth_squad_attack9()

#Сканировать отправленные отряды

screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
squad_name91 = pytesseract.image_to_string(screen911, config=config)
screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
squad_name92 = pytesseract.image_to_string(screen921, config=config)
screen931 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 3
squad_name93 = pytesseract.image_to_string(screen931, config=config)
screen941 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 4
squad_name94 = pytesseract.image_to_string(screen941, config=config)
squad_name9 = [squad_name91, squad_name92, squad_name93, squad_name94]
squad_name9 = [1, 2, 3, 4]
while energy_limit9 == [1, 1, 1, 1]:
    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
    screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
    squad_rename92 = pytesseract.image_to_string(screen921, config=config)
    screen931 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 3
    squad_rename93 = pytesseract.image_to_string(screen931, config=config)
    screen941 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 4
    squad_rename94 = pytesseract.image_to_string(screen941, config=config)
    if squad_rename91 == squad_name94 and energy_limit91 == 1 and energy_limit92 == 1 and energy_limit93 == 1:
        first_squad_attack9()
        second_squad_attack9()
        third_squad_attack9()
    elif squad_rename91 == squad_name93 and energy_limit91 == 1 and energy_limit92 == 1:
        first_squad_attack9()
        second_squad_attack9()
    elif squad_rename91 == squad_name92 and energy_limit91 == 1:
        first_squad_attack9()
    if squad_rename92 == squad_name94 and energy_limit92 == 1 and energy_limit93 == 1:
        second_squad_attack9()
        first_squad_attack9()
    elif squad_rename92 == squad_name93 and energy_limit92 == 1:
        second_squad_attack9()
    if squad_rename93 == squad_name94 and energy_limit93 == 1:
        third_squad_attack9()
    if squad_rename94 != squad_name94 and energy_limit94 == 1:
        fourth_squad_attack9()

    while energy_limit9 == [0, 1, 1, 1]:
        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
        squad_rename81 = pytesseract.image_to_string(screen911, config=config)
        screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
        squad_rename92 = pytesseract.image_to_string(screen921, config=config)
        screen931 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 3
        squad_rename93 = pytesseract.image_to_string(screen931, config=config)
        if squad_rename91 == squad_name94 and energy_limit92 == 1 and energy_limit93 == 1:
            second_squad_attack9()
            third_squad_attack9()
        elif squad_rename92 == squad_name94 and energy_limit93 == 1:
            third_squad_attack9()
        if squad_rename93 != squad_name94 and energy_limit94 == 1:
            fourth_squad_attack9()

        while energy_limit9 == [0, 0, 1, 1]:
            screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
            squad_rename91 = pytesseract.image_to_string(screen911, config=config)
            screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
            squad_rename92 = pytesseract.image_to_string(screen921, config=config)
            if squad_rename91 == squad_name94 and energy_limit93 == 1:
                third_squad_attack9()
            if squad_rename92 != squad_name94 and energy_limit94 == 1:
                fourth_squad_attack9()
            while energy_limit9 == [0, 0, 0, 1]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                if squad_rename91 != squad_name94 and energy_limit94 == 1:
                    fourth_squad_attack9()
            while energy_limit9 == [0, 0, 1, 0]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                if squad_rename91 != squad_name93 and energy_limit93 == 1:
                    third_squad_attack9()

        while energy_limit9 == [0, 1, 0, 1]:
            screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
            squad_rename91 = pytesseract.image_to_string(screen911, config=config)
            screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
            squad_rename92 = pytesseract.image_to_string(screen921, config=config)
            if squad_rename91 == squad_name94 and energy_limit92 == 1:
                second_squad_attack9()
            if squad_rename92 != squad_name94 and energy_limit94 == 1:
                fourth_squad_attack9()
                while energy_limit9 == [0, 0, 0, 1]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name94 and energy_limit94 == 1:
                        fourth_squad_attack9()
                while energy_limit9 == [0, 1, 0, 0]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name92 and energy_limit92 == 1:
                        second_squad_attack9()

        while energy_limit9 == [0, 1, 1, 0]:
            screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
            squad_rename91 = pytesseract.image_to_string(screen911, config=config)
            screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
            squad_rename92 = pytesseract.image_to_string(screen921, config=config)
            if squad_rename91 == squad_name93 and energy_limit92 == 1:
                second_squad_attack9()
            if squad_rename92 != squad_name93 and energy_limit93 == 1:
                third_squad_attack9()
            while energy_limit9 == [0, 0, 1, 0]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                if squad_rename91 != squad_name93 and energy_limit93 == 1:
                    third_squad_attack9()
            while energy_limit9 == [0, 1, 0, 0]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                if squad_rename91 != squad_name92 and energy_limit92 == 1:
                    second_squad_attack9()

    while energy_limit9 == [1, 0, 1, 1]:
        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
        squad_rename91 = pytesseract.image_to_string(screen911, config=config)
        screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
        squad_rename92 = pytesseract.image_to_string(screen921, config=config)
        screen931 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 3
        squad_rename93 = pytesseract.image_to_string(screen931, config=config)
        if squad_rename91 == squad_name94 and energy_limit91 == 1 and energy_limit93 == 1:
            first_squad_attack9()
            third_squad_attack9()
        elif squad_rename92 == squad_name94 and energy_limit93 == 1:
            third_squad_attack9()
        if squad_rename93 != squad_name94 and energy_limit94 == 1:
            fourth_squad_attack9()
            while energy_limit9 == [0, 0, 1, 1]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
                squad_rename92 = pytesseract.image_to_string(screen921, config=config)
                if squad_rename91 == squad_name94 and energy_limit93 == 1:
                    third_squad_attack9()
                if squad_rename92 != squad_name94 and energy_limit94 == 1:
                    fourth_squad_attack9()
                while energy_limit9 == [0, 0, 0, 1]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name94 and energy_limit94 == 1:
                        fourth_squad_attack9()
                while energy_limit9 == [0, 0, 1, 0]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name93 and energy_limit93 == 1:
                        third_squad_attack9()

            while energy_limit9 == [0, 1, 0, 1]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
                squad_rename92 = pytesseract.image_to_string(screen921, config=config)
                if squad_rename91 == squad_name94 and energy_limit92 == 1:
                    second_squad_attack9()
                if squad_rename92 != squad_name94 and energy_limit94 == 1:
                    fourth_squad_attack9()
                    while energy_limit9 == [0, 0, 0, 1]:
                        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                        squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                        if squad_rename91 != squad_name94 and energy_limit94 == 1:
                            fourth_squad_attack9()
                    while energy_limit9 == [0, 1, 0, 0]:
                        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                        squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                        if squad_rename91 != squad_name92 and energy_limit92 == 1:
                            second_squad_attack9()

            while energy_limit9 == [1, 0, 0, 1]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
                squad_rename92 = pytesseract.image_to_string(screen921, config=config)
                if squad_rename91 == squad_name94 and energy_limit91 == 1:
                    first_squad_attack9()
                if squad_rename92 != squad_name94 and energy_limit94 == 1:
                    fourth_squad_attack9()
                    while energy_limit9 == [0, 0, 0, 1]:
                        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                        squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                        if squad_rename91 != squad_name94 and energy_limit94 == 1:
                            fourth_squad_attack9()
                    while energy_limit9 == [1, 0, 0, 0]:
                        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                        squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                        if squad_rename91 != squad_name91 and energy_limit91 == 1:
                            first_squad_attack9()

    while energy_limit9 == [1, 1, 0, 1]:
        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
        squad_rename81 = pytesseract.image_to_string(screen911, config=config)
        screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
        squad_rename92 = pytesseract.image_to_string(screen921, config=config)
        screen931 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 3
        squad_rename93 = pytesseract.image_to_string(screen931, config=config)
        if squad_rename91 == squad_name94 and energy_limit91 == 1 and energy_limit92 == 1:
            first_squad_attack9()
            second_squad_attack9()
        elif squad_rename92 == squad_name94 and energy_limit92 == 1:
            second_squad_attack9()
        if squad_rename93 != squad_name94 and energy_limit94 == 1:
            fourth_squad_attack9()
        while energy_limit9 == [0, 1, 0, 1]:
            screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
            squad_rename91 = pytesseract.image_to_string(screen911, config=config)
            screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
            squad_rename92 = pytesseract.image_to_string(screen921, config=config)
            if squad_rename91 == squad_name94 and energy_limit92 == 1:
                second_squad_attack9()
            if squad_rename92 != squad_name94 and energy_limit94 == 1:
                fourth_squad_attack9()
                while energy_limit9 == [0, 0, 0, 1]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name94 and energy_limit94 == 1:
                        fourth_squad_attack9()
                while energy_limit9 == [0, 1, 0, 0]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name92 and energy_limit92 == 1:
                        second_squad_attack9()
        while energy_limit9 == [1, 0, 0, 1]:
            screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
            squad_rename91 = pytesseract.image_to_string(screen911, config=config)
            screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
            squad_rename92 = pytesseract.image_to_string(screen921, config=config)
            if squad_rename91 == squad_name94 and energy_limit91 == 1:
                first_squad_attack9()
            if squad_rename92 != squad_name94 and energy_limit94 == 1:
                fourth_squad_attack9()
                while energy_limit9 == [0, 0, 0, 1]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name94 and energy_limit94 == 1:
                        fourth_squad_attack9()
                while energy_limit9 == [1, 0, 0, 0]:
                    screen811 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename81 = pytesseract.image_to_string(screen811, config=config)
                    if squad_rename91 != squad_name91 and energy_limit91 == 1:
                        first_squad_attack9()
        while energy_limit9 == [1, 1, 0, 0]:
            screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
            squad_rename91 = pytesseract.image_to_string(screen911, config=config)
            screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
            squad_rename92 = pytesseract.image_to_string(screen921, config=config)
            if squad_rename91 == squad_name92 and energy_limit91 == 1:
                first_squad_attack9()
            if squad_rename92 != squad_name92 and energy_limit92 == 1:
                second_squad_attack9()
            while energy_limit9 == [0, 1, 0, 0]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                if squad_rename91 != squad_name92 and energy_limit92 == 1:
                    second_squad_attack9()
            while energy_limit9 == [1, 0, 0, 0]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                if squad_rename91 != squad_name91 and energy_limit91 == 1:
                    first_squad_attack9()

    while energy_limit9 == [1, 1, 1, 0]:
        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
        squad_rename91 = pytesseract.image_to_string(screen911, config=config)
        screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
        squad_rename92 = pytesseract.image_to_string(screen921, config=config)
        screen931 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 3
        squad_rename93 = pytesseract.image_to_string(screen931, config=config)
        if squad_rename91 == squad_name93 and energy_limit91 == 1 and energy_limit92 == 1:
            first_squad_attack9()
            second_squad_attack9()
        elif squad_rename92 == squad_name93 and energy_limit92 == 1:
            second_squad_attack9()
        if squad_rename93 != squad_name93 and energy_limit93 == 1:
            third_squad_attack9()
            while energy_limit9 == [0, 1, 1, 0]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
                squad_rename92 = pytesseract.image_to_string(screen921, config=config)
                if squad_rename91 == squad_name93 and energy_limit92 == 1:
                    second_squad_attack9()
                if squad_rename92 != squad_name93 and energy_limit93 == 1:
                    third_squad_attack9()
                while energy_limit9 == [0, 0, 1, 0]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name93 and energy_limit93 == 1:
                        third_squad_attack9()
                while energy_limit9 == [0, 1, 0, 0]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name92 and energy_limit92 == 1:
                        second_squad_attack9()
            while energy_limit9 == [0, 1, 0, 1]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
                squad_rename92 = pytesseract.image_to_string(screen921, config=config)
                if squad_rename91 == squad_name94 and energy_limit92 == 1:
                    second_squad_attack9()
                if squad_rename92 != squad_name94 and energy_limit94 == 1:
                    fourth_squad_attack9()
                    while energy_limit9 == [0, 0, 0, 1]:
                        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                        squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                        if squad_rename91 != squad_name94 and energy_limit94 == 1:
                            fourth_squad_attack9()
                    while energy_limit9 == [0, 1, 0, 0]:
                        screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                        squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                        if squad_rename91 != squad_name92 and energy_limit92 == 1:
                            second_squad_attack9()
            while energy_limit9 == [1, 1, 0, 0]:
                screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                screen921 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 2
                squad_rename92 = pytesseract.image_to_string(screen921, config=config)
                if squad_rename91 == squad_name92 and energy_limit91 == 1:
                    first_squad_attack9()
                if squad_rename92 != squad_name92 and energy_limit92 == 1:
                    second_squad_attack9()
                while energy_limit9 == [0, 1, 0, 0]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name92 and energy_limit92 == 1:
                        second_squad_attack9()
                while energy_limit9 == [1, 0, 0, 0]:
                    screen911 = np.array(scr.grab(bbox=(523, 63, 593, 78)))  # Полоса Отправленного отряда № 1
                    squad_rename91 = pytesseract.image_to_string(screen911, config=config)
                    if squad_rename91 != squad_name91 and energy_limit91 == 1:
                        first_squad_attack9()
