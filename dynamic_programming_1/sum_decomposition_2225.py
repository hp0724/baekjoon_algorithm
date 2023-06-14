from itertools import product

n, k = map(int, input().split())
array = [i for i in range(n + 1)]
data = product(array, repeat=k)
count = 0
for i in data:
    if sum(i) == max(array):
        count += 1

print(count % 1000000000)
