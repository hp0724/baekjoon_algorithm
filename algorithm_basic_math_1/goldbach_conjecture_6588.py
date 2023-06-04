import math

while True:
    n = int(input())
    new_array = []
    if n == 0:
        break
    array = [True for _ in range(n + 1)]
    array[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    for i in range(2, n):
        if array[i] and i % 2 == 1:
            new_array.append(i)

    for i in new_array:
        if n - i in new_array:
            print("{} = {} + {}".format(n, i, n - i))
            break
