from itertools import product

n,m = map(int,input().split())
array = list(map(int,input().split()))
array.sort()

for i in product(array,repeat=m):
    print(" ".join(map(str,i)))