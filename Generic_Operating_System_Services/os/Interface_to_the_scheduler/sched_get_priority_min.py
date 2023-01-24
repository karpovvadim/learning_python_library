"""os.sched_get_priority_min(policy)"""
# Получите минимальное значение приоритета для политики.
# policy является одной из констант политики планирования, описанных выше.
import os

print("Below are the minimum priority value for different scheduling policy")
# Ниже приведены минимальные значения приоритета для различных политик планирования.

# Получить минимальное значение приоритета для политики планирования
# «первый пришел — первым обслужен». Константа os.SCHED_FIFO представляет политику
# планирования «первый пришел — первый обслужен».
priority_min = os.sched_get_priority_min(os.SCHED_FIFO)
print("First In First Out scheduling policy:", priority_min)  # Политика планирования
# «первым пришел – первым обслужен»

priority_min = os.sched_get_priority_min(os.SCHED_RR)
print("Round-robin scheduling policy:", priority_min)

priority_min = os.sched_get_priority_min(os.SCHED_OTHER)
print("Default scheduling policy:", priority_min)

priority_min = os.sched_get_priority_min(os.SCHED_IDLE)
print("Scheduling policy for extremely low priority background tasks:", priority_min)

priority_min = os.sched_get_priority_min(os.SCHED_BATCH)
print("Scheduling policy for CPU-intensive processes:", priority_min)
