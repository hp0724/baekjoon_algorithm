n = int(input())
prime = list(map(int, (input().split())))
cnt = 0
prime_cnt = 0
for i in prime:
    for j in range(2, i + 1):
        if i % j == 0:
            prime_cnt += 1
    if prime_cnt == 1:
        cnt += 1
    prime_cnt = 0
print(cnt)
