n = int(input())
array = list(map(int,input().split()))
for i in range(n-1,0,-1):
    if array[i]<array[i-1]:
        for j in range(n-1,0,-1):
            if array[j]<array[i-1]:
                array[i-1],array[j]= array[j],array[i-1]
                array=array[:i] +sorted(array[i:],reverse=True)
                for i in array:
                    print(i,end=" ")
                exit()

print(-1)