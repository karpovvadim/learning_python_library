"""os.abort()"""  # ПРЕРЫВАНИЕ
# Сгенерируйте сигнал SIGABRT для текущего процесса. В Unix по умолчанию создается дамп
# ядра; в Windows процесс немедленно возвращает код выхода 3. Имейте в виду, что вызов
# этой функции не вызовет обработчик сигналов Python, зарегистрированный для SIGABRT с
# помощью signal.signal().

import os
print("Hello World!")
os.abort()
print("This will not be printed")
# Process finished with exit code 134 (interrupted by signal 6: SIGABRT)
# Процесс завершен с кодом выхода 134 (прерыван сигналом 6: СИГНАЛ ПРЕРЫВАНИЯ)
