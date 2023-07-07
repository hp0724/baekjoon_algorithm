from itertools import combinations
N,S = map(int,input().split())
data= list(map(int,input().split()))
count=0

for i in range(1,N+1):

    for per_data in combinations(data,i):
        if sum(per_data)==S :
            count+=1

print(count)           
