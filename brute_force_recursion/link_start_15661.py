def is_it():
    global min_diff
    start, link = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += stats[i][j]
            elif not visited[i] and not visited[j]:
                link += stats[i][j]
    min_diff = min(min_diff, abs(start - link))
    return

def resolve(iter):
    if iter == n:
        is_it()
        return
    visited[iter] = True
    resolve(iter + 1)
    visited[iter] = False
    resolve(iter + 1)

n = int(input())
visited=[False for _ in range(n)]
stats = [list(map(int, input().split())) for _ in range(n)]
min_diff=int(1e9)

resolve(0)

print(min_diff)