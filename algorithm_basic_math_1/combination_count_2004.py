from math import factorial

n, m = map(int, input().split())
combination = factorial(n) / ((factorial(m) * factorial(n - m)))

combination = str(int(combination))
count_0 = 0


print(count_0)
