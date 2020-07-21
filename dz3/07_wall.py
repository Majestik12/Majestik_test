# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1000, 500)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

step = 50
for y in range(0, 1000, 50):
    y1 = y + 50
    step -= 50
    for x in range(step, 1000, 100):
        x1 = x + 100
        point = sd.get_point(x, y)
        point1 = sd.get_point(x1, y1)
        sd.rectangle(point, point1, color=sd.COLOR_ORANGE, width=1)
sd.pause()
