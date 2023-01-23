"""os.wait3(options)"""
# Аналогично waitpid(), за исключением того, что аргумент идентификатора процесса не
# передается, и возвращается кортеж из 3 элементов, содержащий идентификатор дочернего
# процесса, индикацию статуса выхода и информацию об использовании ресурсов. Обратитесь к
# resource.getrusage() для получения подробной информации об использовании ресурсов.
# Аргумент options такой же, как и у функций waitpid() и wait4().
# waitstatus_to_exitcode() можно использовать для преобразования статуса выхода в код выхода.
#      Доступность: Unix, не Emscripten, не WASI.

import os

pid = os.fork()
if pid:
    p_id = pid
    print("pid =", pid)
    # Specify option (Укажите вариант)
    option_1 = os.WUNTRACED  # дочерние процессы сообщаются, если они были остановлены,
    # но их текущее состояние не сообщается с тех пор, как они были остановлены.
    option_2 = os.WCONTINUED  # флаг вызывает сообщение о дочерних процессах, если они были
    # продолжены с момента остановки управления заданиями с момента последнего сообщения о них.
    print("option =", option_1)
    status = os.wait3(option_1)
    print('++++++++++++++++++++++++++++++++++')
    print("Status of child process:", status)
else:
    print("In Child process-")
    print("Process ID:", os.getpid())
    print("Hello World!")
    print("Exiting..")

"""os.WCONTINUED"""
# Этот флаг опций для waitpid(), wait3(), wait4() и waitid() вызывает сообщение о дочерних
# процессах, если они были продолжены с момента остановки управления заданиями с
# момента последнего сообщения о них.
#       Доступность: Unix, не Emscripten, не WASI.

"""os.WUNTRACED"""
# Этот флаг опций для waitpid(), wait3() и wait4() приводит к тому, что дочерние процессы
# также сообщаются, если они были остановлены, но их текущее состояние не сообщается с тех
# пор, как они были остановлены.
#      Эта опция недоступна для waitid().
#      Доступность: Unix, не Emscripten, не WASI.

"""os.WNOHANG"""
# Этот флаг параметров приводит к немедленному возврату функций waitpid(), wait3(),
# wait4() и waitid(), если статус дочернего процесса недоступен.
#       Доступность: Unix, не Emscripten, не WASI.