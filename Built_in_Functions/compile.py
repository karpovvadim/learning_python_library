# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# Параметры:
# source - обязательный параметр. Может быть обычной строкой, байтовой строкой,
# либо объектом абстрактного синтаксического дерева.
# filename - обязательный параметр. Имя файла, из которого будет читается код. Если код
# не будет считан из файла, вы можете написать в качестве параметра любую строку <string>.
# mode - обязательный параметр. Может принимать 3 значения:
#     eval, если источником является одно выражение;
#     exec,если источником является блок операторов;
#     single, если код состоит из одного оператора;
# flag - необязательный параметр. По умолчанию flags=0 и определяет, будет ли
# скомпилированный код содержать асинхронные операции или какие инструкции из
# __future__ следует использовать. Указывается битами. Если нужно задать несколько
# инструкций, то их можно указывать через or;
# dont_inherit - необязательный параметр. По умолчанию dont_inherit=False. Указывает,
# следует ли использовать future определенные в коде, в дополнение в тем, что указаны во flags;
# optimize - необязательный параметр. По умолчанию optimize=-1.
# Задаёт уровень оптимизации компилятора:
#     -1 — использовать настройки интерпретатора (регулируются опцией -O);
#     0 — не оптимизировать, включить debug;
#     1 — убрать инструкции asserts, выключить debug;
#     2 — то, что делает 1 + убрать строки документации.
#
# Возвращаемое значение:
#     объекта кода, готовый к выполнению.
# Описание:
# Функция compile() возвращает переданный, в качестве аргумента источник, в виде объекта кода,
# готового к выполнению. Объекты кода, полученные в результате выполнения функции compile()
# могут быть выполнены с помощью exec() или eval().
# Функция compile() бросает исключение SyntaxError, если скомпилированный источник недопустим
# и ValueErrorесли, если источник содержит нулевые байты.
# Заметка:
# При компиляции строки с многострочным кодом в режиме single или eval, ввод должен
# заканчиваться хотя бы одним символом новой строки '\n'. Это должно облегчить обнаружение
# неполных и полных операторов в модуле code.
# Предупреждение:
# При компиляции в объект AST(абстрактного синтаксического дерева) возможен сбой интерпретатора
# Python с большой(сложной) строкой из-за ограничений глубины стека в компиляторе AST Python
# ast — Abstract Syntax Trees¶.
# Изменено в Python 3.5: Ранее TypeError вызывалось, когда в источнике встречались нулевые байты.
# Новое в Python 3.8: ast.PyCF_ALLOW_TOP_LEVEL_AWAIT теперь можно передать через
# необязательный параметр flag, чтобы обеспечить поддержку await и async.
# Пример компиляции строки кода с последующем выполнением.

# выполнение в exec
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct_1 = compile(codeInString, 'sumstring', 'exec')
exec(codeObejct_1)

# выполнение в eval
codeInEval = "print('4 + 5 =', 4+5)"
codeObejct_2 = compile(codeInEval, 'test', 'eval')
eval(codeObejct_2)
