from sys import stdin
n,m= map(int,stdin.readline().split())
relations = [[] for _ in range(n)]

#방문 표시 
visited = [False] * 2001 

answer = False

for i in range(m) :
    a,b = map(int,input().split())
    # 친구 관계 등록 
    # 양방향 
    relations[a].append(b)
    relations[b].append(a)

def dfs(idx,depth):
    global answer
    visited[idx]=True
    # 친구관계가 4번 이상 
    if depth==4:
        answer=True
        return
    # 친구 관계가 존재 확인 
    for i in relations[idx]:
        if not visited[i]:
            visited[i]=True
            dfs(i,depth+1)
            visited[i]=False

for i in range(n):
    dfs(i,0)
    visited[i]=False
    if answer:
        break

if answer:
    print(1)

else:
    print(0)