"""os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)"""
# Переименуйте файл или каталог src в dst. Если dst является непустым каталогом, будет
# вызвана ошибка OSError. Если dst существует и является файлом, он будет автоматически
# заменен, если у пользователя есть разрешение. Операция может завершиться ошибкой,
# если src и dst находятся в разных файловых системах. В случае успеха переименование
# будет атомарной операцией (это требование POSIX).
# Эта функция может поддерживать указание src_dir_fd и/или dst_dir_fd для
# предоставления путей относительно дескрипторов каталогов.
# Вызывает событие аудита os.rename с аргументами src, dst, src_dir_fd, dst_dir_fd.
# New in version 3.3.
# Изменено в версии 3.6: принимает объект  path-like object (подобный пути), для src и dst.
import os
scr_dir, dst_dir = 'test_dir', 'rename_dir'
os.mkdir(scr_dir, 0o774)
print('scr_dir:', os.path.isdir(scr_dir), '  dst_dir:', os.path.isdir(dst_dir))
os.replace(scr_dir, dst_dir)
print('scr_dir:', os.path.isdir(scr_dir), ' dst_dir:', os.path.isdir(dst_dir))
os.rmdir(dst_dir)
print('scr_dir:', os.path.isdir(scr_dir), ' dst_dir:', os.path.isdir(dst_dir))
print('---------------------------------------------------------------------')
scr_f, dst_f = 'test_file.txt', 'rename_file.txt'
fp = open(scr_f, 'w')
print('scr_f:', os.path.isfile(scr_f), '   dst_f:', os.path.isfile(dst_f))
fp.write('data string')
fp.close()
os.replace(scr_f, dst_f)
print('scr_f:', os.path.isfile(scr_f), '  dst_f:', os.path.isfile(dst_f))
os.remove(dst_f)
print('scr_f:', os.path.isfile(scr_f), '  dst_f:', os.path.isfile(dst_f))
