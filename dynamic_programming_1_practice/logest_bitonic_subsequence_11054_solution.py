n = int(input())
array = list(map(int, input().split()))
inc_dp = [1] * n
dec_dp = [1] * n
max_length = 0

for i in range(n):
    for j in range(i):
        if array[i] > array[j] and inc_dp[i] < inc_dp[j] + 1:
            inc_dp[i] = inc_dp[j] + 1

# 거꾸로 가면서 뒤에 꺼 확인
for i in range(n - 1, -1, -1):
    # 자기 자신과는 비교 안하기 위해서 i+1
    for j in range(i + 1, n):
        if array[i] > array[j] and dec_dp[i] < dec_dp[j] + 1:
            dec_dp[i] = dec_dp[j] + 1


for i in range(n):
    length = inc_dp[i] + dec_dp[i] - 1
    if length > max_length:
        max_length = length


# print(inc_dp)
# print(dec_dp)
print(max_length)
