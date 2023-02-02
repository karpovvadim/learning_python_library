"""str.rindex(sub[, start[, end]])"""
# Подобно rfind(), но вызывает ValueError, когда подстрока sub не найдена.

quote = 'Let it be, let it be, let it be'

result = quote.rindex('let it')
print("Substring 'let it':", result)

result = quote.rindex('be,')
if result != -1:
    print("Highest index where 'be,' occurs:", result)
else:
    print("Doesn't contain substring")