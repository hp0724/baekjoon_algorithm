from sys import stdin
import sys

sys.setrecursionlimit(3000)

 
def dfs(graph,start,visited):
    visited[start]=True 
     
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)
             
N,M = map(int, stdin.readline().split())
graph= [[]for _ in range (N+1)]
for _ in range(M):
    a,b=map(int,stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count=0
visited=[False] *(N+1)
for i in range(1,N+1):
    
     if not visited[i] :
         count+=1
         dfs(graph,i,visited)

print(count)

 