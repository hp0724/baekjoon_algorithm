t_c = int(input())
MAX = 1000001
MOD = 1000000009
dp = [0] * MAX
dp[1] = 1
dp[2] = 2
dp[3] = 4
# 1 = 1   => 1
# 2 = (1,1) (2) => 2
# 3 = (1,1,1) (2,1) (1,2) (3) => 4
# 4 =

for i in range(4, MAX):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % MOD

for _ in range(t_c):
    n = int(input())
    print(dp[n])
