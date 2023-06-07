n = int(input())
stack = []
ans = ""

if n == 0:
    ans = 0
while n:
    if n % -2:
        stack.append(abs(n % -2))
        n = (n // -2) + 1

    else:
        stack.append(n % -2)
        n = n // -2

while stack:
    ans += str(stack.pop())


print(ans)
