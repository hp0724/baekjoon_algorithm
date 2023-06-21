INF = 1e6
n = int(input())
rgb = []
ans = INF
# rgb 값 저장

for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    # 색깔을 고장하기 위해서 나머지는 INF 로 두기
    dp[0][i] = rgb[0][i]
    for j in range(1, n):
        dp[j][0] = rgb[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = rgb[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = rgb[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    # 첫번째 집 칠한 색깔과 마지막 집 칠한 색깔이 다른경우
    for j in range(3):
        if i != j:
            # -1 을 사용해서 리스트 마지막값
            ans = min(ans, dp[-1][j])
print(ans)
