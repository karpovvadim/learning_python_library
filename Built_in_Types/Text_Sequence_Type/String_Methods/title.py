"""str.title()"""   # заглавие
# Возвращает версию строки в заглавном регистре, в которой слова начинаются с прописных
# букв, а остальные символы — строчными.

print('Hello world'.title())

# Алгоритм использует простое независимое от языка определение слова как группы
# последовательных букв. Это определение работает во многих контекстах, но оно означает,
# что апострофы в сокращениях и притяжательных падежах образуют границы слов, что может
# быть нежелательным результатом:

print("they're bill's friends from the UK".title())

# Функция string.capwords() не имеет этой проблемы, так как она разбивает слова только
# по пробелам.
# В качестве альтернативы обходной путь для апострофов может быть построен с
# использованием регулярных выражений:

import re


def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)


print(titlecase("they're bill's friends."))
