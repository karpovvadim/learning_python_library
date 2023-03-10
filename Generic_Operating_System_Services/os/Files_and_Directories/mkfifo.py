"""os.mkfifo(path, mode=0o666, *, dir_fd=None)"""
# Создайте именованный путь FIFO (именованный канал) в числовом режиме. Текущее
# значение umask сначала маскируется из режима.
# Эта функция также может поддерживать пути относительно дескрипторов каталогов.
# FIFO — это каналы, к которым можно обращаться как к обычным файлам. FIFO существуют
# до тех пор, пока они не будут удалены (например, с помощью os.unlink()). Как правило,
# FIFO используются как рандеву между процессами типа «клиент» и «сервер»: сервер
# открывает FIFO для чтения, а клиент открывает его для записи. Обратите внимание,
# что mkfifo() не открывает FIFO — она просто создает точку встречи.
#      Доступность: Unix, не Emscripten, не WASI.
#      Новое в версии 3.3: Аргумент dir_fd.
#      Изменено в версии 3.6: принимает объект, подобный пути.
import os
path = "./mypipe"
# Mode of the FIFO (a named pipe) to be created
# Режим создаваемого FIFO (именованного канала)
mode = 0o600
# Create a FIFO named path with the specified mode using os.mkfifo() method
# Создайте именованный путь FIFO с указанным режимом, используя метод os.mkfifo()
try:
    os.mkfifo(path, mode)
except OSError as error:
    print(error)
print("FIFO named '% s' is created successfully." % path)
print(os.path.exists('./mypipe'))


