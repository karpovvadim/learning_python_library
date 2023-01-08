"""os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)"""
# Создайте жесткую ссылку, указывающую на src с именем dst.
# Эта функция может поддерживать указание src_dir_fd и/или dst_dir_fd для предоставления
# путей относительно дескрипторов каталогов, а не следования символическим ссылкам.
#      Вызывает событие аудита os.link с аргументами src, dst, src_dir_fd, dst_dir_fd.
#      Доступность: Unix, Windows.
#      Изменено в версии 3.2: Добавлена поддержка Windows.
#      Новое в версии 3.3: добавлены аргументы src_dir_fd, dst_dir_fd и follow_symlinks.
#      Изменено в версии 3.6: принимает объект, подобный пути, для src и dst.
import os
src = 'tt.txt'
dst = 'tt_link.txt'  # Destination file path  (Путь к файлу назначения)
# Create a hard link pointing to src named dst using os.link() method
# Создайте жесткую ссылку, указывающую на src с именем dst, используя метод os.link().
os.link(src, dst)
print(os.path.isfile(dst))
print("Hard link created successfully")
