from itertools import combinations

dwarfs = []
new_array = []
for i in range(9):
    dwarfs.append(int(input()))

for i in list(combinations(dwarfs, 7)):
    if sum(i) == 100:
        new_array = i

new_array = list(new_array)
new_array.sort()
print("\n".join(map(str, new_array)))
