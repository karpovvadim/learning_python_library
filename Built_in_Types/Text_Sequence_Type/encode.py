"""str.encode(encoding='utf-8', errors='strict')"""  # кодировать
# Возвращает закодированную версию строки в виде объекта bytes. Кодировка по умолчанию
# — «utf-8». errors (ошибки) могут быть заданы для установки другой схемы обработки ошибок.
# По умолчанию для ошибок используется «строгий», что означает, что ошибки кодирования
# вызывают ошибку UnicodeError. Другими возможными значениями являются 'ignore', 'replace',
# 'xmlcharrefreplace', 'backslashreplace' и любое другое имя, зарегистрированное через
# codecs.register_error(), см. раздел Обработчики ошибок. Список возможных кодировок
# см. в разделе Стандартные кодировки.
# По умолчанию аргумент ошибок не проверяется на лучшую производительность, а используется
# только при первой ошибке кодирования. Включите режим разработки Python или используйте
# отладочную сборку для проверки ошибок.
# Изменено в версии 3.1: добавлена поддержка аргументов ключевых слов.
# Изменено в версии 3.9: Ошибки теперь проверяются в режиме разработки и в режиме debug mode
# (отладки).

string = 'pythön!_ÆÇÈ'
print('The string is:', string)
string_utf = string.encode()
print('The encoded version is:', string_utf)

print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))