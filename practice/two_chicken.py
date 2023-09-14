import sys 
input =sys.stdin.readline
n,m = map(int,input().split())
INF =int(1e9)

# 양방향 그래프 

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]= 1
    graph[b][a] = 1

# 자기 자신은 비용0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b :
            graph[a][b]=0

            

# 모든 정점에서 모든 점정으로 가는 최소거리 
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])

# 2개의 건물을 선택하여 모든 집을 방문해서 걸리는 거리를 측정 
min_sum =INF 
result =list()

for i in range(1,n):
    for j in range(2,n+1):
        sum =0 
        for k in range(1,n+1):
            sum += min(graph[k][i],graph[k][j])*2 
        if sum <min_sum:
            min_sum=sum
            result = [i,j,sum]

print(*result)