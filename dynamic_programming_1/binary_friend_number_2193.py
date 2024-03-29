n = int(input())
max = 90
dp = [[0] * 2 for _ in range(n + 1)]
# 뒷자리가 0 또는 1 체크
dp[1][1] = 1

for i in range(2, n + 1):
    for j in range(2):
        if dp[i]:
            if j == 1:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j]

print(sum(dp[n]))
