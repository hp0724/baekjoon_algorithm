import sys 
input= sys.stdin.readline
sys.setrecursionlimit(3000)
N= int(input())
count=0
count_array=[]
graph=[]
result= 0 
for _ in range (N) :
    graph.append(list(map(int,input().rstrip())))
 
def dfs(x,y) :
    global count
    if x <=-1 or x>=N or y<=-1 or y>=N :
        return False
    
    if graph[x][y] ==1:
        count+=1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for i in range(N):
    for j in range(N) :
        if dfs(i,j) ==True:
            count_array.append(count)
            count=0
            result+=1

print(result)
count_array.sort()
for i in count_array:
    print(i)