def imt():
    wgh =  50 + (h - 150) * k + (age - 21)/4
    return(wgh)

while True:
    try:
        h1 = input('Введите ваш рост(см): ')
        if h1.lower() == 'завершить':
            break
        else:
            h = float(h1)
    except ValueError:
        print('Значение должно включать только число.')
        continue
    
    while True:
        try:
            age = float(input('Введите ваш возраст: '))
        except ValueError:
            print('Значение должно включать только число.')
            continue

        while True:
            s = input('Введите ваш пол (m/w): ')
            if s == 'm':
                k = 0.72
                print('Ваш идеальный вес: ' + str(imt()))
                break
            elif s == 'w':
                k = 0.36
                print('Ваш идеальный вес: ' + str(imt()))
                break
            else:
                print('Некорректный ввод. Необходимо выбрать букву.')
        break
