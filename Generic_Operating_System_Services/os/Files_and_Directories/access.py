"""os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)"""
# Используйте настоящий uid/gid для проверки доступа к пути. Обратите внимание, что в
# большинстве операций будет использоваться эффективный uid/gid, поэтому эту процедуру
# можно использовать в среде suid/sgid для проверки наличия у вызывающего пользователя
# указанного доступа к пути. mode (режим) должен быть F_OK, чтобы проверить существование
# пути, или это может быть включающее ИЛИ одного или нескольких из R_OK, W_OK и X_OK для
# проверки разрешений. Возвращает True, если доступ разрешен, False, если нет.
# См. man-страницу Unix access(2) для получения дополнительной информации.
# Эта функция может поддерживать указание путей относительно дескрипторов каталогов, а
# не по символическим ссылкам.
# Если Effective_ids равно True, access() будет выполнять проверки доступа, используя
# эффективный uid/gid вместо реального uid/gid. Effective_ids может не поддерживаться на
# вашей платформе; вы можете проверить, доступен ли он, используя
# os.supports_efficient_ids. Если он недоступен, его использование вызовет
# NotImplementedError.
# Запись
# Использование access() для проверки, авторизован ли пользователь, например. открыть
# файл перед тем, как это сделать, с помощью open() создает брешь в безопасности,
# потому что пользователь может использовать короткий интервал времени между проверкой и
# открытием файла, чтобы манипулировать им. Предпочтительнее использовать методы EAFP.
# Например:
import os
"""
if os.access("myfile.txt", os.R_OK):
    with open("myfile.txt") as fp:
        return fp.read()
return "some default data"

# is better written as: (лучше записать так:)

try:
    fp = open("1_overview.txt")
except PermissionError:
    return "some default data"
else:
    with fp:
        return fp.read()
"""
# Запись
# Операции ввода-вывода могут завершиться неудачно, даже если access() указывает, что
# они будут успешными, особенно для операций в сетевых файловых системах, которые могут
# иметь семантику разрешений, выходящую за рамки обычной модели битов разрешений POSIX.
# Изменено в версии 3.3: Добавлены параметры dir_fd, Effective_ids и Follow_symlinks.
# Изменено в версии 3.6: принимает объект, подобный пути.

print('Testing:', __file__)
print('Exists:', os.access(__file__, os.F_OK))       # Существует
print('Readable:', os.access(__file__, os.R_OK))     # Читаемый
print('Writable:', os.access(__file__, os.W_OK))     # Доступно для записи
print('Executable:', os.access(__file__, os.X_OK))   # Исполняемый
print("----------------------------------------------------")

# Different mode parameters will return True if access is allowed, else returns False.
# Assuming only read operation is allowed on file.

# Различные параметры режима возвращают значение True, если доступ разрешен,
# в противном случае возвращается значение False.
# Предполагая, что в файле разрешена только операция чтения.

path1 = os.access("file2.txt", os.F_OK)  # Checking access with os.F_OK
print("Exists the path:", path1)

path2 = os.access("file2.txt", os.R_OK)  # Checking access with os.R_OK
print("Access to read the file:", path2)

path3 = os.access("file2.txt", os.W_OK)  # Checking access with os.W_OK
print("Access to write the file:", path3)

path4 = os.access("file2.txt", os.X_OK)  # Checking access with os.X_OK
print("Check if path can be executed:", path4)  # Проверить, может ли путь быть выполнен

"""
os.F_OK - проверка существования файла или каталога,
os.R_OK - проверка возможности чтения,
os.W_OK - проверка возможности записи,
os.X_OK - проверка выполнения файла или открытия директории
"""
