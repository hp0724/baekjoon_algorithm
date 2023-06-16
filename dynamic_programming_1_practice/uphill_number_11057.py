n = int(input())
MAX = 1001
MOD = 10007
dp = [[0] * 10 for _ in range(MAX)]

for i in range(10):
    dp[1][i] = 1


for i in range(1, MAX):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i - 1][k]

print(sum(dp[n]) % MOD)
