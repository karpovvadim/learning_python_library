"""os.minor(device, /)"""
# Извлеките младший номер устройства из необработанного номера устройства (обычно это
# поле st_dev или st_rdev из stat).
import os
# Get the raw device number of the home directory (Получить необработанный
# номер устройства домашнего каталога)
device = os.stat("/home").st_dev
print("Raw device number:", device)  # необработанный номер устройства

# Extract the device minor number from the above raw device number (Извлеките
# второстепенный номер устройства из приведенного выше необработанного номера устройства).
minor = os.minor(device)
print("Device minor number:", minor)  # Второстепенный номер устройства
