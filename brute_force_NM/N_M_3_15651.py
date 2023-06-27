#중복 순열 
from itertools import product
n,m = map(int,input().split())
array = [i for i in range(1,n+1)]

for i in product(array,repeat=m):
    print(" ".join((map(str,i))))