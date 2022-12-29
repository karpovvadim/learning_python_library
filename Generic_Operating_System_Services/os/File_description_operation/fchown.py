"""os.fchown(fd, uid, gid)"""
# Измените владельца и идентификатор группы файла, заданного fd, на числовые uid и gid.
# Чтобы оставить один из идентификаторов без изменений, установите для него значение -1.
# См. chown(). Начиная с Python 3.3, это эквивалентно os.chown(fd, uid, gid).
# Вызывает событие аудита os.chown с аргументами path, uid, gid, dir_fd.
# Доступность: Юникс.
# Эта функция ограничена на Emscripten и WASI, см. Платформы WebAssembly для получения
# дополнительной информации.

import os

filename = "file.txt"

# Open the file and get the
# file descriptor associated
# with it using os.open() method
fd = os.open(filename, os.O_RDWR)

# Print the current owner id
# and group id of the file

# os.stat() method will return a
# 'stat_result’ object of
# ‘os.stat_result’ class whose
# 'st_uid' and 'st_gid' attributes
# will represent owner id and group id
# of the file respectively
print("Owner id of the file:", os.stat(fd).st_uid)
print("Group id of the file:", os.stat(fd).st_gid)

# Change the owner id and
# the group id of the file
# associated with the file descriptor
# using os.fchown() method
uid = 1000
gid = 1000
os.fchown(fd, uid, gid)
print("\nOwner and group id of the file changed")

# Print the owner id
# and group id of the file
print("\nOwner id of the file:", os.stat(fd).st_uid)
print("Group id of the file:", os.stat(fd).st_gid)

print("-------file_2.txt------------------------------")

filename = "file_2.txt"

# Open the file and get the
# file descriptor associated
# with it using os.open() method
fd = os.open(filename, os.O_RDWR)

# Print the current owner id
# and group id of the file

# os.stat() method will return a
# 'stat_result’ object of
# ‘os.stat_result’ class whose
# 'st_uid' and 'st_gid' attributes
# will represent owner id and group id
# of the file respectively
print("Owner id of the file:", os.stat(fd).st_uid)
print("Group id of the file:", os.stat(fd).st_gid)
# Change only group id of
# the file and leave owner id
# unchanged

# set id as -1 to leave
# it unchanged
uid = -1
gid = 1000
os.fchown(fd, uid, gid)
print("\ngroup id of the file changed")

# Print the owner id
# and group id of the file
print("\nOwner id of the file:", os.stat(fd).st_uid)
print("Group id of the file:", os.stat(fd).st_gid)
