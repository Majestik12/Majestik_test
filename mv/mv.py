while True:
    user_input = input('Введите 44 >> ')
    result = int(user_input)
    if result == 44:
        print('Спасибо за сотрудничество!')
        break
    else:
        print('Я просил 44, а Вы ввели', result, 'Попробуйте еще раз...')
