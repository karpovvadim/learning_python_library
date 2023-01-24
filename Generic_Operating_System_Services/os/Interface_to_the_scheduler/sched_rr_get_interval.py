"""os.sched_rr_get_interval(pid)"""
# Возвращает циклический такт в секундах для процесса с PID pid. 0 pid означает
# вызывающий процесс.
import os
# Получить квант времени циклического перебора текущего процесса. pid, равный 0,
# представляет вызывающий процесс.
pid = 0
quantum = os.sched_rr_get_interval(pid)
print("Round Robin time quantum (in seconds):", quantum) # циклический квант времени
