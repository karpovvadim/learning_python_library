"""os.openpty()"""
# Откройте новую пару псевдотерминалов. Возвращает пару файловых дескрипторов
# master and slave (главный, подчиненный) для pty и tty соответственно. Новые файловые
# дескрипторы не подлежат наследованию. Для (немного) более переносимого подхода
# используйте модуль pty.
#      Доступность: Unix, не Emscripten, не WASI.
#      Изменено в версии 3.4: новые файловые дескрипторы теперь не наследуются.
import os

# open new pseudo-terminal pair using os.openpty() method
# открыть новую пару псевдотерминалов, используя метод os.openpty()
master, slave = os.openpty()

# Get the terminal device name associated with file descriptor master
# Получить имя терминального устройства, связанное с мастером дескриптора файла
name = os.ttyname(master)
print(name)

# Get the terminal device name associated with file descriptor slave
# Получить имя терминального устройства, связанное с подчиненным файловым дескриптором
name = os.ttyname(slave)
print(name)
print("---------------------------------------")

m, s = os.openpty()

print(m)
print(s)

# showing terminal name (показывает имя терминала)
s = os.ttyname(s)
print(m)
print(s)
