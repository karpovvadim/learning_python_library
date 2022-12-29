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

# Open file
fd = os.open("f1.txt", os.O_RDWR | os.O_CREAT)

# Writing text
ret = os.write(fd, b"This is test")

# ret consists of number of bytes written to f1.txt
print("the number of bytes written: ")
print(ret)

print("written successfully")

# Close opened file
os.close(fd)
print("Closed the file successfully!!")
