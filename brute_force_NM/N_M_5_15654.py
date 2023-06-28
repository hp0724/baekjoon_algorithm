from itertools import permutations

n,m = map(int,input().split())
array = list(map(int,input().split()))
array.sort()

for i in permutations(array,m):
    print(" ".join(map(str,i)))