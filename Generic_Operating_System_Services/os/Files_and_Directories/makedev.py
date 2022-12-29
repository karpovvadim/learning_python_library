"""os.makedev(major, minor, /)"""
# Составьте необработанный номер устройства из старшего и второстепенного номеров
# устройства.
import os

major = 8
minor = 8

# Compose raw device number from the above minor and major device number
# using os.makedev() method (Составьте необработанный номер устройства из указанных
# выше младшего и основного номеров устройств, используя метод os.makedev()).
raw_device = os.makedev(major, minor)
print("Composed raw device number(major = % d, minor = % d):" \
      % (major, minor), raw_device)  # Составленный необработанный номер устройства

major = 103
minor = 0

# Compose raw device number from the above minor and major device number
# using os.makedev() method
raw_device = os.makedev(major, minor)

print("Composed raw device number(major = % d, minor = % d):" \
      % (major, minor), raw_device)  # Составленный необработанный номер устройства
