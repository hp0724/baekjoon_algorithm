#중복 조합
from itertools import combinations_with_replacement
n,m = map(int,input().split())
array = [i for i in range(1,n+1)]

for i in combinations_with_replacement(array,m):
    print(" ".join((map(str,i))))