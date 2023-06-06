import math


n, x = map(int, input().split())

brother_position = list(map(int, input().split()))

brother_position.sort()


for i, v in enumerate(brother_position):
    if v > x:
        brother_position.insert(i, x)
        break

position_gcd = []
for i in range(len(brother_position) - 1):
    position_gcd.append(abs(brother_position[i + 1] - brother_position[i]))


gcd_get = position_gcd[0]
for i in position_gcd:
    gcd_get = math.gcd(gcd_get, i)

print(gcd_get)
