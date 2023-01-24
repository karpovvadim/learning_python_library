""" os.getenv(key, default=None)"""
# Возвращает значение ключа переменной среды в виде строки, если она существует,
# или по умолчанию, если ее нет. key представляет собой строку. Обратите внимание,
# что поскольку getenv() использует os.environ, сопоставление getenv() также
# фиксируется при импорте, и функция может не отражать будущие изменения среды.
# В Unix ключи и значения декодируются с помощью sys.getfilesystemencoding() и
# обработчика ошибок 'surrogateescape'. Используйте os.getenvb(), если вы хотите
# использовать другую кодировку.
# Доступность: Unix, Windows.
import os

print(os.environ['HOME'])
print(os.getenv('HOME'))
print(os.getenv('TEST_ENV', '/tmp'))

"""os.getenvb(key, default=None)"""
# Функция os.getenvb() возвращает значение ключа key переменной среды, если оно
# существует или значение по умолчанию default, если его нет. Значения key, default
# и возвращаемый результат - байтовые строки bytes.
# Функция os.getenvb() доступна только в том случае, если os.support_bytes_environ
# равно True.
# Доступность: большинство Unix.
print("\nos.getenvb :", os.getenvb(b'HOME'))
print("os.getenvb :", os.getenvb(b'TEST_ENV', b'/tmp'))
