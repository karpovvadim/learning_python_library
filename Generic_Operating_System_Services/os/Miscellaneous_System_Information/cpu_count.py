"""os.cpu_count()"""
# Возвращает количество процессоров в системе. Если не определено, возвращает None.
# Это число не эквивалентно количеству процессоров, которые может использовать текущий процесс.
# Количество используемых процессоров можно узнать с помощью len(os.sched_getaffinity(0))
#    Добавлено в версии 3.4.
import os
# Получите количество процессоров в системе, используя метод os.cpu_count()
cpuCount = os.cpu_count()
print("Number of CPUs in the system:", cpuCount)