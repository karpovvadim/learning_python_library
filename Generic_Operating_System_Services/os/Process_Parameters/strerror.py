"""os.strerror(code)"""  # Параметры процесса
# Вернуть сообщение об ошибке, соответствующее коду ошибки в code. На платформах,
# где функция strerror() возвращает NULL при получении неизвестного номера ошибки, в
# озникает ValueError.
import os
# получение сообщения об ошибке из кода ошибки
print(os.strerror(0))   # 'Success'
print(os.strerror(1))   # 'Operation not permitted'
print(os.strerror(19))  # 'No such device'
print(os.strerror(50))  # 'No CSI structure available'
print(os.strerror(19))  # 'No such device'
print(os.strerror(113))  #  'No route to host'
print(os.strerror(18))

