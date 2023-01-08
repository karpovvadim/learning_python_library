"""os.major(device, /)"""
# Извлеките основной номер устройства из необработанного номера устройства (обычно
# это поле st_dev или st_rdev из stat).

import os
# Get the raw device number of a file (Получить необработанный номер устройства файла)
device = os.stat("tt.txt").st_dev
print("Raw device number:", device)  # Необработанный номер устройства
# Extract the device major number from the above raw device number (Извлеките
# основной номер устройства из приведенного выше необработанного номера устройства).
major = os.major(device)
print("Device major number:", major)  # Основной номер устройства
