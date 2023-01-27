print("""--------str.capitalize()-----печатать прописными буквами----------""")
# Возвращает копию строки с первым символом, набранным заглавными буквами, и остальными
# строчными буквами.
# Изменено в версии 3.8: первый символ теперь помещается в заглавный, а не в верхний
# регистр. Это означает, что такие символы, как орграфы, будут иметь заглавными только
# первую букву, а не полный символ.
string = "python is AWesome."
capitalized_string = string.capitalize()
print('Old String: ', string)
print('Capitalized String:', capitalized_string)
print("--------str.casefold()--------чехол---------------------------")
# Возвращает свернутую копию строки. Строки с регистром могут использоваться для
# безрегистрового сопоставления.
# Сворачивание регистра похоже на преобразование в нижний регистр, но более агрессивно,
# поскольку оно предназначено для удаления всех регистровых различий в строке.
# Например, немецкая строчная буква «ß» эквивалентна «ss». Поскольку это уже нижний регистр,
# функция lower() ничего не сделает с 'ß'; casefold() преобразует его в "ss".
# Алгоритм сворачивания регистров описан в разделе 3.13 стандарта Unicode.
# Новое в версии 3.3.
string = "PYTHON IS AWESOME"
# print lowercase string
print("Lowercase string:", string.casefold())
firstString = "DER Fluß"
secondString = "der Fluss"
# ß is equivalent to ss
if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
print("-------str.center(width[, fillchar])------------------------")
# Возврат по центру в строке длины ширины. Заполнение выполняется с использованием
# указанного символа заполнения (по умолчанию используется пробел ASCII).
# Исходная строка возвращается, если ширина меньше или равна len(s).
string = "Python is awesome"
new_string = string.center(24)
print("Centered String:", new_string)
new_string_2 = string.center(24, '*')
print("Centered String:", new_string_2)
print("------str.count(sub[, start[, end]])---подсчет подстроки-------------")
# Возвращает количество непересекающихся вхождений подстроки sub в диапазоне [начало,
# конец]. Необязательные аргументы start и end интерпретируются как в нотации среза.
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
count = vowels.count('i')
print('The count of i is:', count)
count = vowels.count('p')
print('The count of p is:', count)
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
count = random.count(('a', 'b'))
print("The count of ('a', 'b') is:", count)
count = random.count([3, 4])
print("The count of [3, 4] is:", count)

print("-----str.encode(encoding='utf-8', errors='strict')-------кодировать-----")
# Возвращает закодированную версию строки в виде объекта bytes. Кодировка по умолчанию
# — «utf-8». ошибки могут быть заданы для установки другой схемы обработки ошибок.
# По умолчанию для ошибок используется «строгий», что означает, что ошибки кодирования
# вызывают ошибку UnicodeError. Другими возможными значениями являются 'ignore', 'replace',
# 'xmlcharrefreplace', 'backslashreplace' и любое другое имя, зарегистрированное через
# codecs.register_error(), см. раздел Обработчики ошибок. Список возможных кодировок
# см. в разделе Стандартные кодировки.
# По умолчанию аргумент ошибок не проверяется на лучшую производительность, а используется
# только при первой ошибке кодирования. Включите режим разработки Python или используйте
# отладочную сборку для проверки ошибок.
# Изменено в версии 3.1: добавлена поддержка аргументов ключевых слов.
# Изменено в версии 3.9: Ошибки теперь проверяются в режиме разработки и в режиме отладки.
# unicode string
string = 'pythön!_ÆÇÈ'
print('The string is:', string)
string_utf = string.encode()
print('The encoded version is:', string_utf)
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))
print("-------str.endswith(suffix)----заканчивается------------------")
# Возвращает True, если строка заканчивается указанным суффиксом, в противном случае
# возвращает False. suffix также может быть кортежем суффиксов для поиска.
text = "Python is easy to learn."
result = text.endswith('to learn')
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
print("-------С суффиксом кортежа------------------------------------------")
# Если строка заканчивается каким-либо элементом кортежа, endwith() возвращает True.
# Если нет, возвращается False.
text = "programming is easy"
result = text.endswith(('programming', 'python'))
print(result)  # prints False
result = text.endswith(('python', 'easy', 'java'))
print(result)  # prints True
result = text.endswith(('is', 'an'), 0, 14)
print(result)  # prints True

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
