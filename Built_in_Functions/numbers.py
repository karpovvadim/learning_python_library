print("--0----abs------------------------------------------------")
x = -15.254
print(x, "abs =", abs(x))     #  abs
x2 = complex(15, 4)    #  complex(15, 4)
print(x2, "abs =", abs(x2))    #  abs

print("--1------hex----------------------------------------------")
number = 435
print(number, 'in hex =', hex(number))
number = 0
print(number, 'in hex =', hex(number))
number = -34
print(number, 'in hex =', hex(number))
returnType = type(hex(number))
print('Return type from hex() is', returnType)

print("--2---binary---Changed in version 3.7: x is now a positional-only parameter.-----")
print(3, bin(3))     # binary
print(-10, bin(-10))
print(14, -14, '=>', format(14, '#b'), format(-14, 'b'))
print(14, f'{14:#b}', f'{14:b}')

print("--3----oct----------------------------------------------")
print('oct(8) is:', oct(8))   # decimal to octal
print('oct(0b1010) is:', oct(0b1010))  # binary to octal
print('oct(0XA) is:', oct(0XA))   # hexadecimal to octal
class Person:
    age = 23

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print('The oct is:', oct(person))
# Класс Person реализует __index __() и __int __(). Мы можем использовать oct() для объектов Person.
# Примечание.
# Для совместимости рекомендуется реализовать __int __() и __index __() с одним и тем же выводом.


print("--4-----class bool--------------------------------------")
x = 8   # -0.5; True; complex; Если x ложно или опущено, возвращается False;
y = False
print(bool(False))  # в противном случае возвращается True.
print(bool(x))
print(bool())
print(bool(y))

print("--5-----------class float------------------------------")
print(float('+1.23'))
print(float('   -12345\n'))
print(float('1e-003'))
print(float('+1E6'))
# for inf/infinity
print(float('-Infinity'))
print(float("inf"))
print(float("InF"))
print(float("InFiNiTy"))
print(float("infinity"))
# for NaN
print(float("nan"))
print(float("NaN"))
print("---6-----Функция pow()-------------------------------------")
# Функция pow() возвращает степень числа.
# Синтаксис:
"""pow(x, y, z)"""
# Функция pow() в Python принимает три параметра:
# x — число, основание.
# y — число, показатель степени.
# z (необязательно) — число, используемое для модуля.
# Следовательно,
# pow (x, y) равно x**y
# pow (x, y, z) равно x**y % z

print(pow(2, 2))   # positive x, positive y (2**2) # 4
print(pow(-2, 2))  # negative x, positive y  # 4
print(pow(2, -2))  # positive x, negative y (1/2**2) # 0.25
print(pow(-2, -2))  # negative x, negative y # 0.25
print("----7---pow() с тремя аргументами (x ** y) % z----------------")
x = 7
y = 2
z = 5
print(pow("7, 2, 5", x, y, z))    # 4