"""os.sched_setaffinity(pid, mask, /)"""
# Ограничить процесс с PID pid (или текущим процессом, если он равен нулю) набором процессоров.
# mask — это итерация целых чисел, представляющая множество процессоров, которым должен
# быть ограничен процесс.
import os
# Получите количество процессоров в системе, используя метод os.cpu_count()
print("Number of CPUs:", os.cpu_count())

# Получите набор процессоров, на которых может выполняться вызывающий процесс,
# используя метод os.sched_getaffinity() 0, поскольку PID представляет вызывающий процесс
pid = 0
affinity = os.sched_getaffinity(pid)  # (сходство)
print("Process is eligible to run on:", affinity)  # Процесс может выполняться на сходстве

# Измените маску привязки ЦП вызывающего процесса с помощью метода os.sched_setaffinity().
# Ниже маска привязки ЦП ограничит процесс только этими 2 ЦП (0, 1), т.е.
# процесс может работать только на этих ЦП.
affinity_mask = {0, 1}
pid = 0
os.sched_setaffinity(0, affinity_mask)
print("CPU affinity mask is modified for process id % s" % pid)  # Маска сходства ЦП
# изменена для идентификатора процесса

# Теперь снова получите набор процессоров, на которых может выполняться вызывающий процесс.
pid = 0
affinity = os.sched_getaffinity(pid)
print("Now, process is eligible to run on:", affinity)  # Теперь процесс может быть запущен
