            Text Sequence Type — str
            Тип текстовой последовательности str

Текстовые данные в Python обрабатываются с помощью объектов str или строки. Строки являются 
неизменяемыми последовательностями кодовых точек Юникода. Строковые литералы записываются
разными способами:

    Одинарные кавычки: 'allows embedded "double" quotes'
    Двойные кавычки: "allows embedded 'single' quotes".
    Тройные кавычки: '''Three single quotes''', """Three double quotes"""

Строки в тройных кавычках могут занимать несколько строк — все связанные пробелы будут
включены в строковый литерал.

Строковые литералы, которые являются частью одного выражения и имеют только пробелы между 
ними, будут неявно преобразованы в один строковый литерал. То есть 
("spam " "eggs") == "spam eggs".

См. Строковые и байтовые литералы для получения дополнительной информации о различных формах
строкового литерала, включая поддерживаемые escape-последовательности, и префикс r (“raw”)
(«необработанный»), который отключает большую часть обработки escape-последовательностей.

Строки также могут быть созданы из других объектов с помощью конструктора str.

Поскольку не существует отдельного «символьного» типа, при индексировании строки получаются
строки длиной 1. То есть для непустой строки s, s[0] == s[0:1].

Также не существует изменяемого строкового типа, но str.join() или io.StringIO можно
использовать для эффективного построения строк из нескольких фрагментов.

Изменено в версии 3.3: Для обратной совместимости с серией Python 2 префикс u снова разрешён
для строковых литералов. Он не влияет на значение строковых литералов и не может сочетаться
с префиксом r.
