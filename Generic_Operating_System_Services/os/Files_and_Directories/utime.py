"""os.utime(path, times=None, *, [ns, ]dir_fd=None, follow_symlinks=True)"""
# Установите время доступа и изменения файла, указанного путем.
# utime() принимает два необязательных параметра, times и ns. Они определяют время,
# установленное на пути, и используются следующим образом:
#         Если указан ns, это должен быть кортеж из двух форм (atime_ns, mtime_ns), где
#         каждый элемент представляет собой целое число, выражающее наносекунды.
#         Если значение times не равно None, оно должно быть кортежем из двух форм
#         (atime, mtime), где каждый элемент представляет собой целое или число с
#         плавающей запятой, выражающее секунды.
#         Если значение times равно None, а ns не указано, это эквивалентно указанию
#         ns=(atime_ns, mtime_ns), где оба времени являются текущим временем.
# Ошибка указывать кортежи как для времени, так и для ns.
# Обратите внимание, что точное время, установленное здесь, может не быть возвращено
# последующим вызовом stat(), в зависимости от разрешения, с которым ваша операционная
# система записывает время доступа и модификации; см. статистику(). Лучший способ
# сохранить точное время — использовать поля st_atime_ns и st_mtime_ns из объекта
# результата os.stat() с параметром ns для utime().
# Эта функция может поддерживать указание дескриптора файла, пути относительно
# дескриптора каталога и не следовать символическим ссылкам.
#     Вызывает событие аудита os.utime с аргументами path, times, ns, dir_fd.
#     Новое в версии 3.3: добавлена поддержка указания пути в качестве дескриптора
#     открытого файла, а также параметров dir_fd, follow_symlinks и ns.
#     Изменено в версии 3.6: принимает объект, подобный пути.
import os
import time
f = 'test_utime.txt'
fp = open(f, 'w')
fp.write('content')
fp.close()
atime = os.stat(f).st_atime
mtime = os.stat(f).st_mtime
print(time.ctime(atime), '<---->', time.ctime(mtime))

# изменим время
delta = 60*60*24*15
new_atime = atime - delta
new_mtime = mtime - delta
os.utime(f, times=(new_atime, new_mtime))
atime = os.stat(f).st_atime
mtime = os.stat(f).st_mtime
print(time.ctime(atime), '<---->', time.ctime(mtime))
# Очистка
os.unlink(f)

print('----------------------------------------------------------------')
path = 'test_utime2.txt'
fp = open(path, 'w')
# Распечатать текущий доступ и время модификации указанного выше пути
print("Current access time:", os.stat(path).st_atime)
print("Current modification time:", os.stat(path).st_mtime)
atime = 200000000  # Access time in seconds (Время доступа в секундах)
mtime = 100000000  # Modification time in seconds (Время модификации в секундах)
# Установить время доступа и время модификации для указанного выше пути.
tup = (atime, mtime)
os.utime(path, tup)
print("\nAccess and modification time changed\n")
print("Current access time:", os.stat(path).st_atime)
print("Current modification time:", os.stat(path).st_mtime)
os.unlink(path)

print('---------- If ns parameter is specified-------------')
path2 = 'test_utime3.txt'
file = open(path2, 'w')
# Распечатать текущий доступ и время модификации указанного выше пути
print("Current access time:", os.stat(path2).st_atime)
print("Current modification time:", os.stat(path2).st_mtime)
atime_ns = 20000000012345  # Access time in seconds (Время доступа в наносекундах)
mtime_ns = 10000000012345  # Modification time in seconds (Время модификации в наносекундах)
# Установить время доступа и время модификации для указанного выше пути.
tup = (atime_ns, mtime_ns)
os.utime(path2, ns=tup)
print("\nAccess and modification time changed\n")
print("Current access time:", os.stat(path2).st_atime)
print("Current modification time:", os.stat(path2).st_mtime)

print('-----If times parameter is None and ns parameter is unspecified------')
path2 = 'test_utime3.txt'
# Распечатать текущий доступ и время модификации указанного выше пути
print("Current access time:", os.stat(path2).st_atime)
print("Current modification time:", os.stat(path2).st_mtime)

os.utime(path2)
print("\nAccess and modification time changed\n")
print("Current access time:", os.stat(path2).st_atime)
print("Current modification time:", os.stat(path2).st_mtime)
os.unlink(path2)
