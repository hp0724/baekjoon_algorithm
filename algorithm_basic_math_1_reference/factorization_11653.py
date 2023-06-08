n = int(input())
i = 2
array = []
while n != 1:
    if n % i == 0:
        n = n // i
        array.append(i)
        i = 2

    else:
        i = i + 1
print("\n".join(map(str, array)))
