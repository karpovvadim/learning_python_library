"""str.find(sub[, start[, end]])"""
# Возвращает наименьший индекс в строке, в которой находится подстрока в срезе s[start:end].
# Необязательные аргументы start и end интерпретируются как в нотации среза.
# Вернуть -1, если подпрограмма не найдена.
# Примечание
# Метод find() следует использовать только в том случае, если вам нужно знать позицию sub.
# Чтобы проверить, является ли sub подстрокой или нет, используйте оператор in:
quote = 'Let it be, let it be, let it be'
result = quote.find('let it')
print("Substring 'let it':", result)
result = quote.find('small')
print("Substring 'small ':", result)
print('Py' in 'Python')
# How to use find()
if quote.find('be,') != -1:
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")
