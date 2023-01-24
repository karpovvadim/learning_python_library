"""os.sched_get_priority_max(policy)"""
# Получите максимальное значение приоритета для политики.
# policy является одной из констант политики планирования, описанных выше.
import os

print("Below are the maximum priority value for different scheduling policy")
# Ниже приведены максимальные значения приоритета для различных политик планирования.

# Получить максимальное значение приоритета для политики планирования
# «первый пришел — первым обслужен». Константа os.SCHED_FIFO представляет политику
# планирования «первый пришел — первый обслужен».
priority_max = os.sched_get_priority_max(os.SCHED_FIFO)
print("First In First Out scheduling policy:", priority_max)

# Получите максимальное значение приоритета для политики циклического планирования.
# Константа os.SCHED_RR представляет политику циклического планирования.
priority_max = os.sched_get_priority_max(os.SCHED_RR)
print("Round-robin scheduling policy:", priority_max)

# Получите максимальное значение приоритета для политики планирования по умолчанию.
# Константа os.SCHED_OTHER представляет политику планирования по умолчанию.
priority_max = os.sched_get_priority_max(os.SCHED_OTHER)
print("Default scheduling policy.:", priority_max)

# Получите максимальное значение приоритета для политики планирования для фоновых задач
# с чрезвычайно низким приоритетом. Константа os.SCHED_IDLE представляет политику
# планирования для фоновых задач с чрезвычайно низким приоритетом.
priority_max = os.sched_get_priority_max(os.SCHED_IDLE)
print("Scheduling policy for extremely low priority background tasks:", priority_max)

# Получите максимальное значение приоритета для политики планирования для процессов
# с интенсивным использованием ЦП, который пытается сохранить интерактивность на
# остальной части компьютера.
# os.SCHED_BATCH представляет политику планирования для процессов с интенсивным
# использованием ЦП, который пытается сохранить интерактивность на остальной части компьютера.
priority_max = os.sched_get_priority_max(os.SCHED_BATCH)
print("Scheduling policy for CPU-intensive processes:", priority_max)