"""str.isalnum()"""   # буква-цифра
# Возвращает True, если все символы в строке буквенно-цифровые и есть хотя бы один символ,
# в противном случае возвращает False. Символ c является буквенно-цифровым, если одно из
# следующих значений возвращает True: c.isalpha(), c.isdecimal(), c.isdigit() или
# c.isnumeric().     	Состоит ли строка из цифр или букв

name = "M234onica"
print(name.isalnum())
name = "M3onica Gell22er "  # contains whitespace (содержит пробелы)
print(name.isalnum())
name = "Mo3nicaGell22er"
print(name.isalnum())
name = "133"
print(name.isalnum())
