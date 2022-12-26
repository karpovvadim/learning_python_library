"""os.path.expandvars(path)"""
# Верните аргумент с развернутыми переменными среды. Подстроки вида $name или
# ${name} заменяются значением имени переменной окружения. Неправильно сформированные
# имена переменных и ссылки на несуществующие переменные остаются без изменений.
# В Windows в дополнение к $name и ${name} поддерживаются расширения %name%.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
print(os.path.expandvars("/home/${USER}/file.txt"))
# '/home/docs-python/file.txt'

print(os.path.expandvars("${HOME}"))
# '/home/docs-python'

print(os.path.expandvars(b"/home/${USER}/file.txt"))