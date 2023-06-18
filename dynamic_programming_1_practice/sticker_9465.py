t_c = int(input())

MAX = 100001


for _ in range(t_c):
    n = int(input())
    costs = [[0] * MAX for _ in range(2)]
    dp = [[0] * MAX for _ in range(2)]
    for i in range(2):
        costs[i] = list(map(int, input().split()))

    dp[0][0] = costs[0][0]
    dp[1][0] = costs[1][0]

    for i in range(1, n):
        dp[0][i] = max(costs[0][i] + dp[1][i - 1], costs[0][i] + dp[1][i - 2])
        dp[1][i] = max(costs[1][i] + dp[0][i - 1], costs[1][i] + dp[0][i - 2])

    print(max(dp[0][n - 1], dp[1][n - 1]))


# 현재값을 선택할경우와 안할경우
# 현재 값을 선택하는 경우 대각선 더하기
# 현재 값을 선택 안하는 경우 [i+1][1]+ [i+2][2] < [i+2][1]
