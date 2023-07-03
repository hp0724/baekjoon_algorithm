n= int (input())
time=[]
cost=[]
dp= [0 for _ in range(n+1)]


for _ in range(n):
    T,P = map(int,input().split())
    time.append(T)
    cost.append(P)

#n=10 
for i in range(n-1,-1,-1):
    # 상담일이 마지막 상담일보다 클경우 
    if time[i] +i  >n:
        dp[i] = dp[i+1]
    else: 
        dp[i] =max(dp[i+1],dp[time[i]+i]+cost[i])
    print(dp[i])
print(dp[0])