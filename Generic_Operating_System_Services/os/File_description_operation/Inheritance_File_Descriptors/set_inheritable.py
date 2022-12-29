"""os.set_inheritable(fd, inheritable)"""
# Установите флаг «наследуемый» для указанного файлового дескриптора.
import os

path = "file.txt"

# Open the file and get
# the file descriptor associated
# with it using os.open() method
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# Print the current value of
# inheritable flag of the
# file descriptor fd using
# os.get_inheritable() method
print("Current value of inheritable flag:", os.get_inheritable(fd))

# Change the inheritable flag
# of the file descriptor fd
# using os.set_inheritable() method
inheritable = True
os.set_inheritable(fd, inheritable)
print("Inheritable flag modified")

# Print the modified value of
# inheritable flag of the
# file descriptor using
# os.get_inheritable() method
print("Current value of inheritable flag:", os.get_inheritable(fd))
