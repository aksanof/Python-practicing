def man():
    wgh =  50 + (h - 150) * 0.72 + (age - 21)/4
    return(wgh)

def woman():
    wgh =  50 + (h - 150) * 0.36 + (age - 21)/4
    return(wgh)


h = int(input('Введите ваш рост(см): '))
age = int(input('Введите ваш возраст: '))

while True:
    s = input('Введите ваш пол (m/w): ')
    if s == 'Завершить':
        break
    if s == 'm':
        ves = man()
        print('Ваш идеальный вес: ' + str(ves))
    elif s == 'w':
        ves = woman()
        print('Ваш идеальный вес: ' + str(ves))
    else:
        print('Неправильно введен пол')