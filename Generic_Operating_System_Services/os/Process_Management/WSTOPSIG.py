"""os.WSTOPSIG(status)"""
# Возвращает сигнал, вызвавший остановку процесса.
# Эту функцию следует использовать только в том случае, если WIFSTOPPED() имеет значение true.
#       Доступность: Unix, не Emscripten, не WASI.
import os
import signal
pid = os.fork()
if pid:  # pid больше 0 указывает на родительский процесс
    # Отправьте сигнал «SIGSTOP» дочернему процессу с использованием сигнала
    # метода os.kill() «SIGCONT» приведет к остановке дочернего процесса.
    os.kill(pid, signal.SIGSTOP)
    info = os.waitpid(pid, os.WSTOPPED)  # Получите дочерний pid и код состояния
    print("\ninfo =", info)
    print("\nIn parent process")
    # Получить номер сигнала, из-за которого остановился дочерний процесс,
    # используя метод os.WSTOPSIG()
    stopSignal = os.WSTOPSIG(info[1])
    print("Child stopped due to signal no:", stopSignal)  # остановился из-за отсутствия сигнала
    print("Signal name:", signal.Signals(stopSignal).name)
else:
    print("\nIn child process")
    print("Process ID:", os.getpid())
    print("Hello World!")
    print("Exiting")
