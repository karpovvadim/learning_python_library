"""os.fpathconf(fd, name)"""
# Возвращает информацию о конфигурации системы, относящуюся к открытому файлу.
# имя указывает значение конфигурации для извлечения; это может быть строка, которая
# является именем определенного системного значения; эти имена указаны в ряде стандартов
# (POSIX.1, Unix 95, Unix 98 и др.). Некоторые платформы также определяют дополнительные
# имена. Имена, известные операционной системе хоста, приведены в словаре pathconf_names.
# Для переменных конфигурации, не включенных в это сопоставление, также допускается
# передача целого числа в качестве имени.
# Если имя является строкой и неизвестно, возникает ValueError. Если определенное
# значение имени не поддерживается хост-системой, даже если оно включено в pathconf_names,
# возникает ошибка OSError с номером ошибки errno.EINVAL.
# Начиная с Python 3.3, это эквивалентно os.pathconf(fd, name).
# Доступность: Юникс.
import os

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

print("%s" % os.pathconf_names)   # имена конфигурации пути

# Now get maximum number of links to the file.
# (Теперь получите максимальное количество ссылок на файл)
no = os.fpathconf(fd, 'PC_LINK_MAX')
print("Maximum number of links to the file. :%d" % no)

# Now get maximum length of a filename
# Теперь получите максимальную длину имени файла
no = os.fpathconf(fd, 'PC_NAME_MAX')
print("Maximum length of a filename :%d" % no)

# Close opened file (Закрыть открытый файл)
os.close(fd)

print("Closed the file successfully!!")
