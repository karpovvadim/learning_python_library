"""str.isascii()"""
# Возвращает True, если строка пуста или все символы в строке ASCII, в противном случае
# — False. У символов ASCII кодовые точки в диапазоне U+0000-U+007F.
# Добавлено в версии 3.7.
s1 = ''
print(s1.isascii())
s2 = b'The encoded'
print(s2.isascii())
s3 = b'\xc3\x86\xc3\x87\xc3\x88'
print(s3.isascii())
s4 = 'The encoded'
print(s4.isascii())
s5 = 'все символы'
print(s5.isascii())
