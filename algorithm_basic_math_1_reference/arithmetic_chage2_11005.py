n, b = map(int, input().split())
stack = []
if n == 0:
    stack.append(0)
while n:
    reminder = n % b
    stack.append(reminder)
    n = n // b


while stack:
    n = stack.pop()
    if n >= 10:
        print(chr(n + 55), end="")
    else:
        print(n, end="")

# 15 8
