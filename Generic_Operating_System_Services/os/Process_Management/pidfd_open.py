"""os.pidfd_open(pid, flags=0)"""
# Возвращает файловый дескриптор, ссылающийся на pid процесса. Этот дескриптор можно
# использовать для выполнения управления процессами без гонок и сигналов. Аргумент flags
# предназначен для будущих расширений; в настоящее время значения флагов не определены.
#      См. справочную страницу pidfd_open(2) для более подробной информации.
#      Доступность: Linux >= 5.3
#      Новое в версии 3.9.
import os
# fork the current process
pid = os.fork()
# if child process is in execution (если дочерний процесс выполняется)
if pid:  # если pid, то дочерний процесс находится в процессе выполнения.
    pidfd = os.pidfd_open(pid)  # pidfd_open(pid) используется для получения дескриптора
    # файла для текущего процесса.
    print("Child Process,  pid =", pid)  # печатаем сообщение «Дочерний процесс».
# начинаем родительский раздел.
else:
    print("Parent Process, pid =", pid)  # печатаем сообщение «Родительский процесс».

