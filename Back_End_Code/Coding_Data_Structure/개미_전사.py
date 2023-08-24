n = int(input())
g = list(map(int,input().split()))

dp = [0]*100
dp[0] = g[0]
dp[1] = max(g[0],g[1])
for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+g[i])

print(dp[n-1])