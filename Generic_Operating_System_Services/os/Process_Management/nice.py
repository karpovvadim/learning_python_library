"""os.nice(increment, /)"""
# Добавьте приращение к «приятности» процесса. Верните новую приятность.
#       Доступность: Unix, не Emscripten, не WASI.

import os
# Получить текущее значение nice процесса
niceValue = os.nice(0)
print("Current nice value of the process:", niceValue)
# Повысьте привлекательность процесса
value = 5
niceValue = os.nice(value)
print("\nNiceness of the process increased")
print("\nCurrent nice value of the process:", niceValue)
value = 10
niceValue = os.nice(value)
print("\nNiceness of the process increased")
print("\nCurrent nice value of the process:", niceValue)
value = 10
niceValue = os.nice(value)
print("\nNiceness of the process increased")  # Приятность процесса увеличилась
print("\nCurrent nice value of the process:", niceValue)
# Максимально возможное качество процесса может быть равно 19 поэтому если
# устанавливаемое качество превышает максимальный предел, тогда будет установлено
# максимально возможное качество, т.е. 19.

# Примечание.
# Только суперпользователь может уменьшить качество процесса, поэтому
# запускайте программу от имени суперпользователя, чтобы избежать ошибки, связанной с
# разрешениями.
value = -30
niceValue = os.nice(value)
print("\nNiceness of the process decreased")  # Приятности процесса стало меньше
print("\nCurrent nice value of the process:", niceValue)

# Минимально возможная приятность процесса может быть -20 поэтому если
# устанавливаемая приятность ниже минимального предела, тогда будет установлена
# минимально возможная приятность, т.е. -20.
