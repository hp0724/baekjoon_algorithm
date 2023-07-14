import sys 
sys.setrecursionlimit(20000)
input = sys.stdin.readline

def dfs(start,group):
    global error 

    if error:
        return
    visited[start] =group # 정점의 색깔을 둘로 나눌 예정 

    for i in graph[start]:
        if not visited[i]: # 인접하지 않은경우 
            dfs(i,-group)   # -1 값을 주어서 색깔을 다르게 한다 
        elif visited[start] ==visited[i]: # 같은 색깔끼리 인접한 경우 에러 발생 
            error =True 
            return 
        
K = int(input())

for _ in range(K):
    
    V,E = map(int,input().split())
    graph = [[]for _ in range(V+1)]
    visited = [False] *(V+1)
    error =False

    for _ in range(E):
        a,b= map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1,V+1) :
        if not visited[i] :
            dfs(i,1) # group 에 1 값을 주어서 색깔을 나눈다. 
            if error :
                break
    
    if error:
        print('NO')
    else :
        print('YES')
    
     


 
                
    
  