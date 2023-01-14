"""os.waitid(idtype, id, options, /)"""
#      Дождитесь завершения дочернего процесса.
#      idtype может быть P_PID, P_PGID, P_ALL или (в Linux) P_PIDFD. От этого зависит
# интерпретация id; см. их отдельные описания.
#      options представляет собой комбинацию флагов по ИЛИ. Требуется хотя бы одно из
# значений WEXITED, WSTOPPED или WCONTINUED; WNOHANG и WNOWAIT — дополнительные
# необязательные флаги.
#      Возвращаемое значение — это объект, представляющий данные, содержащиеся в
# структуре siginfo_t, со следующими атрибутами:
#          si_pid (идентификатор процесса)
#          si_uid (реальный ID пользователя дочернего элемента)
#          si_signo (всегда SIGCHLD)
#          si_status (статус выхода или номер сигнала, в зависимости от si_code)
#          si_code (см. CLD_EXITED для возможных значений)
#      Если указан WNOHANG и в запрошенном состоянии нет соответствующих дочерних
# элементов, возвращается None. В противном случае, если нет подходящих дочерних
# элементов, которых можно было бы ожидать, возникает ChildProcessError.
#      Доступность: Unix, не Emscripten, не WASI.
#      Новое в версии 3.3.
import os
pid = os.fork()
if pid:
    idtype = os.P_PID  # Specify idtype (Укажите тип идентификатора)
    print(idtype)
    id = pid
    print(id)
    option = os.WEXITED  # Specify option (Укажите вариант)
    print(option)
    status = os.waitid(idtype, id, option)
    print('++++++++++++++++++++++++++++++++++')
    print("Status of child process:", status)
else:
    print("In Child process-")
    print("Process ID:", os.getpid())
    print("Hello ! Geeks")
    print("Exiting..")

