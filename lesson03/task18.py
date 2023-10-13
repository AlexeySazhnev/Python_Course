# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# list_1 = [1, 2, 3, 4, 5]
# k = 6

#  5

list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 10

m = abs(k - list_1[0])  # функция abs помогает найти разницу между числами
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
        