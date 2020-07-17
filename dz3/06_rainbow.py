# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x1 = 50
x2 = 350
y1 = 50
y2 = 450
for color in rainbow_colors:
    point = sd.get_point(x1, y1)
    point_2 = sd.get_point(x2, y2)
    sd.line(point, point_2, color, 4)
    x1 += 5
    x2 += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
#
x = 600
y = -100
radius = 210
for color in rainbow_colors:
    center_position = sd.get_point(x, y)
    sd.circle(center_position, radius, color, 5)
    radius += 10
sd.pause()
