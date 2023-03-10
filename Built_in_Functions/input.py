# Если присутствует аргумент приглашения, он записывается в стандартный вывод без
# завершающей новой строки. Затем функция считывает строку из ввода, преобразует ее
# в строку (удаляя завершающую новую строку) и возвращает ее. При чтении EOF возникает
# ошибка EOFError. Пример:
# get input from user

inputString = input()
print('The inputted string is:', inputString)

# Если модуль readline был загружен, то input() будет использовать его для предоставления
# расширенных функций редактирования строк и истории.
# Вызывает встроенное событие аудита.input с подсказкой аргумента перед чтением ввода
# Вызывает встроенное событие аудита.input/result с результатом после успешного чтения ввода.

# get input from user
inputString = input('Enter a string:')
print('The inputted string is:', inputString)
