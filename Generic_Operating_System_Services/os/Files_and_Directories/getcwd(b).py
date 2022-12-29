"""os.getcwd()"""
# Функция getcwd() модуля os вернет строку, представляющую текущий рабочий каталог
import os
import stat

print(os.getcwd())

# Функция getcwdb() вернет строку байтов, представляющую текущий рабочий каталог.

print(os.getcwdb())
print("----------для (l)chmod.py----------------------------")
f = '(l)chmod.py'
st = os.stat(f).st_mode
print(stat.filemode(st))
os.chmod(f, 0o754)
st = os.stat(f).st_mode
print(stat.filemode(st))

print("----------для chown.py---------------------------------------")
f = 'chown.py'
st = os.stat(f).st_mode
print(stat.filemode(st))
os.chmod(f, 0o754)
st = os.stat(f).st_mode
print(stat.filemode(st))
