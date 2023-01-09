"""os.pathconf(path, name)"""
# Возвращает информацию о конфигурации системы, относящуюся к именованному файлу.
# name указывает значение конфигурации для извлечения; это может быть строка, которая
# является именем определенного системного значения; эти имена указаны в ряде стандартов
# (POSIX.1, Unix 95, Unix 98 и др.). Некоторые платформы также определяют
# дополнительные имена. Имена, известные операционной системе хоста, приведены в
# словаре pathconf_names. Для переменных конфигурации, не включенных в это
# сопоставление, также допускается передача целого числа в качестве имени.
# Если имя является строкой и неизвестно, возникает ValueError. Если определенное
# значение имени не поддерживается хост-системой, даже если оно включено в
# pathconf_names, возникает ошибка OSError с номером ошибки errno.EINVAL.
# Эта функция может поддерживать указание файлового дескриптора.
# Доступность: Юникс.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os
print("%s" % os.pathconf_names)
# Retrieve maximum length of a filename (Получить максимальную длину имени файла)
no = os.pathconf('minor.py', 'PC_NAME_MAX')
print("Maximum length of a filename :%d" % no)
# Retrieve file size (Получить размер файла)
no = os.pathconf('minor.py', 'PC_FILESIZEBITS')
print("file size in bits  :%d" % no)

print('-------------------------------------------------------')
"""os.pathconf_names"""
# Словарное сопоставление имен, принимаемых pathconf() и fpathconf(), с целочисленными
# значениями, определенными для этих имен операционной системой хоста. Это можно
# использовать для определения набора имен, известных системе.
#      Доступность: Юникс.
print(os.pathconf_names)
