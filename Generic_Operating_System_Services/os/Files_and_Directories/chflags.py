""" os.chflags(path, flags, *, follow_symlinks=True)"""
# Установите флаги path (пути) на числовые flags (флаги). flags может принимать комбинацию
# (побитовое ИЛИ) следующих значений (как определено в модуле stat):
# метод в Python, используемый для установки флагов пути к числовым флагам; доступен
# только в Unix. Флаги могут принимать комбинацию (побитовое ИЛИ) значений флагов.

"""
    stat.UF_NODUMP          Не сбрасывайте файл.
    stat.UF_IMMUTABLE       Файл нельзя изменить.
    stat.UF_APPEND          Файл может быть добавлен только к .
    stat.UF_OPAQUE          Каталог непрозрачен при просмотре через стек объединения.
    stat.UF_NOUNLINK        Файл нельзя переименовывать или удалять.
    stat.UF_COMPRESSED      Файл хранится в сжатом виде (macOS 10.6+).
    stat.UF_HIDDEN          Файл не должен отображаться в графическом интерфейсе (macOS 10.5+).
    stat.SF_ARCHIVED        Файл может быть заархивирован.
    stat.SF_IMMUTABLE       Файл нельзя изменить.
    stat.SF_APPEND          Файл может быть добавлен только к 
    stat.SF_NOUNLINK        Файл нельзя переименовывать или удалять.
    stat.SF_SNAPSHOT        Файл является файлом моментального снимка.
"""
# Эта функция может поддерживать not following symlinks (не следующие символические ссылки).
# (не переходить по символическим ссылкам: если для параметра follow_symlinks установлено
# значение False, а последним элементом пути для работы является символическая ссылка,
# функция будет работать с самой символической ссылкой, а не с файлом, на который указывает
# ссылка. (Для систем POSIX Python вызовет  l... вариант функции.)).
# Вызывает событие аудита os.chflags с аргументами path, flags.
# Доступность: Unix, не Emscripten, не WASI.
# Новое в версии 3.3: Аргумент follow_symlinks.
# Изменено в версии 3.6: принимает объект, подобный пути.

"""os.lchflags(path, flags)"""
# Установите флаги пути на числовые флаги, такие как chflags(), но не переходите по
# символическим ссылкам. Начиная с Python 3.3, это эквивалентно
# os.chflags(path, flags, follow_symlinks=False).
#      Вызывает событие аудита os.chflags с аргументами path, flags.
#      Доступность: Unix, не Emscripten, не WASI.
#      Изменено в версии 3.6: принимает объект, подобный пути.

import stat
import os
path = "tt.py"
flags = stat.SF_NOUNLINK
val = os.chflags(path, flags)
# Doesn't return any value, so nothing will be printed
# Не возвращает никакого значения, поэтому ничего не будет напечатано
print("Operation successful, returning value: %s" % val)
# Операция выполнена успешно, возвращаемое значение: None
