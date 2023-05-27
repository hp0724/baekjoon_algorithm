from collections import deque
import sys

edit_string = sys.stdin.readline().strip().split()
m = int(input())

left_stack = deque(edit_string)  # 왼쪽 스택
right_stack = deque()  # 오른쪽 스택

for _ in range(m):
    cmd = input().split()
    if cmd[0] == "L":
        if left_stack:
            right_stack.appendleft(left_stack.pop())

    elif cmd[0] == "D":
        if right_stack:
            left_stack.append(right_stack.popleft())

    elif cmd[0] == "B":
        if left_stack:
            left_stack.pop()

    elif cmd[0] == "P":
        left_stack.append(cmd[1])

result = "".join(left_stack) + "".join(right_stack)
print(result)
