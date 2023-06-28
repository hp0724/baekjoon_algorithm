from itertools import permutations
n,m = map(int ,input().split())
array=list(map(int,input().split()))
new_array=[]
# print(array_set)
for i in permutations(array, m):
    new_array.append(i)

new_array=set(new_array)
new_array= list(new_array)
new_array.sort()
for i in new_array:
    print(" ".join(map(str,i)))