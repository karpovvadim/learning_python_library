"""os.mknod(path, mode=0o600, device=0, *, dir_fd=None)"""
# Создайте узел файловой системы (файл, специальный файл устройства или именованный
# канал) с именем path. mode указывает как разрешения на использование, так и тип
# создаваемого узла, которые объединяются (побитовое ИЛИ) с одним из stat.S_IFREG,
# stat.S_IFCHR, stat.S_IFBLK и stat.S_IFIFO (эти константы доступны в stat).
# Для stat.S_IFCHR и stat.S_IFBLK устройство определяет только что созданный специальный
# файл устройства (вероятно, используя os.makedev()), в противном случае он игнорируется.
#     Эта функция также может поддерживать пути относительно дескрипторов каталогов.
#     Доступность: Unix, не Emscripten, не WASI.
#     Новое в версии 3.3: Аргумент dir_fd.
#     Изменено в версии 3.6: принимает объект, подобный пути.
import os
import stat
path = "filex.txt"
per = 0o600  # Permission to use (Разрешение на использование)
node_type = stat.S_IRUSR  # type of node to be created (тип создаваемого узла)
mode = per | node_type
# Create a file system node with specified permission and type using os.mknod() method
# Создайте узел файловой системы с указанным разрешением и типом, используя
# метод os.mknod()
os.mknod(path, mode)
print("Filesystem node is created successfully")
