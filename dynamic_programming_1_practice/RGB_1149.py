n = int(input())

rgb = [[0] * 4 for _ in range(n + 1)]
dp = [[0] * 4 for _ in range(n + 1)]

for i in range(n):
    rgb[i][1], rgb[i][2], rgb[i][3] = map(int, input().split())
    min_value = min(rgb[i][1], rgb[i][2], rgb[i][3])
    idx = rgb[i].index(min_value)
    if i == 0:
        dp[i][idx] = min_value
    elif dp[i - 1][idx] == 0:
        dp[i][idx] = min_value
    elif dp[i - 1][idx] != 0:
        if idx == 1:
            min_value = min(rgb[i][idx + 2], rgb[i][idx + 1])
            new_index = rgb[i].index(min_value)
            dp[i][new_index] = min_value
        elif idx == 2:
            min_value = min(rgb[i][idx - 1], rgb[i][idx + 1])
            new_index = rgb[i].index(min_value)
            dp[i][new_index] = min_value
        elif idx == 3:
            min_value = min(rgb[i][idx - 1], rgb[i][idx - 2])
            new_index = rgb[i].index(min_value)
            dp[i][new_index] = min_value

sum = sum(sum(row) for row in dp)
print(sum)
# dp 전꺼랑 다르면서 최소값
