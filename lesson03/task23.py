# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

numbers = [0, 1, 5, 2, 3]

# Вариант 1
count = 0
for i in range(len(numbers)):  # Проходим циклом от 1, а не от 0
    if numbers[i] > numbers[i - 1]:
        count += 1
print(count)