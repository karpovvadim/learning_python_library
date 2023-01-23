"""os.WIFEXITED(status)"""
# Возвращает True, если процесс завершился нормально, то есть вызовом exit() или _exit(),
# или возвратом из main(); в противном случае вернуть False.
#       Доступность: Unix, не Emscripten, не WASI.
import os

pid = os.fork()
if pid:
    pid2 = os.fork()
    if pid2:
        info1 = os.waitpid(pid, 0)  # возвращает первый атрибут кортежа, представляющий дочерний
        info2 = os.waitpid(pid2, 0)  # pid, а второй представляет индикацию статуса выхода.
        print("\nIn parent process")
        # Проверьте, вышел ли первый дочерний элемент с помощью системного вызова exit(2)
        # с помощью метода os.WIFEXITED()
        if os.WIFEXITED(info1[1]):
            print("First child exited using exit(2) system call.")
        else:
            print("First child does not exited using exit(2) system call.")

        if os.WIFEXITED(info2[1]):
            print("Second child exited using exit(2) system call.")
        else:
            print("Second child does not exited using exit(2) system call.")

    else:
        print("\nIn second child process Process ID:", os.getpid())
        print("Hey ! there")
        print("Second child aborted")
        os.abort()  # Метод os.abort() будет генерировать сигнал SIGABRT для текущего процесса.

else:
    print("\nIn first child process Process ID:", os.getpid())
    print("Hello World!")
    print("First child exiting..")

    # Exit using exit(2) system call (Выход с помощью системного вызова exit(2))
    os._exit(5)
