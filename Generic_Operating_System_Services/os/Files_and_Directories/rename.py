""" os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)"""
# Параметры:
#     src - str, исходное имя файла или каталога,
#     dst - str, новое имя файла или каталога,
#     src_dir_fd=None - int, исходный дескриптор каталога,
#     dst_dir_fd=None - int, новый дескриптор каталога.
# Переименуйте файл или каталог src в dst. Если dst существует, операция завершится
# ошибкой с подклассом OSError в ряде случаев:
#      В Windows, если dst существует, всегда возникает FileExistsError.
# В Unix, если src является файлом, а dst — каталогом или наоборот, соответственно будет
# вызвано сообщение об ошибке IsADirectoryError или NotADirectoryError. Если оба являются
# каталогами и dst пуст, dst будет заменен молча. Если dst является непустым каталогом,
# возникает ошибка OSError. Если оба являются файлами, dst будет автоматически заменен,
# если у пользователя есть разрешение. Операция может завершиться ошибкой в некоторых
# разновидностях Unix, если src и dst находятся в разных файловых системах. В случае
# успеха переименование будет атомарной операцией (это требование POSIX).
# Эта функция может поддерживать указание src_dir_fd и/или dst_dir_fd для предоставления
# путей относительно дескрипторов каталогов.
#      Если вы хотите кросс-платформенную перезапись адресата, используйте replace().
#      Вызывает событие аудита os.rename с аргументами src, dst, src_dir_fd, dst_dir_fd.
#      Новое в версии 3.3: Аргументы src_dir_fd и dst_dir_fd.
#      Изменено в версии 3.6: принимает объект  path-like object (подобный пути), для src и dst.

import os
src_dir, dst_dir = 'test_dir', 'rename_dir'
os.mkdir(src_dir, 0o774)
print('src_dir:', os.path.isdir(src_dir), '  dst_dir:', os.path.isdir(dst_dir))
os.rename(src_dir, dst_dir)
print('src_dir:', os.path.isdir(src_dir), ' dst_dir:', os.path.isdir(dst_dir))
os.rmdir(dst_dir)
print('src_dir:', os.path.isdir(src_dir), ' dst_dir:', os.path.isdir(dst_dir))

print('-----------------------------------------------------')
src_f, dst_f = 'test_file.txt', 'rename_file.txt'
fp = open(src_f, 'w')
print('src_f:', os.path.isfile(src_f), '  dst_f:', os.path.isfile(dst_f))
fp.write('data string')
fp.close()
os.rename(src_f, dst_f)
print('src_f:', os.path.isfile(src_f), '  dst_f:', os.path.isfile(dst_f))
os.unlink(dst_f)
print('src_f:', os.path.isfile(src_f), '  dst_f:', os.path.isfile(dst_f))
