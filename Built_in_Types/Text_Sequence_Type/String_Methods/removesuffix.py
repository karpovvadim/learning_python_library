"""str.removesuffix(suffix, /)"""   # удалить суффикс
# Если строка заканчивается строкой суффикса, и этот суффикс не пуст, вернуть
# string[:-len(suffix)]. В противном случае верните копию исходной строки:

print('MiscTests'.removesuffix('Tests'))
print("[:-len('Tests')] =", "MiscTests"[:-len('Tests')])
print('TmpDirMixin'.removesuffix('Tests'))
# New in version 3.9.
