# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def rever(n):
    if n == 0:
        return ''
    num = input()
    return rever(n - 1) + ' ' + num

print(rever(3))

#    rever(3) ' 11 10 9 '
#        rever(2) + ' ' + 10 ' 11 10'
#           rever(1) + ' ' + 11 => ' 11'
#               rever(0) ''