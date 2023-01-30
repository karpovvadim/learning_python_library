"""str.endswith(suffix)"""  # заканчивается
# Возвращает True, если строка заканчивается указанным суффиксом, в противном случае
# возвращает False. suffix также может быть кортежем суффиксов для поиска.

print("-------str.endswith(suffix)----заканчивается------------------")
text = "Python is easy to learn."
result = text.endswith('to learn')  # без точки
print(result)  # returns False
result = text.endswith('to learn.')
print(result)  # returns True

# С необязательным запуском тест начинается с этой позиции.

print("-------str.endswith(suffix[, start])----заканчивается-----------------")
text = "Python programming is easy to learn."
result = text.endswith('learn.', 7)  # строка ищется c 7 позиции
print(result)  # returns True

# С необязательным концом остановите сравнение в этой позиции.

print("-------str.endswith(suffix[, start[, end]])-------------------------")
result = text.endswith('is', 7, 26)  # строка ищется c 7 позиции по 26
print(result)  # Returns False
result = text.endswith('easy', 7, 26)
print(result)  # returns True

# Если строка заканчивается каким-либо элементом кортежа, endwith() возвращает True.
# Если нет, возвращается False.

print("-------С суффиксом кортежа------------------------------------------")
text = "programming is easy"
result = text.endswith(('programming', 'python'))
print(result)  # prints False
result = text.endswith(('python', 'easy', 'java'))
print(result)  # prints True
result = text.endswith(('is', 'an'), 0, 14)
print(result)  # prints True