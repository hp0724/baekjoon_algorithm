from itertools import combinations


t_c = int(input())
sum = 0
for _ in range(t_c):
    n = list(map(int, input().split()))

    n.pop(0)

    for i in list(combinations(n, 2)):
        a, b = i

        while a != b:
            if a > b:
                a -= b
            else:
                b -= a

        sum += a
    print(sum)

    sum = 0
