n = int(input())

card_array = [0] + list(map(int, input().split()))
dp = [0] + [1e6 for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - k] + card_array[k])


print(dp[n])

# dp[1] = min(dp[1],dp[0]+card_array[1])
# dp[2] = min(dp[2],dp[1]+card_array[1])
# dp[2] = min(dp[2],dp[0]+card_array[2])
