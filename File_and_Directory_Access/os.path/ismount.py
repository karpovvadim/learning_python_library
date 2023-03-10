"""os.path.ismount(path)"""    # монтировать
# Возвратите True, если pathname path является точкой монтирования: точкой в
# файловой системе, где была смонтирована другая файловая система.
# В POSIX функция проверяет, находится ли родитель пути, path/.., на другом
# устройстве, чем path, или указывают ли path/.. и path на один и тот же i-узел
# на одном и том же устройстве — это должно обнаруживать точки монтирования для
# всех Варианты Unix и POSIX. Он не может надежно обнаружить монтирование привязки
# в той же файловой системе.
# В Windows корневая буква диска и общий ресурс UNC всегда являются
# точками подключения, а для любого другого пути вызывается GetVolumePathName,
# чтобы проверить, отличается ли он от входного пути.
# Новое в версии 3.4: Поддержка обнаружения точек монтирования без полномочий
# root в Windows.
# Изменено в версии 3.6: принимает объект, подобный пути.
import os.path
print(os.path.ismount('/run'))
# True
print(os.path.ismount('/dev'))
# True
print(os.path.ismount('/home'))
# False
