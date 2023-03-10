"""os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)"""
# Измените идентификатор владельца и группы пути на числовой uid и gid. Чтобы оставить
# один из идентификаторов без изменений, установите для него значение -1.
# Эта функция может поддерживать указание дескриптора файла, пути относительно
# дескриптора каталога и не следовать символическим ссылкам.
# См. Shutil.chown() для функции более высокого уровня, которая принимает имена в
# дополнение к числовым идентификаторам.
# Вызывает событие аудита os.chown с аргументами path, uid, gid, dir_fd.
#      Доступность: Юникс.
# Эта функция ограничена на Emscripten и WASI, см. Платформы WebAssembly для получения
# дополнительной информации.
# Новое в версии 3.3: добавлена поддержка указания пути в качестве дескриптора
# открытого файла, а также аргументов dir_fd и follow_symlinks.
# Изменено в версии 3.6: поддерживает объект, подобный пути.
# Смотрите функцию более высокого уровня shutil.chown() которая принимает имена
# пользователей и групп в дополнение к числовым идентификаторам.
# Вызывает событие аудита os.chown с аргументами path, uid, gid, dir_fd.
# Обе функции требуют привилегии суперпользователя root.
import os
path = 'tt.py'
open(path, 'w')
print(os.stat(path).st_uid)
print(os.stat(path).st_gid)
uid = 2000
gid = 2000
os.chown(path, uid, gid)
print("\nOwner and group id of the file changed")
