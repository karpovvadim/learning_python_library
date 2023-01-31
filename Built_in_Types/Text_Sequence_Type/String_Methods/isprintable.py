"""str.isprintable()"""   # для печати       Как использовать?
# Возвращает True, если все символы в строке доступны для печати или строка пуста,
# в противном случае — False. Непечатаемые символы — это символы, определенные в базе
# данных символов Unicode как «Другие» или «Разделители», за исключением пробела
# ASCII (0x20), который считается пригодным для печати. (Обратите внимание, что печатные
# символы в этом контексте — это те символы, которые не следует экранировать при вызове
# repr() для строки. Это не имеет отношения к обработке строк, записанных в sys.stdout
# или sys.stderr.)
s = 'Space is a printable?'
print(s, s.isprintable())

s = '\nNew Line is printable?'
print(s, s.isprintable())

s = ''
print('\nEmpty string printable?', s.isprintable())

# written using ASCII chr(27) is escape character char(97) is letter 'a'
s = chr(27) + chr(97)
if s.isprintable():
    print('Printable')
else:
    print('Not Printable')

s = '2+2 = 4'
if s.isprintable():
    print('Printable')
else:
    print('Not Printable')
