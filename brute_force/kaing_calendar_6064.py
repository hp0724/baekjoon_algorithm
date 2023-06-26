t_c = int(input())

for _ in range(t_c):
    start_x = 0
    start_y = 0
    total = 0
    m, n, x, y = map(int, input().split())
    while total < 30000:
        start_x += 1
        start_y += 1
        total += 1
        if start_x == m + 1:
            start_x = 1
        if start_y == n + 1:
            start_y = 1
        if x == start_x and y == start_y:
            print(total)
            break
    else:
        print(-1)
