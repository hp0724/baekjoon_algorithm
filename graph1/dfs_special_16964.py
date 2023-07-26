def dfs(graph, start, visited):
    visited[start] = True
    order.append(start)  # 방문 순서 저장
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)

# 입력 받기
n = int(input())  # 노드 개수
graph = [[] for _ in range(n+1)]  # 그래프 초기화
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

expected_order = list(map(int, input().split()))  # 예상 방문 순서

# 그래프의 각 노드에 연결된 리스트 정렬
for i in range(1, n+1):
    graph[i].sort()

# 각 노드를 방문할 때마다 예상 방문 순서에 있는지 확인
visited = [False] * (n+1)
order = []  # 실제 방문 순서 저장
dfs(graph, 1, visited)

# 예상 방문 순서와 실제 방문 순서 비교
if order == expected_order:
    print(1)
else:
    print(0)