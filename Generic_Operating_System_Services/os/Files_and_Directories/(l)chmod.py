"""os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)"""
# Измените режим пути на числовой режим. mode может принимать одно из следующих значений
# (как определено в модуле stat) или их комбинации с побитовым ИЛИ:
"""
stat.S_ISUID - Устанавливает бит идентификатора пользователя.
stat.S_ISGID - Устанавливает бит идентификатора группы. Этот бит имеет несколько
    специальных применений.
        Для каталога это означает, что файлы наследуют идентификатор своей группы из
        каталога, а не от эффективного идентификатора группы процесса создания, и
        созданные там каталоги также получат установленный бит S_ISGID.
        Для файла, который не имеет установленного бита выполнения группы S_IXGRP,
        бит set-group-ID указывает на обязательную блокировку файла/записей (смотрите
        также S_ENFMT).
stat.S_ENFMT - Система V принудительно блокирует файлы. Этот флаг используется
    совместно с SISGID: блокировка файлов/записей применяется к файлам, для которых
    не установлен бит выполнения группы (SIXGRP).
stat.S_ISVTX - Липкий бит. Когда этот бит установлен в каталоге, это означает,
    что файл в этом каталоге может быть переименован или удален только владельцем
    файла, владельцем каталога или привилегированным процессом.
stat.S_IREAD - Unix V7 синоним для S_IRUSR.
stat.S_IWRITE - Unix V7 синоним для S_IWUSR.
stat.S_IEXEC - Unix V7 синоним для S_IXUSR.
stat.S_IRWXU - Маска устанавливает для пользователя права rwx.
stat.S_IRUSR - Владелец имеет разрешение на чтение.
stat.S_IWUSR - Владелец имеет разрешение на запись.
stat.S_IXUSR - Владелец имеет разрешение на исполнение.,
stat.S_IRWXG - Маска устанавливает для группы права rwx.
stat.S_IRGRP - Группа имеет разрешение на чтение.
stat.S_IWGRP - Группа имеет разрешение на запись.
stat.S_IXGRP - Группа имеет разрешение на исполнение.
stat.S_IRWXO - Маска устанавливает для других (не в группе) права rwx.
stat.S_IROTH - Другие имеют разрешение на чтение.
stat.S_IWOTH - Другие имеют разрешение на запись.
stat.S_IXOTH - Другие имеют разрешение на исполнение.
"""
# Эта функция может поддерживать указание дескриптора файла, пути относительно
# дескриптора каталога и не следовать символическим ссылкам.
#       Внимание
#    Хотя Windows поддерживает chmod(), вы можете только установить с его помощью флаг
#    файла только для чтения (через константы stat.S_IWRITE и stat.S_IREAD или
#    соответствующее целочисленное значение). Все остальные биты игнорируются.
# Эта функция ограничена на Emscripten и WASI, см. Платформы WebAssembly для получения
# дополнительной информации.
# Вызывает событие аудита os.chmod с аргументами путь, режим, dir_fd.
# Новое в версии 3.3: добавлена поддержка указания пути в качестве дескриптора
# открытого файла, а также аргументов dir_fd и follow_symlinks.
# Изменено в версии 3.6: принимает объект, подобный пути.
# Параметры:
#     path - str путь в файловой системе,
#     mode - режим доступа,
#     dir_fd=None - путь относительно дескриптор каталога,
#     follow_symlinks=True - bool, переходить ли по ссылкам.
#                       (follow symlinks - следование символическим ссылкам)
#
# Возвращаемое значение:
#     None
# Описание:
# Функция chmod() модуля os изменяет режим доступа к файлу или директории,
# указанного в path.

"""os.lchmod(path, mode)"""
# Функция os.lchmod() эквивалентна вызову функции со следующими установленными
# аргументами os.chmod(path, mode, follow_symlinks=False).
# Аргумент mode может принимать последние 3 цифры восьмеричного представления числа,
# например 0o755 или одно или несколько из следующих значений, значения которых
# приведены в модуле stat:

# Приведенные выше значения можно комбинировать побитовым ИЛИ '|', например
# stat.S_IRWXU|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH. Данная комбинация установит
# разрешение rwxr-xr-- для пути, указанного в path.
# Аргумент path может принимать объекты, представляющие путь файловой системы, такие
# как pathlib.PurePath.
# Функция chmod() может поддерживать указание дескриптора файла, пути относительно
# дескрипторов каталога и не следовать символическим ссылкам follow_symlinks=False.
# Примечание. Несмотря на то, что Windows поддерживает os.chmod(), можно установить
# для него флаг только для чтения через константы stat.S_IWRITE и stat.S_IREAD или
# соответствующее целочисленное значение. Все остальные биты игнорируются.
# Вызывает событие аудита os.chmod с аргументами path, mode, dir_fd.
import os
import stat

print("-----1--'walk.py'------------------------------------------")
# f = 'walk.py'
f = '(l)chmod.py'
st = os.stat(f).st_mode
print(stat.filemode(st))
# '-rw-rw-r--'

os.chmod(f, 0o754)
st = os.stat(f).st_mode
print(stat.filemode(st))
# '-rwxr-xr--'

print("-----2---'tt.txt'-----------------------------------------")
filename = 'tt.txt'
if os.path.exists(filename):
    os.unlink(filename)
with open(filename, 'wt') as f:
    f.write('contents')

# Определим установленные разрешения
existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)

if not os.access(filename, os.X_OK):
    print('Добавим разрешение на запуск "x"')
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Удалим разрешения на выполнение "x"')
    # use xor to remove the user execute permission
    new_permissions = existing_permissions ^ stat.S_IXUSR

os.chmod(filename, new_permissions)

print("-----3--------------------------------------------")
# Set given file read by the owner. (Установить данный файл для чтения владельцем)
os.chmod("tt.txt", stat.S_IREAD)
print("File can be read only by owner.")
# Файл может быть прочитан только владельцем.

# Set given file read by others. (Установить данный файл для чтения другими)
os.chmod("tt.txt", stat.S_IROTH)
print("File access changed, can be read by others now.")
# Доступ к файлу изменен, теперь его могут читать другие

# print("-----4--------------------------------------------")
path = 'chown.py'
print("\nOwner id of the file:", os.stat(path).st_uid)
print("Group id of the file:", os.stat(path).st_gid)
# os.chmod(path, stat.S_IRWXU)
