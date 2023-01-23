"""os.WIFSIGNALED(status)"""
# Возвращает True, если процесс был прерван сигналом, в противном случае возвращает False.
#      Доступность: Unix, не Emscripten, не WASI.
import os
import signal
#
# pid = os.fork()  # Create a child process using os.fork() method
# if pid:
#     info = os.wait()  # Дождитесь завершения дочернего процесса и получить его pid и статус выхода
#     print("\ninfo =", info)
#     print("In parent process")
#     signaled = os.WIFSIGNALED(info[1])  # Check whether the child process exited due to a signal
#     print("Child process exited due a signal? -", signaled)  # Дочерний процесс завершился
#     # из-за сигнала?
# else:
#     print("In Child process")
#     print("Process ID:", os.getpid())
#     print("Hello World!")
#     # Метод os.abort() будет генерировать сигнал SIGABRT для текущего процесса.
#     os.abort()

print("\n----------------------------------------------------------")

pid = os.fork()
if pid:
    pid2 = os.fork()  # Create one more child
    if pid2:
        # Дождитесь завершения первого дочернего процесса и получите его
        # pid и индикацию статуса выхода, используя метод os.waitpid().
        child1_info = os.waitpid(pid, 0)
        # Отправьте сигнал «SIGKILL» второму дочернему процессу с помощью метода os.kill() и
        # получите его pid и код состояния выхода с помощью метода os.waitpid()
        os.kill(pid2, signal.SIGKILL)
        child2_info = os.waitpid(pid2, 0)  # child_info — это кортеж, где child_info[0]
        # представляет идентификатор ребенка child_info[1] представляет выходную статистику
        print("\nIn parent process")
        # Проверьте, завершился ли первый дочерний процесс из-за сигнала
        isSignaled = os.WIFSIGNALED(child1_info[1])
        print("First child process exited due to a signal? -", isSignaled)
        # Check whether the second child process exited due a signal
        isSignaled = os.WIFSIGNALED(child2_info[1])
        print("Second child process exited due to a signal? -", isSignaled)

    else:
        print("\nIn second child process")
        print("Process id:", os.getpid())
        print("Hey ! there")
        while True:
            print("Waiting for signal..")
else:
    print("In first child process")
    print("Process ID:", os.getpid())
    print("Hello World!")
    print("Exiting")
