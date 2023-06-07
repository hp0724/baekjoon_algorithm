primes = [False, False] + [True] * 999999


for i in range(2, 1000001):
    if primes[i]:
        for j in range(i * 2, 1000001, i):
            primes[j] = False

t_c = int(input())

for _ in range(t_c):
    count = 0
    n = int(input())
    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            count += 1

    print(count)
