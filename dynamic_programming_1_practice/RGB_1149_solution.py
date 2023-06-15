n = int(input())
costs = []

# 집의 비용 정보 입력받기
for _ in range(n):
    costs.append(list(map(int, input().split())))

# dp 테이블 초기화
dp = [[0] * 3 for _ in range(n)]
dp[0] = costs[0]  # 첫 번째 집의 비용은 그대로 초기화

# 동적 계획법을 사용하여 최소 비용 계산
for i in range(1, n):
    dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])  # 현재 집을 빨강으로 칠할 경우
    dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])  # 현재 집을 초록으로 칠할 경우
    dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])  # 현재 집을 파랑으로 칠할 경우

# 최종적으로 마지막 집까지 칠하는데 드는 최소 비용
answer = min(dp[n - 1])

print(answer)
