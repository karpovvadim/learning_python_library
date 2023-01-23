    В то время как Справочник по языку Python описывает точный синтаксис и семантику
языка Python, это справочное руководство по библиотеке описывает стандартную
библиотеку, которая распространяется вместе с Python. В нем также описываются
некоторые необязательные компоненты, обычно включаемые в дистрибутивы Python.

Стандартная библиотека Python очень обширна и предлагает широкий спектр возможностей,
как указано в длинном оглавлении, приведенном ниже. Библиотека содержит встроенные
модули (написанные на C), обеспечивающие доступ к системным функциям, таким как
файловый ввод-вывод (I/O), которые в противном случае были бы недоступны программистам
Python, а также модули, написанные на Python, которые предоставляют стандартизированные
решения для многих проблем, возникающих в повседневное программирование. Некоторые
из этих модулей специально предназначены для поощрения и улучшения переносимости
программ Python за счет абстрагирования платформо-специфических API-интерфейсов,
не зависящих от платформы.

Установщики Python для платформы Windows обычно включают в себя всю стандартную
библиотеку, а также множество дополнительных компонентов. Для Unix-подобных
операционных систем Python обычно предоставляется в виде набора пакетов, поэтому
может потребоваться использование инструментов упаковки, поставляемых с операционной
системой, для получения некоторых или всех дополнительных компонентов.

В дополнение к стандартной библиотеке существует активная коллекция из сотен тысяч
компонентов (от отдельных программ и модулей до пакетов и целых сред разработки
приложений), доступных в индексе пакетов Python.
Introduction                            Введение
    Notes on availability                                   Примечания о наличии
Built-in Functions                      Встроенные функции
Built-in Constants                      Встроенные константы
    Constants added by the site module                      Константы, добавляемые модулем сайта

Built-in Types                          Встроенные типы
    Truth Value Testing                                     Проверка истинности
    Boolean Operations — and, or, not                       Логические операции — и, или, не
    Comparisons                                             Сравнения
    Numeric Types — int, float, complex                     Числовые типы — int, float, комплекс
    Iterator Types                                          Типы итераторов
    Sequence Types — list, tuple, range                     Типы последовательностей — список, кортеж, диапазон
    Text Sequence Type — str                                Тип текстовой последовательности — str
    Binary Sequence Types — bytes, bytearray, memoryview    Типы двоичных последовательностей — bytes,
                                                            bytearray, memoryview
    Set Types — set, frozenset                              Типы наборов — набор, замороженный набор
    Mapping Types — dict                                    Типы сопоставления — dict
    Context Manager Types                                   Типы диспетчера контекста
    Type Annotation Types — Generic Alias, Union            Type Типы аннотаций — общий псевдоним, объединение
    Other Built-in Types
    Special Attributes                                      Специальные атрибуты
    Integer string conversion length limitation             Ограничение длины преобразования целочисленной строки

Built-in Exceptions                     Встроенные исключения
    Exception context                                       Контекст исключения
    Inheriting from built-in exceptions                     Наследование от встроенных исключений
    Base classes                                            Базовые классы
    Concrete exceptions                                     Конкретные исключения
    Warnings                                                Предупреждения
    Exception groups                                        Группы исключений
    Exception hierarchy                                     Иерархия исключений

Text Processing Services                Услуги обработки текста
    string — Common string operations                       — Общие строковые операции
    re — Regular expression operations                      — Операции с регулярными выражениями
    difflib — Helpers for computing deltas                  — Помощники для вычисления дельт
    textwrap — Text wrapping and filling                    — Обтекание и заполнение текста
    unicodedata — Unicode Database                          — База данных Юникода
    stringprep — Internet String Preparation                — Подготовка строки Интернета
    readline — GNU readline interface                       — интерфейс GNU readline
    rlcompleter — Completion function for GNU readline      — Функция завершения для GNU readline

Binary Data Services                    Службы двоичных данных
    struct — Interpret bytes as packed binary data          — Интерпретировать байты как упакованные двоичные данные
    codecs — Codec registry and base classes                — Реестр кодеков и базовые классы

Data Types                              Типы данных
    datetime — Basic date and time types                    — Основные типы даты и времени
    zoneinfo — IANA time zone support                       — поддержка часовых поясов IANA
    calendar — General calendar-related functions           — Общие функции, связанные с календарем
    collections — Container datatypes                       — Контейнерные типы данных
    collections.abc — Abstract Base Classes for Containers  — абстрактные базовые классы для контейнеров
    heapq — Heap queue algorithm                            — Алгоритм очереди кучи
    bisect — Array bisection algorithm                      — Алгоритм деления массива пополам
    array — Efficient arrays of numeric values              — Эффективные массивы числовых значений
    weakref — Weak references                               — Слабые ссылки
    types — Dynamic type creation and names for built-in types — Создание динамического типа и имена для встроенных
                                                                 типов
    copy — Shallow and deep copy operations                 — Мелкие и глубокие операции копирования
    pprint — Data pretty printer                            — симпатичный принтер данных
    reprlib — Alternate repr() implementation               — Альтернативная реализация repr()
    enum — Support for enumerations                         — поддержка перечислений
    graphlib — Functionality to operate with graph-like structures — Функциональность для работы с графоподобными
                                                                     структурами

Numeric and Mathematical Modules        Числовые и математические модули
    numbers — Numeric abstract base classes                 Числовые абстрактные базовые классы
    math — Mathematical functions                           — Математические функции
    cmath — Mathematical functions for complex numbers      — Математические функции для комплексных чисел
    decimal — Decimal fixed point and floating point arithmetic — Десятичная фиксированная точка и арифметика с
                                                                  плавающей запятой
    fractions — Rational numbers                            — Рациональные числа
    random — Generate pseudo-random numbers                 — Сгенерировать псевдослучайные числа
    statistics — Mathematical statistics functions          — Функции математической статистики

Functional Programming Modules          Модули функционального программирования
    itertools — Functions creating iterators for efficient looping — Функции, создающие итераторы для эффективного цикла
    functools — Higher-order functions and operations on callable objects — Функции и операции высшего порядка над
                                                                            вызываемыми объектами
    operator — Standard operators as functions              — Стандартные операторы как функции

File and Directory Access               Доступ к файлам и каталогам
    pathlib — Object-oriented filesystem paths              — Пути объектно-ориентированной файловой системы
    os.path — Common pathname manipulations                 — общие манипуляции с путями
    fileinput — Iterate over lines from multiple input streams — Итерация по строкам из нескольких входных потоков
    stat — Interpreting stat() results                      — Интерпретация результатов stat()
    filecmp — File and Directory Comparisons                — Сравнение файлов и каталогов
    tempfile — Generate temporary files and directories     — Создает временные файлы и каталоги
    glob — Unix style pathname pattern expansion            — Расширение шаблона пути в стиле Unix
    fnmatch — Unix filename pattern matching                — сопоставление имен файлов Unix с образцом
    linecache — Random access to text lines                 — Произвольный доступ к текстовым строкам
    shutil — High-level file operations                     — Высокоуровневые файловые операции

Data Persistence                        Сохранение данных
    pickle — Python object serialization                    — сериализация объекта Python
    copyreg — Register pickle support functions             — Регистрация функций поддержки pickle
    shelve — Python object persistence                      — постоянство объекта Python
    marshal — Internal Python object serialization          — Внутренняя сериализация объектов Python
    dbm — Interfaces to Unix “databases”                    — Интерфейсы к «базам данных» Unix
    sqlite3 — DB-API 2.0 interface for SQLite databases     — интерфейс DB-API 2.0 для баз данных SQLite

Data Compression and Archiving          Сжатие данных и архивирование
    zlib — Compression compatible with gzip                 — сжатие, совместимое с gzip
    gzip — Support for gzip files                           — поддержка файлов gzip.
    bz2 — Support for bzip2 compression                     — поддержка сжатия bzip2.
    lzma — Compression using the LZMA algorithm             — Сжатие с использованием алгоритма LZMA
    zipfile — Work with ZIP archives                        — Работа с ZIP-архивами
    tarfile — Read and write tar archive files              — Чтение и запись архивных файлов tar

File Formats                            Форматы файлов
    csv — CSV File Reading and Writing                      — Чтение и запись файла CSV
    configparser — Configuration file parser                — Парсер файла конфигурации
    tomllib — Parse TOML files                              — Разбирает файлы TOML
    netrc — netrc file processing                           — обработка файла netrc
    plistlib — Generate and parse Apple .plist files        — Генерирует и анализирует файлы Apple .plist

Cryptographic Services                  Криптографические услуги
    hashlib — Secure hashes and message digests             — Безопасные хэши и дайджесты сообщений
    hmac — Keyed-Hashing for Message Authentication         — Keyed-Hashing для аутентификации сообщений
    secrets — Generate secure random numbers for managing secrets — генерировать безопасные случайные числа для
                                                                    управления секретами

Generic Operating System Services       Общие службы операционной системы
    os — Miscellaneous operating system interfaces          — Различные интерфейсы операционной системы
    io — Core tools for working with streams                — Основные инструменты для работы с потоками
    time — Time access and conversions                      — Доступ по времени и конверсии
    argparse — Parser for command-line options, arguments and sub-commands — Анализатор параметров командной строки,
                                                                             аргументов и подкоманд
    getopt — C-style parser for command line options        — синтаксический анализатор в стиле C для параметров
                                                              командной строки
    logging — Logging facility for Python                   — Средство ведения журнала для Python
    logging.config — Logging configuration                  — конфигурация ведения журнала
    logging.handlers — Logging handlers                     — Обработчики протоколирования
    getpass — Portable password input                       — Портативный ввод пароля
    curses — Terminal handling for character-cell displays  - Терминальная обработка для отображений символьных ячеек
    curses.textpad — Text input widget for curses programs  — Виджет ввода текста для программ curses
    curses.ascii — Utilities for ASCII characters           — Утилиты для символов ASCII
    curses.panel — A panel stack extension for curses       — расширение стека панелей для curses
    platform — Access to underlying platform’s identifying data — Доступ к идентифицирующим данным базовой платформы
    errno — Standard errno system symbols                   — Стандартные системные символы errno
    ctypes — A foreign function library for Python          — Внешняя библиотека функций для Python

Concurrent Execution                    Параллельное выполнение
    threading — Thread-based parallelism                    — Параллелизм на основе потоков
    multiprocessing — Process-based parallelism             — Параллелизм на основе процессов
    multiprocessing.shared_memory — Shared memory for direct access across processes — Общая память для прямого доступа
                                                                                       между процессами
    The concurrent package                                  Параллельный пакет
    concurrent.futures — Launching parallel tasks           — Запуск параллельных задач
    subprocess — Subprocess management                      — Управление подпроцессом
    sched — Event scheduler                                 — Планировщик событий
    queue — A synchronized queue class                      — Класс синхронизированной очереди
    contextvars — Context Variables                         — Контекстные переменные
    _thread — Low-level threading API                       — низкоуровневый API многопоточности

Networking and Interprocess Communication   Сеть и межпроцессное взаимодействие
    asyncio — Asynchronous I/O                              — асинхронный ввод-вывод
    socket — Low-level networking interface                 — низкоуровневый сетевой интерфейс
    ssl — TLS/SSL wrapper for socket objects                — оболочка TLS/SSL для объектов сокета
    select — Waiting for I/O completion                     — Ожидание завершения ввода/вывода
    selectors — High-level I/O multiplexing                 — Высокоуровневое мультиплексирование ввода/вывода
    signal — Set handlers for asynchronous events           — Установите обработчики для асинхронных событий
    mmap — Memory-mapped file support                       — поддержка отображаемых в памяти файлов

Internet Data Handling                  Обработка данных в Интернете
    email — An email and MIME handling package              — пакет обработки электронной почты и MIME
    json — JSON encoder and decoder                         — кодировщик и декодер JSON
    mailbox — Manipulate mailboxes in various formats       — Управление почтовыми ящиками в различных форматах
    mimetypes — Map filenames to MIME types                 — Сопоставьте имена файлов с типами MIME
    base64 — Base16, Base32, Base64, Base85 Data Encodings  — кодировки данных Base16, Base32, Base64, Base85
    binascii — Convert between binary and ASCII             — Преобразование между двоичным кодом и ASCII
    quopri — Encode and decode MIME quoted-printable data   — Кодирует и декодирует данные MIME в кавычках и для печати

Structured Markup Processing Tools      Инструменты обработки структурированной разметки
    html — HyperText Markup Language support                — поддержка языка гипертекстовой разметки
    html.parser — Simple HTML and XHTML parser              — Простой парсер HTML и XHTML
    html.entities — Definitions of HTML general entities    — определения общих сущностей HTML
    XML Processing Modules                                  Модули обработки XML
    xml.etree.ElementTree — The ElementTree XML API         — XML-API ElementTree
    xml.dom — The Document Object Model API                 — API объектной модели документа
    xml.dom.minidom — Minimal DOM implementation            — Минимальная реализация DOM
    xml.dom.pulldom — Support for building partial DOM trees — поддержка построения частичных деревьев DOM
    xml.sax — Support for SAX2 parsers                      — поддержка парсеров SAX2
    xml.sax.handler — Base classes for SAX handlers         — Базовые классы для обработчиков SAX
    xml.sax.saxutils — SAX Utilities                        — Утилиты SAX
    xml.sax.xmlreader — Interface for XML parsers           — интерфейс для парсеров XML
    xml.parsers.expat — Fast XML parsing using Expat        — Быстрый анализ XML с помощью Expat

Internet Protocols and Support          Интернет-протоколы и поддержка
    webbrowser — Convenient web-browser controller          — Удобный контроллер веб-браузера
    wsgiref — WSGI Utilities and Reference Implementation   — Утилиты WSGI и справочная реализация
    urllib — URL handling modules                           — модули обработки URL
    urllib.request — Extensible library for opening URLs    — расширяемая библиотека для открытия URL
    urllib.response — Response classes used by urllib       — классы ответов, используемые urllib
    urllib.parse — Parse URLs into components               — Разбирает URL на компоненты
    urllib.error — Exception classes raised by urllib.request — классы исключений, вызванные urllib.request
    urllib.robotparser — Parser for robots.txt              — Парсер для robots.txt
    http — HTTP modules                                     — HTTP-модули
    http.client — HTTP protocol client                      — клиент протокола HTTP
    ftplib — FTP protocol client                            — клиент протокола FTP
    poplib — POP3 protocol client                           — клиент протокола POP3
    imaplib — IMAP4 protocol client                         — клиент протокола IMAP4
    smtplib — SMTP protocol client                          — клиент протокола SMTP
    uuid — UUID objects according to RFC 4122               — объекты UUID согласно RFC 4122
    socketserver — A framework for network servers          — фреймворк для сетевых серверов
    http.server — HTTP servers                              — HTTP-серверы
    http.cookies — HTTP state management                    — управление состоянием HTTP
    http.cookiejar — Cookie handling for HTTP clients       — обработка файлов cookie для HTTP-клиентов.
    xmlrpc — XMLRPC server and client modules               — сервер XMLRPC и клиентские модули
    xmlrpc.client — XML-RPC client access                   — клиентский доступ XML-RPC
    xmlrpc.server — Basic XML-RPC servers                   — Базовые серверы XML-RPC
    ipaddress — IPv4/IPv6 manipulation library              — библиотека манипулирования IPv4/IPv6

Multimedia Services                     Мультимедийные услуги
    wave — Read and write WAV files                         — Чтение и запись файлов WAV
    colorsys — Conversions between color systems            — Преобразования между цветовыми системами

Internationalization                    Интернационализация
    gettext — Multilingual internationalization services    — Многоязычные сервисы интернационализации
    locale — Internationalization services                  — Услуги интернационализации

Program Frameworks                      Рамки программы
    turtle — Turtle graphics                                — графика черепахи
    cmd — Support for line-oriented command interpreters    — Поддержка интерпретаторов команд, ориентированных на
                                                              строку
    shlex — Simple lexical analysis                         — Простой лексический анализ

Graphical User Interfaces with Tk       Графические пользовательские интерфейсы с Tk
    tkinter — Python interface to Tcl/Tk                    — интерфейс Python для Tcl/Tk
    tkinter.colorchooser — Color choosing dialog            — Диалог выбора цвета
    tkinter.font — Tkinter font wrapper                     — оболочка шрифта Tkinter
    Tkinter Dialogs                                         Диалоги Ткинтера
    tkinter.messagebox — Tkinter message prompts            — подсказки сообщения Tkinter
    tkinter.scrolledtext — Scrolled Text Widget             — виджет прокручиваемого текста
    tkinter.dnd — Drag and drop support                     — Поддержка перетаскивания
    tkinter.ttk — Tk themed widgets                         — тематические виджеты Tk
    tkinter.tix — Extension widgets for Tk                  — Виджеты расширения для Tk
    IDLE                                                    Интегрированная среда разработки и обучения.

Development Tools                       Инструменты разработки
    typing — Support for type hints                         — Поддержка подсказок типа
    pydoc — Documentation generator and online help system  — Генератор документации и интерактивная справочная система
    Python Development Mode                                 Режим разработки Python
    Effects of the Python Development Mode                  Эффекты режима разработки Python
    ResourceWarning Example                                 Пример предупреждения о ресурсах
    Bad file descriptor error example                       Пример ошибки неверного файлового дескриптора
    doctest — Test interactive Python examples              — Протестируйте интерактивные примеры Python
    unittest — Unit testing framework —                     Фреймворк модульного тестирования
    unittest.mock — mock object library                     — библиотека фиктивных объектов
    unittest.mock — getting started                         — начало работы
    2to3 — Automated Python 2 to 3 code translation         — Автоматический перевод кода Python 2 в 3
    test — Regression tests package for Python              — Пакет регрессионных тестов для Python
    test.support — Utilities for the Python test suite      — Утилиты для набора тестов Python
    test.support.socket_helper — Utilities for socket tests — Утилиты для тестов сокетов
    test.support.script_helper — Utilities for the Python execution tests — Утилиты для выполнения тестов Python
    test.support.bytecode_helper — Support tools for testing correct bytecode generation — Инструменты поддержки для
                                                                                проверки правильной генерации байт-кода
    test.support.threading_helper — Utilities for threading tests — Утилиты для потокового тестирования
    test.support.os_helper — Utilities for os tests         — Утилиты для тестов ОС
    test.support.import_helper — Utilities for import tests — Утилиты для импорта тестов
    test.support.warnings_helper — Utilities for warnings tests — Утилиты для тестов предупреждений

Debugging and Profiling                 Отладка и профилирование
    Audit events table                                      Таблица событий аудита
    bdb — Debugger framework                                — Платформа отладчика
    faulthandler — Dump the Python traceback                — Дамп обратной трассировки Python
    pdb — The Python Debugger                               — отладчик Python
    The Python Profilers                                    Профилировщики Python
    timeit — Measure execution time of small code snippets  — измеряет время выполнения небольших фрагментов кода
    trace — Trace or track Python statement execution       — Трассировка или отслеживание выполнения оператора Python
    tracemalloc — Trace memory allocations                  — Отслеживает выделение памяти

Software Packaging and Distribution     Упаковка и распространение программного обеспечения
    distutils — Building and installing Python modules      — Сборка и установка модулей Python
    ensurepip — Bootstrapping the pip installer             — Начальная загрузка установщика pip
    venv — Creation of virtual environments                 — Создание виртуальных сред
    zipapp — Manage executable Python zip archives          — Управление исполняемыми zip-архивами Python

Python Runtime Services                 Службы выполнения Python
    sys — System-specific parameters and functions          — Системные параметры и функции
    sysconfig — Provide access to Python’s configuration information — предоставляет доступ к информации о конфигурации
                                                                       Python
    builtins — Built-in objects                             — Встроенные объекты
    __main__ — Top-level code environment                   — среда кода верхнего уровня
    warnings — Warning control                              — Управление предупреждением
    dataclasses — Data Classes                              — Классы данных
    contextlib — Utilities for with-statement contexts      — Утилиты для контекстов with-statement
    abc — Abstract Base Classes                             — абстрактные базовые классы
    atexit — Exit handlers                                  — Обработчики выхода
    traceback — Print or retrieve a stack traceback         — Напечатайте или извлеките трассировку стека
    __future__ — Future statement definitions               — Определения операторов будущего
    gc — Garbage Collector interface                        — интерфейс сборщика мусора
    inspect — Inspect live objects                          — Проверяйте живые объекты
    site — Site-specific configuration hook                 — хук конфигурации для конкретного сайта

Custom Python Interpreters              Пользовательские интерпретаторы Python
    code — Interpreter base classes                         — Базовые классы интерпретатора
    codeop — Compile Python code                            — Скомпилировать код Python

Importing Modules                       Импорт модулей
    zipimport — Import modules from Zip archives            — Импорт модулей из Zip-архивов
    pkgutil — Package extension utility                     — утилита расширения пакета
    modulefinder — Find modules used by a script            — Находит модули, используемые сценарием
    runpy — Locating and executing Python modules           — Поиск и выполнение модулей Python
    importlib — The implementation of import                — Реализация импорта
    importlib.resources – Resources                         — Ресурсы
    Deprecated functions                                    Устаревшие функции
    importlib.resources.abc – Abstract base classes for resources — Абстрактные базовые классы для ресурсов
    Using importlib.metadata                                Использование importlib.metadata
    The initialization of the sys.path module search path   Инициализация пути поиска модуля sys.path

Python Language Services                Языковые службы Python
    ast — Abstract Syntax Trees                             — Абстрактные синтаксические деревья
    symtable — Access to the compiler’s symbol tables       — Доступ к таблицам символов компилятора
    token — Constants used with Python parse trees          — Константы, используемые с деревьями синтаксического
                                                              анализа Python
    keyword — Testing for Python keywords                   — Тестирование ключевых слов Python
    tokenize — Tokenizer for Python source                  — Tokenizer для источника Python
    tabnanny — Detection of ambiguous indentation           — Обнаружение неоднозначного отступа
    pyclbr — Python module browser support                  — поддержка браузера модуля Python
    py_compile — Compile Python source files                — компилирует исходные файлы Python
    compileall — Byte-compile Python libraries              — байтовая компиляция библиотек Python
    dis — Disassembler for Python bytecode                  — Дизассемблер для байт-кода Python
    pickletools — Tools for pickle developers               — Инструменты для разработчиков pickle

MS Windows Specific Services            Специальные службы MS Windows
    msvcrt — Useful routines from the MS VC++ runtime       — Полезные подпрограммы из среды выполнения MS VC++
    winreg — Windows registry access                        — доступ к реестру Windows
    winsound — Sound-playing interface for Windows          — Звуковой интерфейс для Windows

Unix Specific Services                  Специальные службы Unix
    posix — The most common POSIX system calls              — наиболее распространенные системные вызовы POSIX
    pwd — The password database                             — База паролей
    grp — The group database                                — База данных группы
    termios — POSIX style tty control                       — элемент управления tty в стиле POSIX
    tty — Terminal control functions                        — Функции управления терминалом
    pty — Pseudo-terminal utilities                         — Псевдотерминальные утилиты
    fcntl — The fcntl and ioctl system calls                — Системные вызовы fcntl и ioctl
    resource — Resource usage information                   — Информация об использовании ресурсов
    syslog — Unix syslog library routines                   — подпрограммы библиотеки системного журнала Unix

Superseded Modules                      Замененные модули
    aifc — Read and write AIFF and AIFC files               — Чтение и запись файлов AIFF и AIFC
    asynchat — Asynchronous socket command/response handler — обработчик команды/ответа асинхронного сокета
    asyncore — Asynchronous socket handler                  — обработчик асинхронного сокета
    audioop — Manipulate raw audio data                     — Манипулировать необработанными аудиоданными
    cgi — Common Gateway Interface support                  — поддержка общего интерфейса шлюза
    cgitb — Traceback manager for CGI scripts               — Менеджер трассировки для CGI-скриптов
    chunk — Read IFF chunked data                           — Считайте данные, разбитые на блоки IFF
    crypt — Function to check Unix passwords                — Функция для проверки паролей Unix
    imghdr — Determine the type of an image                 — Определить тип изображения
    imp — Access the import internals                       — Доступ к внутренним компонентам импорта
    mailcap — Mailcap file handling                         — Обработка файла Mailcap
    msilib — Read and write Microsoft Installer files       — Чтение и запись файлов установщика Microsoft
    nis — Interface to Sun’s NIS (Yellow Pages)             — Интерфейс к Sun’s NIS (Желтые страницы)
    nntplib — NNTP protocol client                          — клиент протокола NNTP
    optparse — Parser for command line options              — Анализатор параметров командной строки
    ossaudiodev — Access to OSS-compatible audio devices    — Доступ к OSS-совместимым аудиоустройствам
    pipes — Interface to shell pipelines                    — Интерфейс к конвейерам оболочки
    smtpd — SMTP Server                                     — SMTP-сервер
    sndhdr — Determine type of sound file                   — Определить тип звукового файла
    spwd — The shadow password database                     — база данных теневых паролей
    sunau — Read and write Sun AU files                     — Чтение и запись файлов Sun AU
    telnetlib — Telnet client                               — Telnet-клиент
    uu — Encode and decode uuencode files                   — кодировать и декодировать файлы uuencode
    xdrlib — Encode and decode XDR data                     — кодирует и декодирует данные XDR

Security Considerations                Вопросы безопасности
