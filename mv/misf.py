import time

my_pets = ['lion', 'dog', 'skunk', 'hamster', 'cat', 'monkey']
i = -1
while i < len(my_pets):
    i += 1
    if i == 2:
        print('Скунса даже проверять не будем, бее!')
        time.sleep(2)
        continue
    pet = my_pets[i]
    print('Проверяем ', pet)
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    if pet == 'cat':
        print('Ура, кот найден!')
        break
    else:
        print('Это не кот!!!')
    time.sleep(2)
print('дотвиданя!')
