"""os.mkdir(path, mode=0o777, *, dir_fd=None)"""
# Создайте каталог с именем пути в числовом режиме.
# Если каталог уже существует, возникает FileExistsError. Если родительский каталог в
# пути не существует, возникает FileNotFoundError.
# В некоторых системах mode игнорируется. Там, где он используется, текущее значение
# umask сначала маскируется. Если установлены биты, отличные от последних 9 (т. е.
# последние 3 цифры восьмеричного представления mode), их значение зависит от
# платформы. На некоторых платформах они игнорируются, и вы должны явно вызывать
# chmod() для их установки.
# Эта функция также может поддерживать пути относительно дескрипторов каталогов.
# Также можно создавать временные каталоги;
# см. функцию tempfile.mkdtemp() модуля tempfile.
# Вызывает событие аудита os.mkdir с аргументами путь, режим, dir_fd.
# Новое в версии 3.3: Аргумент dir_fd.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os

directory = "Process_Management"  # Directory
parent_dir = "/home/vadim/PycharmProjects/learning_python_library/Generic_Operating_System_Services/os/"  # Parent Directory path
path = os.path.join(parent_dir, directory)  # Path

# Create the directory 'Process_Management' in '/home/vadim/PycharmProjects/
# learning_python_library/Generic_Operating_System_Services/os/'
#os.mkdir(path)
print("Directory '%s' created" % directory)

directory = "ihritik"  # Directory
# Parent Directory path
parent_dir = "/home/vadim/PycharmProjects/learning_python_library/Generic_Operating_System_Services/os/"
mode = 0o666
path = os.path.join(parent_dir, directory)
# Create the directory "Process_Management" in '/home/vadim/PycharmProjects/
# learning_python_library/Generic_Operating_System_Services/ os/' with mode 0o666
#os.mkdir(path, mode)
print("Directory '%s' created" % directory)
print('---------------------------------------')
# Ошибка обработки при использовании метода os.mkdir()
path = "/home/vadim/PycharmProjects/learning_python_library/Generic_Operating_System_Services/os/ihritik"
try:
    os.mkdir(path)
except OSError as error:
    print(error)
