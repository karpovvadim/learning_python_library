"""os.WEXITSTATUS(status)"""
# Вернуть статус завершения процесса.
#      Эту функцию следует использовать, только если WIFEXITED() имеет значение true.
#      Доступность: Unix, не Emscripten, не WASI.
import os

pid = os.fork()
if pid:
    pid2 = os.fork()
    if pid2:
        info1 = os.waitpid(pid, 0)  # возвращает первый атрибут кортежа, представляющий дочерний
        # pid, а второй представляет индикацию статуса выхода.
        
        # Дождитесь завершения второго дочернего процесса и получите его pid и
        # индикацию статуса выхода, используя метод os.waitpid().
        info2 = os.waitpid(pid2, 0)
        print("\nIn parent process")
        # Проверьте, вышел ли первый дочерний элемент с помощью системного вызова exit(2)
        # с помощью метода os.WIFEXITED()
        if os.WIFEXITED(info1[1]):
            code = os.WEXITSTATUS(info1[1])
            print("First child's exit code:", code)
        else:
            print("First child does not exited using exit(2) system call.")

        if os.WIFEXITED(info2[1]):
            code = os.WEXITSTATUS(info2[1])
            print("\nSecond child's exit code:", code)
        else:
            print("Second child does not exited using exit(2) system call.")

    else:
        print("\nIn second child process Process ID:", os.getpid())
        print("Hey ! there")
        print("Second child aborted")
        os.abort()  # Метод os.abort() будет генерировать сигнал SIGABRT для текущего
        # процесса и создаст дамп ядра.
else:
    print("\nIn first child process Process ID:", os.getpid())
    print("Hello World!")
    print("First child exiting..")

    # Exit using exit(2) system call (Выход с помощью системного вызова exit(2))
    os._exit(5)
