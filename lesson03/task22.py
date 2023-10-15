#  Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Enter the count: "))
m = int(input("Enter the count: "))

list1 = []
list2 = []

for i in range(n) :
    list1.append(int(input("Enter an integer: ")))
    
print(f"list1 => {list1}")
    
for j in range(m) :
    list2.append(int(input("Enter an integer: ")))
    
print(f"list2 => {list2}")
    
set1 = set(list1)
set2 = set(list2)

print(sorted(set1 & set2))
      