"""os.kill(pid, sig, /)"""
# Отправьте сигнал sig процессу pid. Константы для конкретных сигналов, доступных на
# хост-платформе, определяются в модуле signal.
# Windows: Сигналы signal.CTRL_C_EVENT и signal.CTRL_BREAK_EVENT — это специальные сигналы,
# которые могут быть отправлены только консольным процессам, которые совместно используют
# общее консольное окно, например, некоторые подпроцессы. Любое другое значение для sig
# вызовет безусловное уничтожение процесса API-интерфейсом TerminateProcess, а код
# выхода будет установлен на sig. Версия kill() для Windows дополнительно принимает
# дескрипторы процесса для уничтожения.
#      См. также signal.pthread_kill().
#      Вызывает событие аудита os.kill с аргументами pid, sig.
#      Доступность: Unix, Windows, не Emscripten, не WASI.
#      Новое в версии 3.2: поддержка Windows.
import os
import signal
pid = os.fork()  # Создайте дочерний процесс, используя метод os.fork()
if pid:
    print("\nIn parent process")
    # отправить сигнал «SIGSTOP» дочернему процессу, используя метод os.kill().
    # Сигнал «SIGSTOP» приведет к остановке процесса
    os.kill(pid, signal.SIGSTOP)
    print("Signal sent, child stopped.")  # Сигнал отправлен, дочерний элемент остановлен.

    info = os.waitpid(pid, os.WSTOPPED)
    # Метод waitpid() возвращает кортеж, первый атрибут которого представляет pid
    # дочернего элемента, а второй атрибут представляет собой индикацию состояния
    # дочернего элемента.

    # os.WSTOPSIG() возвращает номер сигнала, вызвавшего остановку процесса.
    stopSignal = os.WSTOPSIG(info[1])
    # Child остановился из-за отсутствия сигнала
    print("Child stopped due to signal no:", stopSignal)
    print("Signal name:", signal.Signals(stopSignal).name)

    # отправить сигнал «SIGCONT» дочернему процессу с использованием метода os.kill()
    # Сигнал «SIGCONT» приведет к продолжению процесса
    os.kill(pid, signal.SIGCONT)
    print("\nSignal sent, child continued.")  # Сигнал отправлен, child продолжил
else:
    print("\nIn child process")
    print("Process ID:", os.getpid())
    print("Hello World!")
    print("Exiting")


