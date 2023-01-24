"""os.getrandom(size, flags=0)"""
# Получить до size случайных байт. Функция может вернуть меньше байтов, чем запрошено.
# Эти байты могут использоваться для заполнения генераторов случайных чисел
# пользовательского пространства или для криптографических целей.
# getrandom() полагается на энтропию, полученную от драйверов устройств и других
# источников шума окружающей среды. Излишнее чтение больших объемов данных окажет
# негативное влияние на других пользователей устройств /dev/random и /dev/urandom.
# Аргумент flags представляет собой битовую маску, которая может содержать ноль или
# более следующих значений, объединенных ИЛИ: os.GRND_RANDOM и GRND_NONBLOCK.
#     Также Страница руководства Linux getrandom().
#     Доступность: Linux 3.17 и новее.
#     Добавлено в версии 3.6.

"""os.GRND_NONBLOCK"""
#     По умолчанию при чтении из /dev/random getrandom() блокируется, если случайные
# байты недоступны, а при чтении из /dev/urandom он блокируется, если пул энтропии
# еще не инициализирован.
#     Если установлен флаг GRND_NONBLOCK, то getrandom() не блокируется в этих случаях,
# а вместо этого немедленно вызывает BlockingIOError.
#     Добавлено в версии 3.6.

""" os.GRND_RANDOM"""
#      Если этот бит установлен, то случайные байты берутся из пула /dev/random
# вместо пула /dev/urandom.
#      Добавлено в версии 3.6.

import os
print("------os.GRND_RANDOM------------------------------")
# Declaring size (Объявление размера)
size = 5

# Using os.getrandom() method
# Using os.GRND_NONBLOCK flag
result = os.getrandom(size, os.GRND_RANDOM)

# Print the random bytes string (Напечатать случайную строку байтов)
# Output will be different everytime (Вывод каждый раз будет разным)
print(result)

print("\n------os.GRND_NONBLOCK----------------------------")

# Declaring size (Объявление размера)
size = 5
# Using os.getrandom() method
# Using os.GRND_NONBLOCK flag
result = os.getrandom(size, os.GRND_NONBLOCK)
# Print the random bytes string (Напечатать случайную строку байтов)
# Output will be different everytime (Вывод каждый раз будет разным)
print(result)




