from collections import deque
import sys

q = deque()
output = []
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        if q:
            output.append(q.popleft())
        else:
            output.append("-1")
    elif cmd[0] == "back":
        if q:
            output.append(q[-1])
        else:
            output.append("-1")
    elif cmd[0] == "front":
        if q:
            output.append(q[0])
        else:
            output.append("-1")
    elif cmd[0] == "size":
        output.append(len(q))
    elif cmd[0] == "empty":
        if q:
            output.append("0")
        else:
            output.append("1")

print("\n".join(map(str, output)))
