"""os.WTERMSIG(status)"""
# Возвращает номер сигнала, вызвавшего завершение процесса.
#      Эту функцию следует использовать, только если WIFSIGNALED() имеет значение true.
#      Доступность: Unix, не Emscripten, не WASI.
import os
import signal

pid = os.fork()  # Create a child process using os.fork() method
if pid:
    info = os.wait()  # Дождитесь завершения дочернего процесса и получить его pid и статус выхода
    print("\ninfo =", info)
    print("In parent process")
    sig_num = os.WTERMSIG(info[1])  # Получить номер сигнала, который вызвал выход
    # дочернего процесса
    print("Child process exited due a signal no? -", sig_num)  # Дочерний процесс завершился
    # из-за отсутствия сигнала?

    # Мы можем получить имя сигнала, соответствующее номеру сигнала, следующим образом.
    print("Signal name:", signal.Signals(sig_num).name)
else:
    print("In Child process")
    print("Process ID:", os.getpid())
    print("Hello World!")
    # Метод os.abort() будет генерировать сигнал SIGABRT для текущего процесса
    os.abort()    # и создаст дамп ядра.
