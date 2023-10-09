# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

numbers = [2, 3, 2, 3, 1, 1, 5, 20, 20, 30]

# Вариант 1
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(len(result))


# Вариант 2
'''result = []
for num in numbers:
    if result.count(num) == 0:
        result.append(num)
print(len(result))'''
