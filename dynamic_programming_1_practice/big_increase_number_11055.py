n = int(input())
array = list(map(int, input().split()))
# 얕은복사
dp = array[:]
for i in range(1, n):
    for j in range(i):
        if array[i] > array[j] and dp[i] < dp[j] + array[i]:
            dp[i] = dp[j] + array[i]

print(max(dp))
