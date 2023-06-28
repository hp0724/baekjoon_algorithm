from itertools import combinations_with_replacement
n,m = map(int ,input().split())
array=list(map(int,input().split()))
new_array=[]
array.sort()
# print(array_set)
for i in combinations_with_replacement(array,m):
    new_array.append(i)

new_array=set(new_array)  
new_array =list(new_array)
new_array.sort()
for i in new_array:
    print(" ".join(map(str,i)))