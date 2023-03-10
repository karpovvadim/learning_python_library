# 1. У t должна быть та же длина, что и заменяемая нарезка.

print("-----s[i:j] = t-------s.append(x)--------------------")
s = [1, 2, 3, 4, 5]
print("s =", s)
t = [20, 30]
s[1:3] = t
print("s =", s)
s.append(75)
print("s.append(75) =", s)
s[len(s):len(s)] = [100]
print("s[len(s):len(s)] =", s)

print("\n-----s.extend(t)---------------")
s = ['один', 'два', 'три', 'четыре', 'пять']
s2 = ['шесть',  'семь']
s.extend(s2)
print("s.extend(s2) =", s)
t = ['один', 'два']
s += t
print(s)
s[len(s):len(s)] = t
print(s)

# 2. Необязательный аргумент i по умолчанию равен -1, так что по умолчанию последний
# элемент удаляется и возвращается.
print("\n------s.pop[i]----------------------------------")
s = ['один', 'два', 'три', 'четыре', 'пять']
print("s =", s)
removed = s.pop()
print("s.pop() =", s)
print("removed =", removed)
removed = s.pop(1)
print("s.pop(1) =", s)
print("removed =", removed)

# 3. remove() вызывает ValueError, если x не находится в s.

print("\n------s.remove(x) ---------------------------------")
s = ['один', 'два', 'три', 'четыре', 'пять']
s.remove('два')
print("s.remove('два') =", s)

# 4. Метод reverse() изменяет существующую последовательность для экономии места при
# обращении большой последовательности. Чтобы напомнить пользователям, что он работает
# как побочный эффект, он не возвращает обратную последовательность.

print("\n------s.reverse()-----------------------------------")
s = [1, 2, 3, 4, 5]
s.reverse()
print("s.reverse() =", s)

# 5. clear() и copy() включены для согласованности с интерфейсами изменяемых контейнеров,
# которые не поддерживают операции нарезки (например, dict и set). copy() не является
# частью collections.abc.MutableSequence ABC, но большинство классов изменяемых
# последовательностей предоставляют его.
# Добавлено в версии 3.3: Методы clear() и copy().

print("\n-----s.clear()----s.copy()----del s[i:j:k]-------------")
s = ['один', 'два', 'три', 'четыре', 'пять']
print("s =", s)
s.clear()
print("s.clear() =", s)
s = ['один', 'два', 'три', 'четыре', 'пять']
del s[1:5:2]
print("del s[1:5:2] =", s)
s = ['один', 'два', 'три', 'четыре', 'пять']
s1 = s.copy()
print("s.copy() =", s1)
s = ['один', 'два', 'три', 'четыре', 'пять']
del s[:]
print("del s[:] = ", s)
s = ['один', 'два', 'три', 'четыре', 'пять']
del s[2:]
print("del s[2:] = ", s)

# 6. Значение n является целым числом или объектом, реализующим __index__(). Нулевые и
# отрицательные значения n очищают последовательность. Элементы в последовательности не
# копируются; на них ссылаются несколько раз, как описано для s * n в разделе
# Общие последовательные операции.

print("\n-----s *= n-----------------------------------------")
s = ['один', 'два', 'три', 'четыре', 'пять']
print(s * 2)
print(s * -2)

print("\n-----s.insert(i, x)-------------------------------")
s = [1, 2, 3, 4, 5]
s.insert(1, 'Привет')
print("s.insert(1, 'Привет') =", s)
