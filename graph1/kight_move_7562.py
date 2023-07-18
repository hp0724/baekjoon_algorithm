from collections import deque 

#맨 왼쪽 상 부터 시계방향 
dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1, 1, 2,2,1,-1,-2]

def bfs ( start, target,size) :
    queue = deque()
    queue.append(start)
    visited = [[False]*size for _ in range(size)]
    visited[start[0]][start[1]]=True 
    count = 0 

    while queue : 
        count +=1 
        # 모든 큐를 처리하기 위해 반복문 
        for _ in range(len(queue)):
            x,y = queue.popleft()

            # 도착 했을때 반환 
            if x == target[0] and y==target[1] :
                return count -1 
            # 8가지의 경우의 수 
            for i in range (8):
                nx = x+ dx[i] 
                ny = y+ dy[i]
                # 범위에 맞고 방문하지 않은곳이면 queue에 추가후 방문 처리 
                if 0<=nx <size and 0 <=ny <size and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] =True 
    
    return -1 

t_c = int(input())
for _ in range(t_c):
    size= int(input())
    # 값을 튜플로 넣어 주기 
    knight_start = tuple(map(int,input().split()))
    knight_target = tuple(map(int,input().split()))

    #BFS 
    result = bfs(knight_start,knight_target,size)
    print(result)