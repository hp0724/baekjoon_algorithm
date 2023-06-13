n = int(input())
array = list(map(int, input().split()))
# 처음 길이는 다 1 이니깐
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if array[i] > array[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
