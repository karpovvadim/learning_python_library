"""os.remove(path, *, dir_fd=None)"""
# Удалить (удалить) путь к файлу. Если путь является каталогом, возникает ошибка
# OSError. Используйте rmdir() для удаления каталогов. Если файл не существует,
# возникает FileNotFoundError.
# Эта функция может поддерживать пути относительно дескрипторов каталогов.
# В Windows попытка удалить файл, который используется, приводит к возникновению
# исключения; в Unix запись каталога удаляется, но хранилище, выделенное для файла,
# не становится доступным до тех пор, пока исходный файл больше не используется.
# Эта функция семантически идентична unlink().
# Вызывает событие аудита os.remove с аргументами path, dir_fd.
#      Новое в версии 3.3: Аргумент dir_fd.
#      Изменено в версии 3.6: принимает объект, подобный пути.
import os
print("--------------------to remove a file---------------------------")
open('filex.txt', 'w')
file = 'filex.txt'
print(os.path.isfile(file))
location = "/home/vadim/PycharmProjects/learning_python_library/" \
           "Generic_Operating_System_Services/os/Files_and_Directories/"
path = os.path.join(location, file)
os.remove(path)
print("%s has been removed successfully" % file)

print("---------Handling error while using os.remove() method----------------")
path = '/home/User/Documents/ihritik'

try:
    os.remove(path)
    print("% s removed successfully" % path)
except OSError as error:
    print(error)
    print("File path can not be removed")

print('----------------------------------------------')
f = 'test_delete.txt'

with open(f, 'w') as fp:
    fp.write('data string')

print(os.path.isfile(f))
os.remove(f)
print(os.path.isfile(f))
