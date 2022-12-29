"""os.dup2(fd, fd2, inheritable=True)"""
# Дублируйте файловый дескриптор fd в fd2, закрыв последний, если необходимо. Возврат fd2.
# Новый файловый дескриптор является наследуемым по умолчанию или ненаследуемым, если
# наследуемый имеет значение False.
# Наличие: не WASI.
# Изменено в версии 3.4: добавлен необязательный наследуемый параметр.
# Изменено в версии 3.7: Возврат fd2 в случае успеха. Ранее значение None всегда
# возвращалось.
import os

path = "file_3.txt"

# open the file and get
# the file descriptor associated
# with it using os.open() method
fd = os.open(path, os.O_WRONLY | os.O_CREAT)

# Print the value of
# file descriptor
print("Original file descriptor:", fd)

# Duplicate the file descriptor
# using os.dup2() method
dup_fd = 7
os.dup2(fd, dup_fd)

# The duplicate file descriptor
# will correspond to the same
# file to which original file
# descriptor was referring

# Print the value of
# duplicate file descriptor
print("Duplicated file descriptor:", dup_fd)

# Get the list of all
# file Descriptors Used
# by the current Process
# (Below code works on UNIX systems)
pid = os.getpid()
print("pid:", pid)
os.system("ls -l/proc/%s/fd" % pid)

# Close file descriptors
os.close(fd)
os.close(dup_fd)

print("File descriptor duplicated successfully")
