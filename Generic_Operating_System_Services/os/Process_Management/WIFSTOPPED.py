"""os.WIFSTOPPED(status)"""
#      Возвращает True, если процесс был остановлен доставкой сигнала, в противном случае
# возвращает False.
#      WIFSTOPPED() возвращает True только в том случае, если вызов waitpid() был выполнен
# с использованием параметра WUNTRACED (ВЫПОЛНЕН) или когда процесс отслеживается (см. ptrace(2)).
#      Доступность: Unix, не Emscripten, не WASI.
import os
import signal
pid = os.fork()
if pid:
    # Отправьте сигнал «SIGSTOP» дочернему процессу с использованием сигнала
    # метода os.kill() «SIGCONT» приведет к остановке дочернего процесса.
    os.kill(pid, signal.SIGSTOP)
    info = os.waitpid(pid, os.WSTOPPED)  # Получите дочерний pid и код состояния
    print("\ninfo =", info)
    print("In parent process")
    # Проверьте, был ли остановлен дочерний процесс с помощью метода os.WIFSTOPPED().
    isStopped = os.WIFSTOPPED(info[1])
    print("Has child process been stopped? -", isStopped)  # Дочерний процесс был остановлен?
else :
    print("In Child process")
    print("Process ID:", os.getpid())
    print("Hello World!")
