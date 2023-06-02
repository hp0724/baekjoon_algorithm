num1, num2 = map(int, input().split())
gcd = 0
lcm = 0
for i in range(1, max(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

if num1 == num2:
    lcm = gcd * (num1 // gcd)
else:
    lcm = gcd * (num1 // gcd) * (num2 // gcd)
print(gcd)
print(lcm)
