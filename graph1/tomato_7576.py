import sys 
from collections import deque
input =sys.stdin.readline
M,N =map(int,input().split())
graph=[]
count =0 
for _ in range (N):
    graph.append(list(map(int,input().split())))

# 상하 좌우 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 익은 토마토가  있는 좌표를 큐에 저장 
queue = deque() 
for i in range(N) :
     for j in range(M ):
          if graph[i][j] ==1:
               queue.append((i,j))


def bfs():
    while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 범위를 벗어나지 않고 아직 익지 않은 토마토인 경우 
                if 0<=nx<N and 0 <= ny <M  and graph[nx][ny]==0:
                    graph[nx][ny] = graph[x][y]+1
                    queue.append((nx,ny))

bfs()
               
def check_tomatoes() :
    days =-1  # 처음 익은 토마토는 1일이 걸리므로 -1로 초기화
    for row in graph :
        if 0 in row :
            return -1 # 익지 않은 토마토가 있는 경우 
        days = max(days,max(row))
    
    return days -1  

result =check_tomatoes()
print(graph)
print(result)
