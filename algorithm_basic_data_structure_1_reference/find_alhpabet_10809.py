expression = input()
dic = {}

for i in "abcdefghijklmnopqrstuvwxyz":
    dic[i] = -1
# baekjoon
for index, value in enumerate(expression):
    if value in dic:
        if dic[value] == -1:
            dic[value] = index

print(" ".join(map(str, dic.values())))

# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 6 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
