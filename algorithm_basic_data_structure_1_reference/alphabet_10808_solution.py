alphabet = input()
dic = {}
for chr in "abcdefghijklmnopqrstuvwxyz":
    dic[chr] = 0

for chr in alphabet:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1

print(" ".join(map(str, dic.values())))
