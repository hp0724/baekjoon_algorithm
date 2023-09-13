import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy= [0,0,-1,1]

n= int(input())
# 자리 배열 
arr=[[0]*n for _ in range(n)]
# 한번에 정보 받기 
students = [list(map(int,input().split())) for _ in range(n**2)]

# 학생 수 만큼 for 문 돌려서 자리에 앉기 

for order in range(n**2):
    # 4 2 5 1 7
    student = students[order]

    # 가능한 자리를 다 담아서 정렬후 앉기 
    tmp = [] 
    for i in range(n):
        for j in range(n):
            # 빈자리 라면
            if arr[i][j]==0:
                like=0
                blank=0
                # 상하좌우 확인 
                for k in range(4):
                    nr,nc= i+dx[k], j+dy[k]
                    # 범위 안에 있으면
                    if 0<= nr <n and 0<= nc <n : 
                        # 인접한곳에 좋아하는 학생이 있는경우
                        if arr[nr][nc] in student[1:]:
                            like+=1
                        if arr[nr][nc] ==0:
                            blank+=1
                # 1. 좋아하는 학생이 인접한 칸에 많은 칸
                # 2. 1을 만족하는 칸 여러개있는 경우 비어있는 칸
                # 3.3 2 만족하면 행 작은칸 , 다음 열의 번호 
                tmp.append([like,blank,i,j])
    # like 내림차순 , 빈칸 내림차순 , 행 오름차순 열 오름차순
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    # arr[행][열] = 학생번호 
    arr[tmp[0][2]][tmp[0][3]] = student[0]

result =0 
students.sort()

for i in range(n):
    for j in range(n):
        ans=0 
        for k in range(4):
            nr,nc = i+dx[k],j+dy[k]
            if 0<=nr <n and 0<= nc <n:
                if arr[nr][nc] in students[arr[i][j]-1]:
                    ans +=1
        
        if ans!=0:
            result +=10** (ans-1)

print(result )

    
