"""os.tcgetpgrp(fd)"""
# Возвращает группу процессов, связанную с терминалом, заданным fd
# (дескриптор открытого файла, возвращаемый функцией os.open()).
#       Доступность: Unix, не WASI.
import os
# Get the/dev/tty file and get the file descriptor associated with it
# using os.open() method
# Получите файл /dev/tty и связанный с ним файловый дескриптор, используя метод os.open().

# '/dev / tty' is a special file which represents the controlling terminal of
# the current process
# '/dev/tty'– это специальный файл, представляющий управляющий терминал текущего процесса.
fd = os.open("/dev/tty", os.O_RDWR)

# Get the process group associated with the terminal given by the specified file
# descriptor using os.tcgetpgrp() method
# Получите группу процессов, связанную с терминалом, заданным указанным файловым
# дескриптором, используя метод os.tcgetpgrp().
pgid = os.tcgetpgrp(fd)

# Print the process group associated with the controlling terminal of the current process
# Вывести группу процессов, связанную с управляющим терминалом текущего процесса.
print("Process group associated with controlling\n "
      "terminal of the current process:", pgid)
# Close the file descriptor
os.close(fd)
"""
Output:

Process group associated with controlling
terminal of the current process: 19787

"""