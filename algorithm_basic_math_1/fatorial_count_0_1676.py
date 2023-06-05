from math import factorial

n = int(input())

factorial_str = str(factorial(n))
count_0 = 0

for i in factorial_str[::-1]:
    if i != "0":
        break
    count_0 += 1


print(count_0)
