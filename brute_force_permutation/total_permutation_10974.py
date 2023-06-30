from itertools import permutations
n= int(input())
array = [i for i in range(1,n+1)]

for i in list(permutations(array,n)):
    print(" ".join(map(str,i)))