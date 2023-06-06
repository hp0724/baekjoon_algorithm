import math

n, x = map(int, input().split())

brother_position = list(map(int, input().split()))

position_gcd = []
for i in range(n):
    position_gcd.append(abs(brother_position[i] - x))

gcd_get = position_gcd[0]
for i in position_gcd:
    gcd_get = math.gcd(gcd_get, i)

print(gcd_get)
