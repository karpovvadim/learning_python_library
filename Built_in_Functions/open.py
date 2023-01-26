"""open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None,
   closefd=True, opener=None)"""
# Открыть файл и вернуть соответствующий файловый объект. Если файл не может быть открыт,
# возникает ошибка OSError. Дополнительные примеры использования этой функции см. в
# разделе Чтение и запись файлов.
# 1. file — это объект, подобный пути, задающий путь (абсолютный или относительный к текущему
# рабочему каталогу) файла, который нужно открыть, или целочисленный файловый дескриптор файла,
# который нужно обернуть. (Если указан файловый дескриптор, он закрывается при закрытии
# возвращаемого объекта ввода-вывода, если только для параметра closefd не задано значение False.)
# 2. mode — необязательная строка, указывающая режим, в котором открывается файл. По умолчанию
# это «r», что означает «открыто для чтения в текстовом режиме». Другими распространенными
# значениями являются «w» для записи (усечение файла, если он уже существует), «x» для
# монопольного создания и «a» для добавления (что в некоторых системах Unix означает,
# что все операции записи добавляются в конец файла). независимо от текущей позиции поиска).
# В текстовом режиме, если кодировка не указана, используемая кодировка зависит от платформы:
# вызывается locale.getencoding() для получения текущей кодировки локали. (Для чтения и записи
# необработанных байтов используйте двоичный режим и оставьте кодировку неуказанной.)
# Доступны следующие режимы:

# Character   Meaning
# (Персонаж)  (Значение)
#   'r"       open for reading (default) - открыть для чтения (по умолчанию)
#   'w"       open for writing, truncating the file first - открыть для записи,
#                                                           предварительно обрезав файл
#   'x'        open for exclusive creation, failing if the file already exists -
#              открыть для эксклюзивного создания, если файл уже существует
#   'a'        open for writing, appending to the end of file if it exists -
#              открыть для записи, добавив в конец файла, если он существует
#   'b'        binary mode - двоичный режим
#   't'        text mode (default) - текстовый режим (по умолчанию)
#   '+'        open for updating (reading and writing) - открыты для обновления (чтение и запись)
# Режим по умолчанию — «r» (открыт для чтения текста, синоним «rt»). Режимы «w+» и «w+b»
# открывают и обрезают файл. Режимы 'r+' и 'r+b' открывают файл без усечения.
# Как упоминалось в обзоре, Python различает двоичный и текстовый ввод-вывод. Файлы, открытые
# в двоичном режиме (включая «b» в аргументе режима), возвращают содержимое в виде байтовых
# объектов без какого-либо декодирования. В текстовом режиме (по умолчанию или когда 't' в
# ключено в аргумент режима) содержимое файла возвращается как str, причем байты были сначала
# декодированы с использованием кодировки, зависящей от платформы, или с использованием
# указанной кодировки, если она задана.
# Примечание
# Python не зависит от представлений базовой операционной системы о текстовых файлах;
# вся обработка выполняется самим Python и поэтому не зависит от платформы.
# 3. buffering (буферизация) — это необязательное целое число, используемое для установки политики буферизации.
# Передайте 0, чтобы отключить буферизацию (разрешено только в двоичном режиме), 1,
# чтобы выбрать буферизацию строк (можно использовать только в текстовом режиме),
# и целое число > 1, чтобы указать размер в байтах буфера фрагмента фиксированного размера.
# Обратите внимание, что указание размера буфера таким образом применимо к двоичному
# буферизованному вводу-выводу, но TextIOWrapper (т. е. файлы, открытые с помощью режима = 'r+')
# будет иметь другую буферизацию. Чтобы отключить буферизацию в TextIOWrapper, рассмотрите
# возможность использования флага write_through для io.TextIOWrapper.reconfigure(). Если
# аргумент буферизации не указан, политика буферизации по умолчанию работает следующим образом:
# 3.1. Двоичные файлы буферизуются фрагментами фиксированного размера; размер буфера выбирается с
# помощью эвристики, пытающейся определить «размер блока» базового устройства и возвращаясь к io.
# DEFAULT_BUFFER_SIZE. Во многих системах длина буфера обычно составляет 4096 или 8192 байта.
# 3.2. «Интерактивные» текстовые файлы (файлы, для которых функция isatty() возвращает значение
# True) используют буферизацию строк. Другие текстовые файлы используют политику, описанную
# выше для двоичных файлов.
# 4. encoding (кодировка) — это имя кодировки, используемой для декодирования или кодирования
# файла. Это должно использоваться только в текстовом режиме. Кодировка по умолчанию зависит
# от платформы (независимо от того, что возвращает locale.getencoding()), но можно использовать
# любую текстовую кодировку, поддерживаемую Python. См. модуль кодеков для списка
# поддерживаемых кодировок.
# 5. error — необязательная строка, указывающая, как должны обрабатываться ошибки кодирования и
# декодирования — ее нельзя использовать в двоичном режиме. Доступны различные стандартные
# обработчики ошибок (перечислены в разделе «Обработчики ошибок»), хотя любое имя обработки
# ошибок, зарегистрированное с помощью codecs.register_error(), также допустимо. Стандартные
# названия включают:
# 5.1. 'strict' (строгий), чтобы вызвать исключение ValueError в случае ошибки кодирования.
# Значение по умолчанию None имеет тот же эффект.
# 5.2. 'ignore' («игнорировать») игнорирует ошибки. Обратите внимание, что игнорирование ошибок
# кодирования может привести к потере данных.
# 5.3. 'replace' заставляет маркер замены (например, '?') вставляться там, где есть
# искаженные данные.
# 5.4. 'surrogateescape' (суррогатный побег) будет представлять любые неправильные байты как
# младшие единицы суррогатного кода в диапазоне от U+DC80 до U+DCFF. Эти единицы суррогатного
# кода затем будут преобразованы обратно в те же байты, когда при записи данных используется
# обработчик ошибок суррогатного перехода. Это полезно для обработки файлов в неизвестной кодировке.
# 5.5. «xmlcharrefreplace» поддерживается только при записи в файл. Символы, не поддерживаемые
# кодировкой, заменяются соответствующей ссылкой на символы XML &#nnn;.
# 5.6. 'backslashreplace' заменяет искаженные данные управляющими последовательностями Python с
# обратной косой чертой.
# 5.7. 'namereplace' (также поддерживается только при записи) заменяет неподдерживаемые символы
# управляющими последовательностями \N{...}.
# 6. newline определяет, как анализировать символы новой строки из потока. Это может быть
# None, '', '\n', '\r' и '\r\n'. Это работает следующим образом:
# 6.1. При чтении ввода из потока, если для новой строки установлено значение «Нет», включается
# режим универсальной новой строки. Строки во входных данных могут заканчиваться на '\n', '\r'
# или '\r\n', и они преобразуются в '\n' перед возвратом вызывающей стороне. Если это '', включен
# универсальный режим новой строки, но окончания строк возвращаются вызывающей стороне без
# перевода. Если он имеет какое-либо другое допустимое значение, входные строки завершаются
# только данной строкой, а окончание строки возвращается вызывающей стороне без перевода.
# 6.2. При записи вывода в поток, если новая строка имеет значение None, любые записанные
# символы '\n' преобразуются в системный разделитель строк по умолчанию, os.linesep. Если новая
# строка равна '' или '\n', перевод не выполняется. Если перевод строки является любым другим
# допустимым значением, любые написанные символы '\n' преобразуются в заданную строку.
# 7. Если для параметра closefd установлено значение False и был задан файловый дескриптор,
# а не имя файла, базовый файловый дескриптор будет оставаться открытым при закрытии файла.
# Если задано имя файла, то closefd должно быть равно True (по умолчанию); в противном случае
# будет вызвана ошибка.
# 8. Пользовательский открыватель можно использовать, передав вызываемый объект как
# opener (открыватель). Базовый файловый дескриптор для файлового объекта затем получается путем
# вызова opener с (file, flags). opener должен возвращать дескриптор открытого файла (передача
# os.open в качестве открывателя приводит к функциональности, аналогичной передаче None).
# Вновь созданный файл не подлежит наследованию.
# В следующем примере параметр dir_fd функции os.open() используется для открытия файла
# относительно заданного каталога:
"""
import os
dir_fd = os.open('somedir', os.O_RDONLY)
def opener(path, flags):
    return os.open(path, flags, dir_fd=dir_fd)

with open('spamspam.txt', 'w', opener=opener) as f:
    print('This will be written to somedir/spamspam.txt', file=f)

os.close(dir_fd)  # don't leak a file descriptor (не сливайте файловый дескриптор)
"""
# Тип файлового объекта, возвращаемого функцией open(), зависит от режима. Когда open()
# используется для открытия файла в текстовом режиме («w», «r», «wt», «rt» и т. д.), он
# возвращает подкласс io.TextIOBase (в частности, io.TextIOWrapper). При использовании для
# открытия файла в двоичном режиме с буферизацией возвращаемый класс является подклассом
# io.BufferedIOBase. Точный класс варьируется: в двоичном режиме чтения он возвращает
# io.BufferedReader; в режимах двоичной записи и добавления двоичных данных он возвращает
# io.BufferedWriter, а в режиме чтения/записи он возвращает io.BufferedRandom. Когда
# буферизация отключена, возвращается необработанный поток, подкласс io.RawIOBase, io.FileIO.
# См. также модули обработки файлов, такие как fileinput, io (где объявлено open()), os,
# os.path, tempfile и Shutil.
# Вызывает открытое событие аудита с файлом аргументов, режимом, флагами.
# Аргументы режима и флагов могли быть изменены или выведены из исходного вызова.
# Изменено в версии 3.3:
# 1. Добавлен параметр открывателя.
# 2. Добавлен режим «x».
# 3. Раньше вызывался IOError, теперь это псевдоним OSError.
# 4. FileExistsError теперь вызывается, если файл, открытый в монопольном режиме создания ('x'),
# уже существует.
# Изменено в версии 3.4:
# Теперь файл не наследуется.
# Изменено в версии 3.5:
# 1. Если системный вызов прерывается, а обработчик сигнала не вызывает исключение, функция теперь
# повторяет системный вызов вместо создания исключения InterruptedError (обоснование см.
# в PEP 475).
# 2. Добавлен обработчик ошибок namereplace.
# Изменено в версии 3.6:
#     Добавлена поддержка для приема объектов, реализующих os.PathLike.
#     В Windows открытие буфера консоли может вернуть подкласс io.RawIOBase, отличный от io.FileIO.
# Изменено в версии 3.11: Убран режим "U".
# opens test.text file of the current directory
"""
f = open("test.txt")

# specifying the full path (указание полного пути)
f = open("C:/Python33/README.md.txt")

# opens the file in reading mode (открывает файл в режиме чтения)
f = open("path_to_file", mode='r')

# opens the file in writing mode (открывает файл в режиме записи)
f = open("path_to_file", mode='w')

# opens for writing to the end (открывается для записи до конца)
f = open("path_to_file", mode='a')
"""