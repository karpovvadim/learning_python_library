"""os.tcsetpgrp(fd, pg)"""
# Установите группу процессов, связанную с терминалом, заданным fd (дескриптор открытого
# файла, возвращаемый функцией os.open()), в pg.
#      Доступность: Unix, не WASI.

import os

# Showing current directory
print("Current working dir :%s" %os.getcwd())

# Changing dir to /dev/tty
fd = os.open("/dev/tty", os.O_RDONLY)

f = os.tcgetpgrp(fd)

# Showing the process group
print("the process group associated is: ")
print(f)

# Setting the process group
os.tcsetpgrp(fd, 2672)
print("done")

os.close(fd)
print("Closed the file successfully!!")
