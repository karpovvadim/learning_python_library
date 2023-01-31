"""str.isupper()"""  # верхний  Как в программе используется?
# Возвращает True, если все символы [4] в строке в верхнем регистре и есть хотя бы один
# символ в регистре, в противном случае — False.
# [4] - Кодированные символы — это символы с общим свойством категории
# «Lu» (буква, заглавная буква), «Ll» (буква, строчная буква) или
# «Lt» (буква, заглавный регистр).
#               	Состоит ли строка из символов в верхнем регистре
string = "this should be uppercase!"
print(string.isupper())
string = "Th!s Sh0uLd B3 uPp3rCas3!"  # string with numbers
print(string.isupper())
firstString = "python is awesome!"
secondString = "PyThOn Is AwEsOmE!"
if firstString.isupper() == secondString.isupper():
    print("The strings are same.")
else:
    print("The strings are not same.")

string = "HELLO"
print("\n", string.isupper())
string = "HELLO WORLD!"
print("\n", string.isupper())
