# Даны два целых числа A и В.
# Выведите все числа от A до B включительно, в порядке возрастания,
# если A < B, или в порядке убывания, если A > B

def IntegersFromAtoB(num1, num2):

    if num1 == num2:
        return num2

    if num1 > num2:
        return f'{num1} {IntegersFromAtoB(num1 - 1, num2)}'

    if num1 < num2:
        return f'{num1} {IntegersFromAtoB(num1 + 1, num2)}'

a = int(input("Enter an integer A:\n"))
b = int(input("Enter an integer B:\n"))
print(IntegersFromAtoB(a, b))
        
    
    