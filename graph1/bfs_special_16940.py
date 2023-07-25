from collections import deque
N=int(input())
data=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b =map(int,input().split())
    data[a].append(b)
    data[b].append(a)
origin = list(map(int,input().split()))
answer = []
visited=[False]*(N+1)

def bfs(data,visited,start):
    queue = deque([start])
    visited[start]=True
    while queue:
        v= queue.popleft()
         
        answer.append(v)
        for i in data[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

bfs(data,visited,1)


if origin==answer :
    print(1)
else:
    print(0)