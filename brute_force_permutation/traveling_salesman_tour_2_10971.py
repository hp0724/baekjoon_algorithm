import sys 
# 최솟값 갱신을 위한 INF 
INF = sys.maxsize


def dfs(graph,visited,start,current,cost,count) :
    global min_cost

    # 모든 도시를 방문한 경우 
    if count ==n :
        # 시작 도시로 돌아가는 경우 경로가 있을때만 업데이트 
        if graph[current][start]!=0:
            min_cost = min(min_cost,cost+graph[current][start])
        return 
    visited[current] =True

    # 모든 도시에 대해 탐색 
    for i in range(n):
        # 방문했거나  갈수 없는 동시인 경우 pass 
        if visited[i] or graph[current][i] ==0:
            continue 
        
        dfs(graph,visited,start,i,cost+graph[current][i],count+1)
    # 방문한 도시 표시 제거
    # 백트래킹을 위한 False 
    visited[current] = False

n= int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

min_cost = INF 

for start in range(n):
    visited = [False]*n
    dfs(graph,visited,start,start,0,1)

print(min_cost)