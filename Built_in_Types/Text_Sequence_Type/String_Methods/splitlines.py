"""str.splitlines(keepends=False)"""   # разделить строки
# Возвращает список строк в строке, разрывая границы строк. Разрывы строк не включаются в
# результирующий список, если не указано значение keepends, равное true.
# Этот метод разбивается на следующие границы строк. В частности, границы представляют
# собой надмножество универсальных новых строк.
# Представление     Описание
# \n                Перевод строки
# \r                Возврат каретки
# \r\n              Возврат каретки + перевод строки
# \v или \x0b       Табулирование строк
# \f или \x0c       Подача формы
# \x1c              Разделитель файлов
# \x1d              Разделитель групп
# \x1e              Разделитель записей
# \x85              Следующая строка (контрольный код C1)
# \u2028            Разделитель строк
# \u2029            Разделитель абзацев
# Changed in version 3.2: \v and \f added to list of line boundaries.
# Изменено в версии 3.2: \v и \f добавлены в список границ строк.
grocery = 'Milk\nChicken\r\nBread\vButter'
print("01", grocery)
print("02", grocery.splitlines())
print("03", grocery.splitlines(True))
grocery = 'Milk Chicken Bread Butter'
print("\n04", grocery.splitlines())

print("\n05", 'ab c\n\nde fg\rkl\r\n'.splitlines())
print("06", 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True))

# В отличие от split (), когда дается SEP строки разделителя, этот метод возвращает пустой
# список для пустой строки, а разрыв строки терминала не приводит к дополнительной линии:
print("\n07", "".splitlines())
print("08", "One line\n".splitlines())

print("09", ''.split('\n'))  # Для сравнения, split('\n') дает:
print("10", 'Two lines\n'.split('\n'))
