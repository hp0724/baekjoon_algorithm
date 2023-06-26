import math

t_c = int(input())

for _ in range(t_c):
    # 10 12 3 9
    m, n, x, y = map(int, input().split())
    # 최소 공배수
    lcm_val = (m * n) // math.gcd(m, n)

    while x <= lcm_val:
        if (x - y) % n == 0:
            print(x)
            break
        x += m
    else:
        print(-1)
