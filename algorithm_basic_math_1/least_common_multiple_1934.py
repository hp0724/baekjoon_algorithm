for _ in range(int(input())):
    a, b = map(int, input().split())
    gcd = 0
    lcm = 0
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    if a == b:
        lcm = gcd * (a // gcd)
    else:
        lcm = gcd * (a // gcd) * (b // gcd)

    print(lcm)
