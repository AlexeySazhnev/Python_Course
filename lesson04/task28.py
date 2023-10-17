# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 3, 5 -> 8
# 2, 2 -> 4


def sum(num1, num2):
    if num2 == 0:
        return num1
    elif num1 == 0:
        return num2
    else:
        return sum(num1 + 1, num2 - 1)

a = int(input("Enter num1: \n"))
b = int(input("Enter num2: \n"))

print(f"Сумма чисел {a} и {b} -> {sum(a, b)}")
