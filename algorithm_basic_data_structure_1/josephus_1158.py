# from collections import deque

n, k = map(int, input().split())
q = [i for i in range(1, n + 1)]
result = []

# 리스트에서 하나 빠지는것도 고려
# 개수 넘어가는것도 고려
i = k - 1  # 2
while True:
    result.append(q.pop(i))  # 2
    # print(i, q.pop(i), len(q))  # 3 6 4
    if len(q) == 0:
        break
    elif (i + (k - 1)) >= len(q):
        i = (i + (k - 1)) % len(q)
    else:  # 4
        i = i + (k - 1)

print("<" + ", ".join(map(str, result)) + ">")
