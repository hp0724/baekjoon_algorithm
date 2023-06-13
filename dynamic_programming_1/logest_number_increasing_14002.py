n = int(input())
array = list(map(int, input().split()))

dp = [1] * n  # 각 요소별로 증가하는 부분 수열의 길이를 저장하는 배열
previous = [-1] * n  # 각 요소의 이전 요소 인덱스를 저장하는 배열

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            previous[i] = j

max_length = max(dp)
max_index = dp.index(max_length)

result = []
while max_index != -1:
    result.append(array[max_index])
    max_index = previous[max_index]

result.reverse()

print(max_length)
print(" ".join(map(str, result)))
