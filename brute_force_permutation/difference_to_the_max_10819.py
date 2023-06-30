from itertools import permutations

n= int(input())
array = map(int,input().split())
sum_per=0
max_value=0
for per_array in list(permutations(array,n)):
    for j in range(len(per_array)-1):
         
        sum_per+=abs((list(per_array)[j] -list(per_array)[j+1]))
    max_value=max(max_value,sum_per)
    sum_per=0

print(max_value)