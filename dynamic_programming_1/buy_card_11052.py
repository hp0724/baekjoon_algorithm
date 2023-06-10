# 개수를 맞추면서 최대값을 구하라
# (1,1) (2,5) (3,6) (4,7)
# 카드 i 개를 구매하는 최대 비용
# dp[i] = dp[k] +dp[i-k]

n = int(input())
card = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
# 0 1 5 6 7

for i in range(1, n + 1):
    for k in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - k] + card[k])
# dp [1] = (dp[1] dp[0] +card[1])
# dp [2] = dp[2] dp[1] +card[1] dp[2] dp[0] +card[2]
print(dp[i])
