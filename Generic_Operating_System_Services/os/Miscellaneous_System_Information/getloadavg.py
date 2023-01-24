"""os.getloadavg()"""
# Возвращает количество процессов в очереди запуска системы, усредненное за последние
# 1, 5 и 15 минут, или вызывает OSError, если средняя загрузка была недостижимой.
#     Доступность: Unix
import os
# Получите среднюю загрузку за последние 1, 5 и 15 минут, используя метод os.getloadavg().
load1, load5, load15 = os.getloadavg()
print("Load average over the last 1 minute:", load1)
print("Load average over the last 5 minute:", load5)
print("Load average over the last 15 minute:", load15)