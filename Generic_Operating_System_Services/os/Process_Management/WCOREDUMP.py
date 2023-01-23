"""os.WCOREDUMP(status, /)"""
# Верните True, если для процесса был создан дамп ядра, в противном случае верните False.
#      Эту функцию следует использовать, только если WIFSIGNALED() имеет значение true.
#      Доступность: Unix, не Emscripten, не WASI.
import os
pid = os.fork()  # Create a child process using os.fork() method
if pid:
    info = os.wait()  # Дождитесь завершения дочернего процесса и получить его pid и статус выхода
    print("\ninfo", info)
    print("In parent process")
    core_dump = os.WCOREDUMP(info[1])  # Check if core dump was generated for the child process
    print("Was core dump generated? -", core_dump)
else:
    print("In Child process")
    print("Process ID:", os.getpid())
    print("Hello World!")
    # Метод os.abort() будет генерировать сигнал SIGABRT для текущего процесса.
    os.abort()

print("\n----------------------------------------------------------")

pid = os.fork()
if pid:
    pid2 = os.fork()  # Create one more child
    if pid2:
        # Дождитесь завершения первого дочернего процесса и получите его
        # pid и индикацию статуса выхода, используя метод os.waitpid().
        child1_info = os.waitpid(pid, 0)
        # Wait for the completion of second child process and get its pid
        # and exit status indication using os.waitpid() method
        child2_info = os.waitpid(pid2, 0)  # child_info — это кортеж, где child_info[0]
        # представляет идентификатор ребенка child_info[1] представляет выходную статистику
        print("\nIn parent process")
        core_dump = os.WCOREDUMP(child1_info[1])
        print("Was core dump generated for first child process? -", core_dump)
        core_dump = os.WCOREDUMP(child2_info[1])
        print("\nWas core dump generated for second child process? - ", core_dump)
    else:
        print("\nIn second child process")
        print("Process id:", os.getpid())
        print("Hey ! there")
        print("Exiting")
else:
    print("In first child process")
    print("Process ID:", os.getpid())
    print("Hello World!")
    os.abort()
