"""os.ttyname(fd)"""
# Возвращает строку, указывающую терминальное устройство, связанное с файловым
# дескриптором fd. Если fd не связан с терминальным устройством, возникает исключение.
#      Доступность: Юникс.
import os

# Showing current directory
print("Current working dir :%s" % os.getcwd())

# Changing dir to /dev/tty
fd = os.open("/dev/tty", os.O_RDONLY)

p = os.ttyname(fd)
print("the terminal device associated is: ")
print(p)
print("done!!")

os.close(fd)
print("Closed the file successfully!!")
