"""os.abort()"""  # ПРЕРЫВАНИЕ
# Сгенерируйте сигнал SIGABRT для текущего процесса. В Unix по умолчанию создается дамп
# ядра; в Windows процесс немедленно возвращает код выхода 3. Имейте в виду, что вызов
# этой функции не вызовет обработчик сигналов Python, зарегистрированный для SIGABRT с
# помощью signal.signal().

import os
import signal
pid = os.fork()  # Создайте дочерний процесс, используя метод os.fork()
if pid > 0:
    print("\nIn Parent process")
    info = os.wait()
    print("info:", info)
    sig = os.WTERMSIG(info[1])
    print("Child exited due to signal no:", sig)  # Ребенок вышел из-за сигнала №: 6
    print("Signal name:", signal.Signals(sig).name)
else:
    print("In child process")
    print("Process ID:", os.getpid())
    print("Hello World!")

    os.abort()

print('-----------------------------------------------------------')
print("Hello World!")
os.abort()
print("This will not be printed")
# Process finished with exit code 134 (interrupted by signal 6: SIGABRT)
# Процесс завершен с кодом выхода 134 (прерыван сигналом 6: СИГНАЛ ПРЕРЫВАНИЯ)
