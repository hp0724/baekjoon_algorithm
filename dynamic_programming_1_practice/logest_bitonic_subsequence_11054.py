n = int(input())
array = list(map(int, input().split()))
dp = [1] * n
turn_on = True
for i in range(n):
    for j in range(i):
        if array[i] > array[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1


idx = dp.index(max(dp))

for i in range(idx, n):
    for j in range(i):
        if array[i] < array[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1


print(dp)
print(max(dp))
