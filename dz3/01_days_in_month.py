# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
month_1 = 0
if month == 1:
    month_1 = 31
elif month == 2:
    month_1 = 28
elif month == 3:
    month_1 = 31
elif month == 4:
    month_1 = 30
elif month == 5:
    month_1 = 31
elif month == 6:
    month_1 = 30
elif month == 7:
    month_1 = 31
elif month == 8:
    month_1 = 31
elif month == 9:
    month_1 = 30
elif month == 10:
    month_1 = 31
elif month == 11:
    month_1 = 30
elif month == 12:
    month_1 = 31
else:

    print("Вы ввели некорректное число")
print('Дней в этом месяце %s' % month_1)
