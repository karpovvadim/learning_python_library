"""os.startfile(path[, operation][, arguments][, cwd][, show_cmd])"""
#                         Доступность: Windows.
#      Запустите файл со связанным с ним приложением.
#      Когда операция не указана или не «открыта», это действует как двойной щелчок по
# файлу в проводнике Windows или указание имени файла в качестве аргумента команде
# запуска из интерактивной командной оболочки: файл открывается в любом приложении
# (если оно есть). ) связано его расширение.
#      Когда задается другая операция, это должен быть «командный глагол», указывающий,
# что следует делать с файлом. Обычными глаголами, задокументированными Microsoft,
# являются «распечатать» и «редактировать» (для использования в файлах), а также
# «исследовать» и «найти» (для использования в каталогах).
#      При запуске приложения укажите аргументы, которые будут передаваться в виде одной
# строки. Этот аргумент может не иметь никакого эффекта при использовании этой функции для
# запуска документа.
#      Рабочий каталог по умолчанию наследуется, но может быть переопределен аргументом
# cwd. Это должен быть абсолютный путь. Относительный путь будет разрешен для этого
# аргумента.
#      Используйте show_cmd, чтобы переопределить стиль окна по умолчанию. Будет ли это
# иметь какой-либо эффект, будет зависеть от запускаемого приложения. Значения
# представляют собой целые числа, поддерживаемые функцией Win32 ShellExecute().
#      startfile() возвращается сразу после запуска связанного приложения. Нет
# возможности ждать, пока приложение закроется, и нет возможности получить статус выхода
# приложения. Параметр пути относится к текущему каталогу или cwd. Если вы хотите
# использовать абсолютный путь, убедитесь, что первый символ не является косой чертой ('/').
# Используйте pathlib или функцию os.path.normpath(), чтобы убедиться, что пути правильно
# закодированы для Win32.
#      Чтобы уменьшить нагрузку на запуск интерпретатора, функция Win32 ShellExecute()
# не разрешается до первого вызова этой функции. Если функция не может быть разрешена,
# будет вызвана ошибка NotImplementedError.
#      Вызывает событие аудита os.startfile с аргументами path, operation(путь, операция).
#      Вызывает событие аудита os.startfile/2 с аргументами  path, operation, arguments,
# cwd, show_cmd (путь, операция, аргументы, cwd, show_cmd).
#      Доступность: Windows.
#      Изменено в версии 3.10: добавлены аргументы, аргументы cwd и show_cmd, а также
# событие аудита os.startfile/2.
import os
os.startfile('test.docx', 'edit')
os.startfile('test.txt', 'edit')