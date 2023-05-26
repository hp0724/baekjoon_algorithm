# [4 3 6 8 7 5 2 1]
n = int(input())
sequence = []
stack = []
result = []
count = 1
for _ in range(n):
    x = int(input())
    sequence.append(x)

# 해당 숫자까지 count 늘리고 +
for num in sequence:
    while count <= num:
        stack.append(count)
        result.append("+")
        count += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

for op in result:
    print(op)
