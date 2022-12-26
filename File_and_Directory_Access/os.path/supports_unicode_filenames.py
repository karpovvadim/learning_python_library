"""os.path.supports_unicode_filenames"""
# Истинно, если в качестве имен файлов можно использовать произвольные строки Unicode
# (с ограничениями, налагаемыми файловой системой).
import os.path
print(os.path.supports_unicode_filenames)
