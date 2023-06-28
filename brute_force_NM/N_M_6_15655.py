from itertools import combinations

n,m = map(int,input().split())
array = list(map(int,input().split()))
array.sort()

for i in combinations(array ):
    print(" ".join(map(str,i)))