# Найдите сумму цифр трехзначного числа. 

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = 123

a = n // 100
b = n // 10 % 10
c = n % 10
res = a + b + c

print( res )