"""os.pipe2(flags)"""
# Создайте канал с флагами, установленными атомарно. флаги могут быть созданы путем
# объединения одного или нескольких из этих значений с помощью операции ИЛИ:
# O_NONBLOCK, O_CLOEXEC. Возвращает пару файловых дескрипторов (r, w), пригодных для
# чтения и записи соответственно.
#      Доступность: Unix, не Emscripten, не WASI.
#      Новое в версии 3.3.

import os
# Create a pipe with flag set automatically
# os.O_NONBLOCK flag tells that file descriptor is in non-blocking mode

# Создайте канал с автоматически установленным флагом.
# Флаг os.O_NONBLOCK сообщает, что файловый дескриптор находится в неблокирующем режим
flags = os.O_NONBLOCK
r, w = os.pipe2(flags)

# The returned file descriptor r and w can be used for reading and writing respectively.

# Возвращаемые файловые дескрипторы r и w можно использовать для чтения и записи
# соответственно.

# We will create a child process and using these file descriptor the parent process
# will write some text and child process will read the text written by the parent process

# Мы создадим дочерний процесс, и, используя этот файловый дескриптор, родительский
# процесс напишет некоторый текст, а дочерний процесс прочитает текст, написанный
# родительским процессом.

pid = os.fork()     # Create a child process
print("pid1:", pid)
# pid greater than 0 represents the parent process
# pid больше 0 представляет родительский процесс
if pid > 0:
    # This is the parent process
    # Closes file descriptor r (Закрывает файловый дескриптор r)
    os.close(r)

    # Write some text to file descriptor w (Напишите какой-нибудь текст в дескриптор файла w)
    print("Parent process is writing")
    text = b"Hello child process"
    os.write(w, text)
    print("Written text:", text.decode())    # Письменный текст
else:
    # This is the child process
    # Closes file descriptor w
    os.close(w)

    # Read the text written by parent process (Прочитать текст, написанный родительским процессом)
    print("\nChild Process is reading")
    r = os.fdopen(r)
    print("Read text:", r.read())   # Читать текст
