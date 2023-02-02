"""str.startswith(prefix[, start[, end]])"""  # начинается с
# Возвращает True, если строка начинается с prefix, в противном случае вернёт False.
# prefix также может быть набором префиксов, которые нужно искать. При необязательном
# start тестовая строка начинается с этой позиции. С необязательным end прекратить
# сравнивать строку в этой позиции.

print("-------str.startswith(prefix)---------------------------------------")
text = "Python is easy to learn."
result = text.startswith('is easy')

print(result)
result = text.startswith('Python is ')  # returns True
print(result)

result = text.startswith('Python is easy to learn.')
print(result)

print("-------str.startswith(prefix[, start])--------------------------------")
text = "Python programming is easy."
result = text.startswith('programming is', 7)
print(result)

print("-------str.startswith(prefix[, start[, end]])--------------------------")
result = text.startswith('programming is', 7, 18)
print(result)

result = text.startswith('programming', 7, 18)
print(result)

print("-------С префиксом кортежа---------------------------------------------")
text = "programming is easy"
result = text.startswith(('python', 'programming'))  # True
print(result)

result = text.startswith(('is', 'easy', 'java'))  # False
print(result)

# With start and end parameter 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)  # False
print(result)

result = text.startswith(('programming', 'easy', 'is'), 12, 19)
print(result)
