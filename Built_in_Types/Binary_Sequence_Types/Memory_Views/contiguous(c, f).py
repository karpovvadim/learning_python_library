"""c_contiguous"""
# Логическое значение, указывающее, является ли память смежной, C-смежной
# или Fortran-смежной.

import array

a = array.array('l', [1, 2, 3])
x = memoryview(a)

print(x.contiguous)
print(x.c_contiguous)
print(x.f_contiguous)

#     Добавлено в версии 3.3.
