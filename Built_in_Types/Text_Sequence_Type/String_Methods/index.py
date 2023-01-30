"""str.index(sub[, start[, end]])"""
# Аналогично find(), но вызывает ValueError, когда подстрока не найдена.
quote = 'Let it be, let it be, let it be'
result = quote.index('let it')
print("Substring 'let it':", result)
