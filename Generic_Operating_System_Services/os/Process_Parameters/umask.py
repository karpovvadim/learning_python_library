"""os.umask(mask)"""
# Установите текущую числовую маску umask и верните предыдущую маску umask.
# Эта функция представляет собой заглушку для Emscripten и WASI. Дополнительную информацию
# см. в разделе Платформы WebAssembly.
import os
# mask                              маска
# 18 in decimal is                  18 в десятичном виде
# equal to 0o022 in octal           равно 0o022 в восьмеричной системе
mask = 18
# Set the current umask value       Установить текущее значение umask
# and get the previous              и получить предыдущий
# umask value                       значение umask
umask = os.umask(mask)
# Print the                         Распечатать
# current and previous              текущий и предыдущий
# umask value                       значение umask
print("Current umask:", mask)
print("Previous umask:", umask)
