def imt():
    wgh =  50 + (h - 150) * k + (age - 21)/4
    return(wgh)

h = float(input('Введите ваш рост(см): '))
age = float(input('Введите ваш возраст: '))

while True:
    s = input('Введите ваш пол (m/w): ')
    if s == 'Завершить':
        break
    if s == 'm':
        k = 0.72
        print('Ваш идеальный вес: ' + str(imt()))
        break
    elif s == 'w':
        k = 0.36
        print('Ваш идеальный вес: ' + str(imt()))
        break
    else:
        print('Неправильно введен пол')