import sys

left_stack = []
right_stack = []

edit_string = sys.stdin.readline().strip()
for char in edit_string:
    left_stack.append(char)

m = int(sys.stdin.readline())

for _ in range(m):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == "P":
        left_stack.append(cmd[1])

    elif cmd[0] == "B":
        if left_stack:
            left_stack.pop()

    elif cmd[0] == "L":
        if left_stack:
            right_stack.append(left_stack.pop())

    elif cmd[0] == "D":
        if right_stack:
            left_stack.append(right_stack.pop())

result = "".join(left_stack) + "".join(reversed(right_stack))
print(result)
