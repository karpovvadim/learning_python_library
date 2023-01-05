"""os.write(fd, str)"""
# Запишите строку байтов в str в файловый дескриптор fd.
# Возвращает количество фактически записанных байтов.
#      Примечание
# Эта функция предназначена для низкоуровневого ввода-вывода и должна применяться к
# файловому дескриптору, возвращаемому функциями os.open() или pipe(). Чтобы записать
# «файловый объект», возвращаемый встроенной функцией open() или popen(), или fdopen(),
# или sys.stdout, или sys.stderr, используйте его метод write().
# Изменено в версии 3.5: если системный вызов прерывается, а обработчик сигнала
# не вызывает исключение, функция теперь повторяет системный вызов вместо создания
# исключения InterruptedError (обоснование см. в PEP 475).
import os
path = "f1.txt"
fd = os.open(path, os.O_RDWR | os.O_CREAT)
ret = os.write(fd, b"This is test")
# ret состоит из количества байтов, записанных в f1.txt
# ret consists of number of bytes written to f1.txt
print("the number of bytes written: ", ret)
print("written successfully")

# Close opened file
os.close(fd)
print("Closed the file successfully!!")
os.unlink(path)
