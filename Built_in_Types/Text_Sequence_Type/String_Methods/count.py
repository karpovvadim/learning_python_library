"""str.count(sub[, start[, end]])"""  # подсчет подстроки
# Возвращает количество непересекающихся вхождений подстроки sub в диапазоне [начало,
# конец]. Необязательные аргументы start и end интерпретируются как в нотации среза.
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
count = vowels.count('i')
print('The count of i is:', count)
count = vowels.count('p')
print('The count of p is:', count)

random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
count = random.count(('a', 'b'))
print("The count of ('a', 'b') is:", count)
count = random.count([3, 4])
print("The count of [3, 4] is:", count)
