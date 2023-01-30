"""str.islower()"""  # нижний  Как использовать в программе?
# Возвращает True, если все символы [4] в строке в нижнем регистре и есть хотя бы один
# символ в регистре, в противном случае — False.
# [4] - Символы в регистре — это те, общее свойство категории которых является одним из
# «Lu» (буква, верхний регистр), «Ll» (буква, нижний регистр) или «Lt» (буква, заглавный).
#        	Состоит ли строка из символов в нижнем регистре
s = 'this is good'
print(s.islower())
if s.islower():
    print('Does not contain uppercase letter.')
else:
    print('Contains uppercase letter.')

s = 'this is Good'
if s.islower():
    print('Does not contain uppercase letter.')
else:
    print('Contains uppercase letter.')
