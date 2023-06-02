import math

n, m = map(int, input().split())
prime_cnt = 0
for i in range(n, m + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            prime_cnt += 1
    if prime_cnt == 1:
        print(i)
    prime_cnt = 0
