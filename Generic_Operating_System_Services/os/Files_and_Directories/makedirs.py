"""os.makedirs(name, mode=0o777, exist_ok=False)"""
# Функция рекурсивного создания каталогов. Подобно mkdir(), но создает все каталоги
# промежуточного уровня, необходимые для содержания конечного каталога.
# Параметр mode передается в mkdir() для создания конечного каталога;
# см. описание mkdir() для того, как это интерпретируется. Чтобы установить биты прав
# доступа к файлам любых вновь созданных родительских каталогов, вы можете установить
# umask перед вызовом makedirs(). Биты прав доступа к файлам существующих родительских
# каталогов не изменяются.
# Если для exists_ok установлено значение False (по умолчанию), возникает
# FileExistsError, если целевой каталог уже существует.
#     Внимание
# makedirs() запутается, если элементы пути для создания включают pardir
# (например, «..» в системах UNIX).
# Эта функция правильно обрабатывает пути UNC.
# Вызывает событие аудита os.mkdir с аргументами путь, режим, dir_fd.
# Новое в версии 3.2: параметр exists_ok.
# Изменено в версии 3.4.1: до Python 3.4.1, если для exists_ok было установлено значение
# True и каталог существовал, makedirs() по-прежнему вызывал ошибку, если режим не
# соответствовал режиму существующего каталога. Поскольку такое поведение было
# невозможно безопасно реализовать, оно было удалено в Python 3.4.1. См. bpo-21082.
# Изменено в версии 3.6: принимает объект, подобный пути.
# Изменено в версии 3.7: Аргумент режима больше не влияет на биты прав доступа к файлам
# вновь созданных каталогов промежуточного уровня.
import os

directory = "Interface_to_the_scheduler"  # Интерфейс к планировщику
parent_dir = "/home/vadim/PycharmProjects/learning_python_library/Generic_Operating_System_Services/os/"
path = os.path.join(parent_dir, directory)
try:
    os.makedirs(path)
except FileExistsError:
    print("Directory '%s' created" % directory)
print("-----------------------------------------------")
directory = "c"
parent_dir = "/home/vadim/PycharmProjects/learning_python_library/" \
             "Generic_Operating_System_Services/os/Files_and_Directories/" \
             "Linux_extended_attributes/a/b"
mode = 0o666
path = os.path.join(parent_dir, directory)
try:
    os.makedirs(path, mode)
except FileExistsError:
    print("Directory '%s' created" % path)

# 'Linux extended attributes', 'a', and 'b' will also be created if it does not exists
# If any of the intermediate level directory is missing os.makedirs() method will
# create them
# Если какой-либо из каталогов промежуточного уровня отсутствует, метод os.makedirs()
# создаст их

# os.makedirs() method can be used to create a directory tree
# Метод os.makedirs() можно использовать для создания дерева каталогов.

print("-----------------------------------")
# os.makedirs() method will raise an OSError if the directory to be created already
# exists. But It can be suppressed by setting the value of a parameter exist_ok as True
# Метод os.makedirs() вызовет ошибку OSError, если создаваемый каталог уже существует.
# Но его можно подавить, установив для параметра exists_ok значение True.
directory = "ihritik"
parent_dir = "/home/vadim/PycharmProjects/learning_python_library/" \
             "Generic_Operating_System_Services/os/"
path = os.path.join(parent_dir, directory)
try:
    os.makedirs(path, exist_ok=True)
    print("Directory '%s' created successfully" % directory)
except OSError as error:
    print("Directory '%s' can not be created")

# By setting exist_ok as True error caused due already existing directory can be
# suppressed but other OSError may be raised due to other error like invalid path name
# Установив для exists_ok значение True, ошибку, вызванную уже существующим каталогом,
# можно подавить, но может возникнуть другая ошибка OSError из-за другой ошибки, такой
# как неверное имя пути.
