""" os.system(command)"""
#      Выполнить команду (строку) в подоболочке. Это реализуется путем вызова стандартной
# функции C system() и имеет те же ограничения. Изменения в sys.stdin и т. д. не отражаются
# в среде выполняемой команды. Если команда генерирует какой-либо вывод, он будет
# отправлен в стандартный поток вывода интерпретатора. Стандарт C не определяет значение
# возвращаемого значения функции C, поэтому возвращаемое значение функции Python зависит
# от системы.
#      В Unix возвращаемое значение является статусом завершения процесса, закодированным
# в формате, указанном для wait().
#      В Windows возвращаемое значение — это значение, возвращаемое системной оболочкой
# после выполнения команды. Оболочка задается переменной среды Windows COMSPEC: обычно
# это cmd.exe, которая возвращает статус завершения выполнения команды; в системах,
# использующих неродную оболочку, обратитесь к документации по вашей оболочке.
#      Модуль подпроцессов предоставляет более мощные средства для создания новых
# процессов и получения их результатов; использование этого модуля предпочтительнее
# использования этой функции. Некоторые полезные рецепты см. в разделе Замена старых
# функций модулем подпроцесса в документации по подпроцессу.
#      В Unix можно использовать функцию waitstatus_to_exitcode() для преобразования
# результата (статуса выхода) в код выхода. В Windows результатом является
# непосредственно код выхода.
#      Вызывает событие аудита os.system с командой аргумента.
#      Доступность: Unix, Windows, не Emscripten, не WASI.

import os
from subprocess import run, STDOUT, PIPE
# указывайте полный путь к запускаемой программе/команде или она не будет работать
cmd = '/bin/ls -l /home/vadim/PycharmProjects/learning_python_library/Generic_Operating_System_Services'
# перенаправляем `stdout` и `stderr` в переменную `output`
output = run(cmd.split(), stdout=PIPE, stderr=STDOUT, text=True)
print(output)

# указывайте полный путь к запускаемой
# программе/команде или она не будет работать
cmd = "/home/vadim/PycharmProjects/learning_python_library"
code_exit = os.system(cmd)
print('----------------------------------------------------------------------')
print("code_exit =", code_exit)
# Выведет:
# 0 - успех выполнения команды, что означает код завершения программы.
# Permission denied - В правах отказано