""""os.wait()"""
#      Дождитесь завершения дочернего процесса и верните кортеж, содержащий его pid и
# индикацию статуса выхода: 16-битное число, чей младший байт — это номер сигнала,
# который, убил процесс, а старший байт — статус выхода (если сигнал число равно нулю);
# старший бит младшего байта устанавливается, если был создан основной файл.
#      Если нет дочерних элементов, которых можно было бы ожидать, возникает
# ChildProcessError.
#      waitstatus_to_exitcode() можно использовать для преобразования статуса выхода в
# код выхода.
#      Доступность: Unix, не Emscripten, не WASI.
#      Смотрите также:
#      Другие функции wait*(), задокументированные ниже, могут использоваться для
# ожидания завершения определенного дочернего процесса и имеют больше параметров.
# waitpid() — единственная функция, доступная в Windows.
import os
pid = os.fork()
print("     pid =", pid)
if pid:
    print("1_Process ID:", os.getpid())
    status = os.wait()
    print("\nstatus:       ", status)
    print("\nIn parent process-")
    print("2_Process ID:", os.getpid())
    print("Terminated child's process id:", status[0])
    print("Signal number that killed the child process:", status[1])
else:
    print("In Child process-")
    print("3_Process ID:", os.getpid())
    print("Hello World!")
    print("Exiting")

# с помощью метода os.wait() Родительский процесс будет ждать завершения дочернего
# процесса и только после этого начнет свое выполнение
