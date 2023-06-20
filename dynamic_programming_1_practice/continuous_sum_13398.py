n = int(input())
arrays = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n)]

# dp[i][0]: i번째 수를 제거하지 않은 연속합
dp[0][0] = arrays[0]

# , dp[i][1]: i번째 수를 제거한 연속합
dp[0][1] = float("-inf")
max_sum = arrays[0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + arrays[i], arrays[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arrays[i])
    max_sum = max(max_sum, dp[i][0], dp[i][1])
    print(dp[i])

print(max_sum)
