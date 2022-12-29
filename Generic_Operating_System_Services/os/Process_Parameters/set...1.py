import os               # Параметры процесса

"""os.setpgrp()"""
# Вызывает системный вызов setpgrp() или setpgrp(0, 0) в зависимости от того,
# какая версия реализована, если есть.
# Доступность: Unix.
os.setpgrp()
print(os.setpgrp())

"""os.setregid(rgid, egid)"""
# Устанавливает действительный rgid и эффективный egid ids текущего процесса.
print(os.setregid(1000, 1000))

"""os.setresgid(rgid, egid, sgid)"""
# Функции os.setresgid() устанавливает действительный rgid, эффективный egid и
# сохраненный sgid идентификаторы групп текущего процесса.
print(os.setresgid(1000, 1000, 1000))

"""os.setresuid(ruid, euid, suid)"""
# Функции os.setresuid() устанавливает действительный ruid, эффективный euid и
# сохраненный suid идентификаторы текущего процесса.
print(os.setresuid(1000, 1000, 1000))

"""os.setreuid(ruid, euid)"""
# Функции os.setreuid() устанавливает действительный ruid и эффективный euid
# идентификаторы пользователя текущего процесса.
print(os.setreuid(1000, 1000))

"""os.getsid(pid)"""
# Функции os.getsid() вызывает системный вызов getsid().
# Доступность: Unix.
print("os.getsid(0):", os.getsid(0))

"""os.setpgid(pid, pgrp)"""
# Функции os.setpgid() вызывает системный вызов setpgid(), чтобы установить идентификатор
# группы процессов для процесса с идентификатором pid для группы процессов с
# идентификатором pgrp.
# Доступность: Unix.
print(os.setpgid(0, 1655))

"""os.setsid()"""
# Функции os.setsid() вызывает системный вызов setsid().
print(os.setsid())

"""os.setuid(uid)"""
# Функции os.setuid() устанавливает идентификатор пользователя uid текущего процесса.
print(os.setuid(1000))

print("---------test-gid-uid.py-----------------------------------------")
TEST_GID = 1000
TEST_UID = 1000


def show_user_info():
    print(f'User (actual/effective): {os.getuid()}/{os.geteuid()}')
    print(f'Group (actual/effective): {os.getgid()}/{os.getegid()}')
    print('Actual Groups:', os.getgroups())


print('BEFORE CHANGE:')
show_user_info()
print()

try:
    os.setegid(TEST_GID)
except OSError:
    print('ERROR: Could not change effective group. '
          'Rerun as root.')
else:
    print('CHANGE GROUP:')
    show_user_info()
    print()

try:
    os.seteuid(TEST_UID)
except OSError:
    print('ERROR: Could not change effective user. '
          'Rerun as root.')
else:
    print('CHANGE USER:')
    show_user_info()
    print()

