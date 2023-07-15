import sys 
input = sys.stdin.readline
sys.setrecursionlimit(5000)

count=0 
def dfs(x,y):
     global graph 
     
     if x <0 or x>=h or y <0 or y >=w : 
         return False 
     elif graph[x][y] ==1:
        graph[x][y] =0
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x-1,y-1)
        dfs(x-1,y+1)
        dfs(x+1,y-1)
        dfs(x+1,y+1)
        return True
     return False

while True :
    w,h =map (int,input().split())
    if w ==0 and h==0:
        break

    graph=[]
    for _ in range(h):
         graph.append(list(map(int,input().split())))
    
    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j): 
                count+=1
    print(count)
    

    

