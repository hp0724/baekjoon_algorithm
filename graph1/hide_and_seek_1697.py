from collections import deque 

def bfs(N,K):
    visited = [False] * 100001
    queue = deque([(N,0)])

    while queue:
        current , time = queue.popleft()

        if current ==K :
            return time 
        # x-1 로 이동 
        if current -1 >=0 and not visited[current-1]:
            visited[current-1] =True 
            queue.append((current-1,time+1))
        
        # x + 1 로 이동 
        if current +1 <= 100000 and not visited[current+1]:
            visited[current+1] =True 
            queue.append((current+1,time+1))
        
        # 2*x 로 순간인동 
        if current*2 <=100000 and not visited [current*2]:
            visited[current*2] =True 
            queue.append((current*2,time+1))

N,K = map(int,input().split())

result = bfs(N,K)
print(result)