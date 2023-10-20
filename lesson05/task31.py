# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 21

# Решение с for

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b # обмен значениями
    return a 

print(fib(7))

# Решение через рекурсию

'''def fib_2(n):
    if n <= 1:
        return n
    return fib_2(n - 1) + fib_2(n - 2)'''

def fib_2(n):
    return n if n <=1 else fib_2(n - 1) + fib_2(n - 2)

print(fib_2(7))