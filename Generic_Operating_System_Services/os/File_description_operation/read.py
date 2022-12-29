"""os.read(fd, n)"""
# Прочитать не более n байт из файлового дескриптора fd.
# Возвращает строку байтов, содержащую прочитанные байты. Если достигнут конец файла,
# на который указывает fd, возвращается пустой объект bytes.
#     Примечание
# Эта функция предназначена для низкоуровневого ввода-вывода и должна применяться к
# файловому дескриптору, возвращаемому функциями os.open() или pipe(). Чтобы прочитать
# «файловый объект», возвращаемый встроенной функцией open(), popen(), fdopen() или
# sys.stdin, используйте его методы read() или readline().
# Изменено в версии 3.5: если системный вызов прерывается, а обработчик сигнала не
# вызывает исключение, функция теперь повторяет системный вызов вместо создания
# исключения InterruptedError (обоснование см. в PEP 475).
import os

# File path
path = "Python_intro.txt"
# Open the file and get the file descriptor associated with it using os.open() method
# Откройте файл и получите связанный с ним файловый дескриптор, используя метод os.open().
fd = os.open(path, os.O_RDONLY)
# Number of bytes to be read
n = 60

# Read at most n bytes from file descriptor fd using os.read() method
# Прочитайте не более n байтов из файлового дескриптора fd, используя метод os.read()
readBytes = os.read(fd, n)
print(readBytes)   # Print the bytes read
os.close(fd)   # close the file descriptor
