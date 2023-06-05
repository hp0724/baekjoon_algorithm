import sys


def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):  # 4,1000000,2
                primes[i] = False
        p += 1

    return primes


MAX = 1000000
primes = sieve_of_eratosthenes(MAX)

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    found = False
    for i in range(3, n // 2 + 1, 2):
        if primes[i] and primes[n - i]:
            print("{} = {} + {}".format(n, i, n - i))
            found = True
            break

    if not found:
        print("Goldbach's conjecture is wrong.")
