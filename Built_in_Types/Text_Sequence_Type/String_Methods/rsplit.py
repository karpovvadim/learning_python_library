"""str.rsplit(sep=None, maxsplit=- 1)"""   # расколоть
# Возвращает список слов в строке, используя sep в качестве строки-разделителя. Если задано
# значение maxsplit, выполняется не более maxsplit, самые правые. Если sep не указан или
# None, любая строка пробела является разделителем. За исключением разделения справа,
# rsplit() ведет себя как split(), который подробно описан ниже.

text = 'Love thy neighbor'
print(text.rsplit('t'))  # splits at space
print(text.rsplit(maxsplit=0))
print(text.rsplit(maxsplit=1))
grocery = 'Milk, Chicken, Bread'
print("\n", grocery.rsplit(', '))  # splits at ','    распадается на
print('', grocery.rsplit(':'))  # Splitting at ':'  Разделение на

grocery = 'Milk, Chicken, Bread, Butter'
print("\n", grocery.rsplit(sep=', ', maxsplit=0))  # maxsplit: 0
print("", grocery.rsplit(', ', 1))  # maxsplit: 1
print('', grocery.rsplit(', ', 2))  # maxsplit: 2
print('', grocery.rsplit(', ', 5))  # maxsplit: 5
