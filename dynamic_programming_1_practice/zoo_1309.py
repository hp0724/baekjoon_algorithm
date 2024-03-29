import sys

n = int(sys.stdin.readline())
MOD = 9901
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 3
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] * 2 + (dp[i - 2] * 1)) % MOD

print(dp[n])
