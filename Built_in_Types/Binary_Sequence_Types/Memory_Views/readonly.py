""" readonly"""

# Логическое значение, указывающее, доступна ли память только для чтения.
import array

a = array.array('l', [1, 2, 3])
x = memoryview(a)
print(x.readonly)

mx = x.toreadonly()
print(mx.readonly)
