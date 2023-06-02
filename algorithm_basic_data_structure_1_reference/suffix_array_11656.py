import sys
from collections import deque

s = list(sys.stdin.readline().rstrip())
deque_s = deque(s)

new_array = []
for i in s:
    new_array.append(list(deque_s))
    deque_s.popleft()
new_array.sort()
for i in new_array:
    print("".join(map(str, i)))
