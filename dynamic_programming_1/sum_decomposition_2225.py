N, K = map(int, input().split())
# 20 2
# 2차원 DP 테이블 초기화
MOD = 1000000000
dp = [[0] * (N + 1) for _ in range(K + 1)]
# 0을 만드는 경우의 수는 항상 1
for i in range(K + 1):
    dp[i][0] = 1


for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD
        # dp[1][1] = dp[1][0]+dp[0][1]
print(dp[K][N])
