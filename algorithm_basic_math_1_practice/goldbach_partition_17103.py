from itertools import combinations
import math

t_c = int(input())

for _ in range(t_c):
    count = 0
    n = int(input())

    array = [True] * (n + 1)
    combination_array = []

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    for i in range(2, n + 1):
        if array[i]:
            combination_array.append(i)

    for i in list(combinations(combination_array, 2)):
        a, b = i
        if a + b == n:
            count += 1
        elif a + a == n:
            count += 1

    print(count)
