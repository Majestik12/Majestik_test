# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

sd.resolution = (1000, 1000)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def glaz(x, y, color):
    x1 = x - 40
    y1 = y + 40
    point1 = sd.Point(x1, y1)
    sd.circle(point1, 25, color, 2)


def glaz_2(x, y, color):
    x2 = x + 40
    y2 = y + 40
    point2 = sd.Point(x2, y2)
    sd.circle(point2, 25, color, 2)


def ulibka(x, y, color):
    x3 = x - 50
    y3 = y - 10
    x4 = x - 25
    y4 = y - 25
    x5 = x + 25
    y5 = y - 25
    x6 = x + 50
    y6 = y - 10
    point3 = sd.Point(x3, y3)
    point4 = sd.Point(x4, y4)
    point5 = sd.Point(x5, y5)
    point6 = sd.Point(x6, y6)
    point_list = (point3, point4, point5, point6)
    sd.lines(point_list, color, False, 2)


def smile(x, y, color):
    point = sd.Point(x, y, )
    sd.circle(point, 100, color, 5)
    glaz(x, y, color)
    glaz_2(x, y, color)
    ulibka(x, y, color)


random.choice(range(0, 1000))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
smile(random.choice(range(0, 1000)), random.choice(range(0, 1000)), (255, 127, 0))
sd.pause()
