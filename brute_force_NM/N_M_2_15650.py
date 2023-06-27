from itertools import combinations
n,m = map(int,input().split())
array = [i for i in range(1,n+1)]

for i in combinations(array,m):
    print(" ".join((map(str,i))))