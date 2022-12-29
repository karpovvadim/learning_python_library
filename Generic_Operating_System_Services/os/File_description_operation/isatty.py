"""os.isatty(fd, /)"""
# Верните True, если файловый дескриптор fd открыт и подключен к tty-подобному
# устройству, иначе False.
import os

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, b"This is test")

# Now use isatty() to check the file.
ret = os.isatty(fd)

print("Returned value is: ", ret)

# Close opened file
os.close(fd)
