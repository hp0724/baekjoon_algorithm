n = int(input())
MAX = 31
dp = [0] * MAX
dp[2] = 3
dp[4] = 11
for i in range(6, MAX, 2):
    dp[i] = dp[i - 2] * 4 - dp[i - 4]


print(dp[n])
