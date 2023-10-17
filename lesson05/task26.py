# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

def f(x,y):
    if y == 1 :
        return x
    return x * f(x,y - 1)

a = int(input("Введите число а :\n"))
b = int(input("Введите число а :\n"))

print(f(a,b))