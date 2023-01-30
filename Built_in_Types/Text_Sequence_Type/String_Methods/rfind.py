"""str.rfind(sub[, start[, end]])"""
# Возвращает самый высокий индекс в строке, где найдена подстрока sub, так что sub
# содержится в пределах s[start:end]. Необязательные аргументы start и end интерпретируются
# как в нотации среза. Возврат -1 в случае неудачи.
quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if result != -1:
    print("Highest index where 'be,' occurs:", result)
else:
    print("Doesn't contain substring")