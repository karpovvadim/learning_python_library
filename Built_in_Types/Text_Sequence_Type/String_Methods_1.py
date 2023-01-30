

print("-----str.expandtabs(tabsize=8)------развернуть вкладки--------------------")
# Возвращает копию строки, в которой все символы табуляции заменены одним или несколькими
# пробелами, в зависимости от текущего столбца и заданного размера табуляции. Позиции
# табуляции встречаются через каждый символ табуляции (по умолчанию 8, что дает позиции
# табуляции в столбцах 0, 8, 16 и т. д.). Чтобы расширить строку, текущий столбец
# устанавливается равным нулю, и строка проверяется посимвольно. Если символ представляет
# собой табуляцию (\t), в результат вставляется один или несколько пробелов до тех пор,
# пока текущий столбец не сравняется со следующей позицией табуляции. (Сам символ
# табуляции не копируется.) Если символ является символом новой строки (\n) или возврата
# (\r), он копируется, а текущий столбец обнуляется. Любой другой символ копируется без
# изменений, а текущий столбец увеличивается на единицу независимо от того, как символ
# представлен при печати.
str_ = 'xyz\t12345\tabcde'
print('Original String:', str_)
result = str_.expandtabs()  # default tabsize is 8
print('Tabsize 8:      ', result)
str_1 = "xyz\t12345\tabc"
print('Original String:', str_1)
print('Tabsize 2:', str_1.expandtabs(2))  # tabsize is set to 2
print('Tabsize 3:', str_1.expandtabs(3))  # tabsize is set to 3
print('Tabsize 4:', str_1.expandtabs(4))  # tabsize is set to 4
print('Tabsize 5:', str_1.expandtabs(5))  # tabsize is set to 5
print('Tabsize 6:', str_1.expandtabs(6))  # tabsize is set to 6

print("----str.find(sub[, start[, end]])--------------------------------")
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
print("-----str.rfind(sub[, start[, end]])-----------------------------------")
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
