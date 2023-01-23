"""os.fork()"""  # разветвление, вилка
# Разветвите дочерний процесс. Возвращает 0 в дочернем и идентификатор дочернего процесса
# в родительском. При возникновении ошибки возникает ошибка OSError.
# Обратите внимание, что некоторые платформы, включая FreeBSD <= 6.3 и Cygwin, имеют
# известные проблемы при использовании fork() из потока.
#      Вызывает событие аудита os.fork без аргументов.
#      Изменено в версии 3.8: Вызов fork() в субинтерпретаторе больше не поддерживается (возникает RuntimeError).
#      Предупреждение
#      См. ssl для приложений, использующих модуль SSL с fork().
#      Доступность: Unix, не Emscripten, не WASI.
import os
pid = os.fork()  # Создайте дочерний процесс, используя метод os.fork()
print("      pid =", pid)
if pid:
    print("I am parent process:")
    print("Process ID:", os.getpid())
    print("Child's process ID:", pid)
# pid, равный 0, представляет созданный дочерний процесс
else:
    print("\nI am child process:")
    print("Process ID:", os.getpid())
    print("Parent's process ID:", os.getppid())
# Если при использовании метода os.fork() возникла какая-либо ошибка,
# OSError будет поднят.
