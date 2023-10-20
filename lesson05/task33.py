# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# минимальные – на максимальные.

seq = [2, 4, 2, 5, 3]
mx = 0
mn = 6
for el in seq:
    if el > mx:
        mx = el
    if el < mn:
        mn = el
# for i in range(len(seq)):
#       if seq[i] == mn:
#           seq[i] = mx
# print(*seq)

print([mx if seq[i] == mn else seq[i]
        for i in range(len(seq)) if mx >= 4 and seq[i] >= 4])