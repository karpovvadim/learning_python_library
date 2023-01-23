"""os.WIFCONTINUED(status)"""
# Возвратите True, если остановленный дочерний процесс был возобновлен доставкой
# SIGCONT (если процесс был продолжен после остановки управления заданием), в
# противном случае верните False.
#      См. вариант WCONTINUED.
#      Доступность: Unix, не Emscripten, не WASI.
import os
import signal

pid = os.fork()
if pid:
    # Отправьте сигнал «SIGSTOP» дочернему процессу с использованием сигнала
    # метода os.kill() «SIGCONT» приведет к остановке дочернего процесса.
    os.kill(pid, signal.SIGSTOP)
    # Отправьте сигнал «SIGCONT» дочернему процессу с помощью метода os.kill().
    # Сигнал SIGCONT приведет к продолжению дочернего процесса.
    os.kill(pid, signal.SIGCONT)
    info = os.waitpid(pid, os.WCONTINUED)  # Получите дочерний pid и код состояния
    print("\ninfo =", info)
    print("In parent process")
    continued = os.WIFCONTINUED(info[1])
    # Продолжен ли дочерний процесс после остановки управления заданиями?
    print("Has child process been continued from a job control stop? -", continued)
else:
    print("In Child process")
    print("Process ID:", os.getpid())
    print("Hello World!")
