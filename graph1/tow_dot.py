from sys import stdin
input = stdin.readline

def cycle ( color,x,y,cnt,start_x,start_y):
    global ans 
    # 사이클 찾으면 종료 
    if ans :
        return 
    # 4가지 방향 
    for i in range(4):
        nx =x+dx[i]
        ny =y+dy[i]

        if nx <0 or nx >=n or ny <0 or ny >=m:
            continue
        # 사이클이 존재 한다면 
        if cnt >=4  and nx == start_x and ny ==start_y:
            ans =True 
            return 
        
        if board[nx][ny] == color and not visited[nx][ny]:
            visited[nx][ny] =1 
            cycle(color,nx,ny,cnt+1,start_x,start_y)
            visited[nx][ny] = 0

def game_start() : 
    for i in range(n):
        for j in range(m):
            # 사이클 시작 위치 
            start_x , start_y = i,j 
            # 방문 표시 
            visited[start_x][start_y]=1 
            cycle(board[i][j],i,j,1,start_x,start_y)
            if ans:
                return 'Yes'
    return 'No'

n,m = map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(map(str,input().rstrip())))
# 방문 표시 
visited = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy= [0,0,-1,1]

ans =False 

print(game_start())