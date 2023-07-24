import sys 
from collections import deque 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 순환선이 존재 확인 
# dfs 
def circulation_station(start,idx,cnt):
    global cycle 
    # 순환선 체크 
    if start == idx and cnt >=2:
        cycle =True 
        return 
    #현재 역 방문 표시 
    visited[idx] =True
    # 다음 방문할 역을 받고 
    for i in info[idx] :
        if not visited[i]:
            circulation_station(start,i,cnt+1)
        elif i == start and cnt>=2:
            circulation_station(start,i,cnt)
# 역과 순환역 사이 거리체크는 bfs 
def distance_station():
    global check 
    q= deque()
    # 순환역에 속하면 0 
    for i in range(N):
        if cycle_station[i]:
            check[i] =0 
            q.append(i)
    while q : 
        now= q.popleft()
        for i in info[now] :
            if check[i]==-1:
                q.append(i)
                # 이동 거리 구하기 
                check[i] = check[now] +1 
    

    for i in check: 
        print(i,end=' ')


N=int(input())
info=[[] for _ in range(N)]
cycle_station = [False] * N 
check =[-1]*N
for _ in range(N):
    a,b= map(int,input().split())
    info[a-1].append(b-1)
    info[b-1].append(a-1)

for i in range(N):
    visited = [False] *N 
    cycle = False
    circulation_station(i,i,0)
    if cycle :
        cycle_station[i]=True 


distance_station()