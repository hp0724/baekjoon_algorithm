import sys

n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
right_big_number = []
for i in range(n):
    # 3 5 2 7
    popValue = data.pop(i)  # 3
    is_insert = False
    for idx, num in enumerate(data):
        if num > popValue and idx >= i:
            is_insert = True
            right_big_number.append(num)
            break

    if is_insert == False:
        right_big_number.append(-1)

    data.insert(i, popValue)
print(right_big_number)
