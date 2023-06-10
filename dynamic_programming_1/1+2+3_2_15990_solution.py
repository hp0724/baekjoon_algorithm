MOD = 1000000009
MAX = 100001
t_c = int(input())
dp = [[0] * 3 for _ in range(MAX)]
# 1 로끝나는 수 1개
dp[1] = [1, 0, 0]
# 2로 끝나는 수 1개
dp[2] = [0, 1, 0]
# (2 1) (1 2) (3) 1 1개 2 1개 3 1개
dp[3] = [1, 1, 1]
# 4 DP[3] + DP[1]
#
# 13 31 121
for i in range(4, MAX):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % MOD
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % MOD
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % MOD

for _ in range(t_c):
    n = int(input())
    print(sum(dp[n]) % MOD)
