""" os.get_exec_path(env=None)"""
# Возвращает список каталогов, в которых будет выполняться поиск именованного
# исполняемого файла, аналогичного оболочке, при запуске процесса. env, если он
# указан, должен быть словарем переменных среды для поиска PATH. По умолчанию,
# когда env имеет значение None, используется environ.
#       Новое в версии 3.2.
import os

path = os.get_exec_path()
print(path)
for i in path:
    print(i)
print(os.get_exec_path({'PATH': '/usr/local/bin:/usr/sbin:/usr/bin:/sbin'}))

