"""os.supports_dir_fd"""
# Объект набора, указывающий, какие функции в модуле os принимают дескриптор открытого
# файла для своего параметра dir_fd. Различные платформы предоставляют разные функции,
# а базовые функции, которые Python использует для реализации параметра dir_fd,
# доступны не на всех поддерживаемых Python платформах. Ради согласованности функции,
# которые могут поддерживать dir_fd, всегда позволяют указывать параметр, но будут
# генерировать исключение, если функция используется, когда она недоступна локально.
# (Указание None для dir_fd всегда поддерживается на всех платформах.)
# Чтобы проверить, принимает ли конкретная функция дескриптор открытого файла для своего
# параметра dir_fd, используйте оператор in для supports_dir_fd. Например, это выражение
# оценивается как True, если os.stat() принимает дескрипторы открытых файлов для dir_fd
# на локальной платформе:
# В настоящее время параметры dir_fd работают только на платформах Unix;
# ни один из них не работает в Windows.
#      Новое в версии 3.3.
import os
print(os.stat in os.supports_dir_fd)

"""os.supports_fd"""
# Объект набора, указывающий, какие функции в модуле os позволяют указывать свой параметр
# пути в качестве дескриптора открытого файла на локальной платформе. Различные платформы
# предоставляют разные функции, а базовая функциональность, которую Python использует
# для принятия дескрипторов открытых файлов в качестве аргументов пути, доступна не на
# всех платформах, поддерживаемых Python.
# Чтобы определить, разрешает ли конкретная функция указывать дескриптор открытого файла
# для своего параметра пути, используйте оператор in для supports_fd.
# Например, это выражение оценивается как True, если os.chdir() принимает дескрипторы
# открытых файлов для пути на вашей локальной платформе:
print(os.chdir in os.supports_fd)
#      Новое в версии 3.3.
