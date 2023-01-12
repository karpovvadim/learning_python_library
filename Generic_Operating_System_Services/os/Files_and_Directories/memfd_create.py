"""os.memfd_create(name[, flags=os.MFD_CLOEXEC])"""
# Создайте анонимный файл и верните дескриптор файла, который ссылается на него.
# flags должен быть одной из констант os.MFD_*, доступных в системе (или их комбинацией
# с побитовым ИЛИ). По умолчанию новый дескриптор файла не наследуется.
# Имя, указанное в name, используется в качестве имени файла и будет отображаться как
# цель соответствующей символической ссылки в каталоге /proc/self/fd/. Отображаемое имя
# всегда имеет префикс memfd: и служит только для целей отладки. Имена не влияют на
# поведение дескриптора файла, поэтому несколько файлов могут иметь одно и то же имя
# без каких-либо побочных эффектов.
#      Доступность: Linux >= 3.17 с glibc >= 2.27.
#      Новое в версии 3.8.

# os.MFD_CLOEXEC"""     - закрыть при выполнении
# os.MFD_ALLOW_SEALING  - РАЗРЕШАЕТ УПЛОТНЕНИЕ
# os.MFD_HUGETLB        - ОГРОМНЫЙ TLB
# os.MFD_HUGE_SHIFT     - ОГРОМНАЯ ПЕРЕМЕНА
# os.MFD_HUGE_MASK      - ОГРОМНАЯ МАСКА
# os.MFD_HUGE_64KB
# os.MFD_HUGE_512KB
# os.MFD_HUGE_1MB¶
# os.MFD_HUGE_2MB
# os.MFD_HUGE_8MB
# os.MFD_HUGE_16MB
# os.MFD_HUGE_32MB
# os.MFD_HUGE_256MB
# os.MFD_HUGE_512MB
# os.MFD_HUGE_1GB
# os.MFD_HUGE_2GB
# os.MFD_HUGE_16GB

# Эти флаги можно передать в memfd_create().
# Доступность: Linux >= 3.17 с glibc >= 2.27
# Флаги MFD_HUGE* доступны только начиная с Linux 4.14.
# Новое в версии 3.8.
import os
fd = os.memfd_create('test_file.txt')
print(fd)
s = os.write(fd, b'This is a test file\n')
print(type(s), "s =", s)
"""
nano /proc/[pid]/fd/[fd]
It automatically disappears if closed.
"""
os.lseek(fd, 0, os.SEEK_SET)
print(os.read(fd, 0x100))
b'This is a test file\nIt automatically disappears if closed.\n'
os.close(fd)


