"""os.waitpid(pid, options, /)"""
#      Детали этой функции различаются в Unix и Windows.
#      В Unix: дождитесь завершения дочернего процесса, заданного идентификатором
# процесса pid, и верните кортеж, содержащий его идентификатор процесса и индикацию
# состояния выхода (закодированный как для ожидания()). На семантику вызова влияет
# значение целочисленных опций, которое должно быть равно 0 для нормальной работы.
#      Если pid больше 0, waitpid() запрашивает информацию о состоянии для этого
# конкретного процесса. Если pid равен 0, запрашивается статус любого дочернего элемента
# в группе процессов текущего процесса. Если pid равен -1, запрос относится к любому
# потомку текущего процесса. Если pid меньше -1, статус запрашивается для любого процесса
# в группе процессов -pid (абсолютное значение pid).
#      options представляет собой комбинацию флагов по ИЛИ. Если он содержит WNOHANG и
# в запрошенном состоянии нет соответствующих дочерних элементов, возвращается (0, 0).
# В противном случае, если нет подходящих дочерних элементов, которых можно было бы
# ожидать, возникает ChildProcessError. Другими вариантами, которые можно использовать,
# являются WUNTRACED и WCONTINUED.
#      В Windows: дождитесь завершения процесса, указанного дескриптором процесса pid,
# и верните кортеж, содержащий pid, и его статус выхода, сдвинутый влево на 8 бит
# (сдвиг упрощает межплатформенное использование функции). Значение pid, меньшее или
# равное 0, не имеет особого значения в Windows и вызывает исключение. Значение
# целочисленных опций не имеет значения. pid может относиться к любому процессу,
# идентификатор которого известен, не обязательно к дочернему процессу. Функции spawn*,
# вызываемые с помощью P_NOWAIT, возвращают подходящие дескрипторы процесса.
# waitstatus_to_exitcode() можно использовать для преобразования статуса выхода в код выхода.
#      Доступность: Unix, Windows, не Emscripten, не WASI.
#      Изменено в версии 3.5: если системный вызов прерывается, а обработчик сигнала
# не вызывает исключение, функция теперь повторяет системный вызов вместо создания
# исключения InterruptedError (обоснование см. в PEP 475).
import os
import sys
import time

pid = os.fork()
if pid:
    p_id = pid
    print("w_id =", pid)
    option_1 = os.WUNTRACED  # Specify option (Укажите вариант)
    option_2 = os.WCONTINUED
    print("option =", option_1)
    status = os.waitpid(p_id, option_2)
    print('++++++++++++++++++++++++++++++++++')
    print("Status of child process:", status)
else:
    print("In Child process-")
    print("Process ID:", os.getpid())
    print("Hello ! Geeks")
    print("Exiting..")

time.sleep(3)
print('------------------------------------------------------------------')
workers = []
for i in range(2):
    print(f'PARENT {os.getpid()}: Forking {i}')
    worker_pid = os.fork()
    if not worker_pid:
        print(f'WORKER {i}: Starting')
        time.sleep(2 + i)
        print(f'WORKER {i}: Finishing')
        sys.exit(i)
    workers.append(worker_pid)

for pid in workers:
    print(f'PARENT: Waiting for {pid}')
    done = os.waitpid(pid, 0)
    print(f'PARENT: Child done: {done}')
