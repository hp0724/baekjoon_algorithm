from collections import deque
 
def dfs(graph,v,visited):
    # 방문 처리하고 
    visited[v]=True
    # 출력 하고 
    print(v,end=' ')
    # 현재 노드와 연결된 다른 노드 재귀적 방문 
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    # deque 선언하고 
    queue = deque([start])
    # 방문 처리하고 
    visited[start] =True 
    # queue 가 빌때까지 
    while queue :
        # pop 하면서 
        v= queue.popleft()
        # 출력하고 
        print(v,end=' ')
        # 방문하지 않은곳 찾기 
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


N,M,V = map(int, input().split())
graph = [[] for _ in range(N+1)]
# 양뱡항 
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# 작은숫자부터 하기 위해서 sort()
for i in range(1,N+1):
    graph[i].sort()

visited=[False] *(N+1)
dfs(graph,V,visited)
print()
visited=[False] *(N+1)
bfs(graph,V,visited)

