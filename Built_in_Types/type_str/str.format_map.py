print("-------str.format_map(mapping)----------------------------------")
# Аналогичен str.format(**mapping), за исключением того, что mapping  используется
# напрямую, а не копируется в словарь. Это полезно, если, например, mapping  является
# подклассом dict:


class Default(dict):
    def __missing__(self, key):
        return key


print('{name} was born in {country}'.format_map(Default(name='Guido')))
print('({x}, {y})'.format_map(Default(x='6')))
print('({x}, {y})'.format_map(Default(y='5')))
print('({x}, {y})'.format_map(Default(x='6', y='5')))
# New in version 3.2.

# Метод format_map() похож на str.format (** mapping), за исключением того,
# что str.format (** mapping) создает новый словарь, а str.format_map (mapping) ‒ нет.
print("------str.format (**mapping) для словарей Python---------------")
point = {'x': 4, 'y': -5}
print('{x} {y}'.format(**point))
print("-------str.format_map(mapping)----------------------------------")
# Единственная разница в том, что str.format (** mapping) копирует dict, тогда как
# str.format_map (mapping) создает новый словарь во время вызова метода.
# Это может быть полезно, если вы работаете с подклассом dict.
print('{x} {y}'.format_map(point))
point = {'x': 4, 'y': -5, 'z': 0}
print('{x} {y} {z}'.format_map(point))
# str.format_map(mapping) более гибкий, чем str.format (**mapping), так как у вас могут
# отсутствовать ключи.
