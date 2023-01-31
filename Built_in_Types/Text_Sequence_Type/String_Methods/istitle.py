"""str.istitle()"""  # заглавие
# Верните True, если строка является строкой с заглавным регистром и содержит хотя бы
# один символ, например, символы верхнего регистра могут следовать только за
# символами без регистра, а символы нижнего регистра — только за символами в регистре.
# В противном случае верните False.
# Начинаются ли слова в строке с заглавной буквы.

s = 'Python Is Good.'
print(s.istitle())
s = 'Python is good'
print(s.istitle())
s = 'This Is @ Symbol.'
print(s.istitle())
s = '99 Is A Number'
print(s.istitle())
s = 'PYTHON'
print(s.istitle())

s = 'I Love Python.'
if s.istitle():
    print('Titlecased String')
else:
    print('Not a Titlecased String')

s = 'PYthon'
if s.istitle():
    print('Titlecased String')
else:
    print('Not a Titlecased String')
