"""os.supports_bytes_environ"""
# Истинно, если исходный тип среды ОС — байты (например, False в Windows).
# Новое в версии 3.2.
import os
# Check whether the native OS       Проверьте, родная ли ОС
# type of the environment is        тип окружения
# bytes or not                      байт или нет
isBytes = os.supports_bytes_environ
print(isBytes)
