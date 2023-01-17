Модули, описанные в этой главе, работают с файлами и каталогами на диске.
Например, есть модули для чтения свойств файлов, переносимого управления путями
и создания временных файлов. Полный список модулей в этой главе:

pathlib — Object-oriented filesystem paths Пути объектно-ориентированной файловой системы
    Basic use                 Основное использование
    Pure paths                Чистые пути
        General properties    Общие свойства
        Operators             Операторы
        Accessing individual parts    Доступ к отдельным частям
        Methods and properties    Методы и свойства
    Concrete paths        Бетонные дорожки
        Methods            Методы
    Correspondence to tools in the os module    Соответствие инструментам в модуле os
os.path — Common pathname manipulations         общие манипуляции с путями
fileinput — Iterate over lines from multiple input streams  Итерация по строкам из нескольких входных потоков
stat — Interpreting stat() results             Интерпретация результатов stat()
filecmp — File and Directory Comparisons       Сравнение файлов и каталогов
    The dircmp class                           Класс dircmp
tempfile — Generate temporary files and directories  Создает временные файлы и каталоги
    Examples
    Deprecated functions and variables         Устаревшие функции и переменные
glob — Unix style pathname pattern expansion   Расширение шаблона пути в стиле Unix
fnmatch — Unix filename pattern matching     сопоставление имен файлов Unix с образцом
linecache — Random access to text lines      Произвольный доступ к текстовым строкам
shutil — High-level file operations          Высокоуровневые файловые операции.
    Directory and files operations           Операции с каталогами и файлами
        Platform-dependent efficient copy operations  Платформозависимые эффективные операции копирования
        copytree example       пример копировального дерева
        rmtree example         пример rmtree
    Archiving operations        Архивные операции
        Archiving example            Пример архивации
        Archiving example with base_dir            Пример архивации с base_dir
    Querying the size of the output terminal       Запрос размера выходного терминала

