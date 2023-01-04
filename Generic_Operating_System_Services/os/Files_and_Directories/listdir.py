"""os.listdir(path='.')"""
# Возвращает список, содержащий имена записей в каталоге, указанном путем. Список
# находится в произвольном порядке и не включает специальные записи '.' и «..», даже
# если они присутствуют в каталоге. Если файл удаляется из каталога или добавляется в
# него во время вызова этой функции, не указано, будет ли включаться имя этого файла.
# path может быть путеподобным объектом. Если путь имеет тип bytes (напрямую или
# косвенно через интерфейс PathLike), возвращаемые имена файлов также будут иметь тип
# bytes; во всех остальных случаях они будут иметь тип str.
# Эта функция также может поддерживать указание файлового дескриптора; дескриптор
# файла должен ссылаться на каталог.
# Вызывает событие аудита os.listdir с путем аргумента.
#      внимание
# Чтобы закодировать имена файлов str в байты, используйте fsencode().
#      Смотрите также
# Функция scandir() возвращает записи каталога вместе с информацией об атрибутах
# файла, обеспечивая более высокую производительность во многих распространенных случаях
# использования.
# Изменено в версии 3.2: Параметр пути стал необязательным.
# Новое в версии 3.3: Добавлена поддержка указания пути в качестве дескриптора
# открытого файла.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os
# Get the list of all files and directories in the root directory
print("---Получить список всех файлов и каталогов в корневом каталоге----")
path = "/"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
print(dir_list)

print("-----список всех файлов и каталогов в указанном каталоге каталоге----")
# Get the path of current working directory (Получить путь к текущему рабочему каталогу)
path = os.getcwd()
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
print(dir_list)

print("------список всех файлов и каталогов в текущем рабочем каталоге--------")
# If we do not specify any path os.listdir() method will return the list of all
# files and directories in current working directory
# Если мы не укажем никакого пути, метод os.listdir() вернет список всех файлов
# и каталогов в текущем рабочем каталоге.
dir_list = os.listdir()
print("Files and directories in  current working directory :")
print(dir_list)