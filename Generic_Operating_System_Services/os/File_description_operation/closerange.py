"""os.closerange(fd_low, fd_high)"""
# Закрыть все файловые дескрипторы от fd_low (включительно) до fd_high (эксклюзивно),
# игнорируя ошибки.
# Эквивалентно (но намного быстрее):
import os
fd_low = 3
fd_high = 6
for fd in range(fd_low, fd_high+1):
    try:
        os.close(fd)
    except OSError:
        pass