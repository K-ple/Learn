n, m = map(int,input().split())
d = []
dp = [10001]*(m+1)
for i in range(n):
    a = int(input())
    d.append(a)
    if a <=m:
        dp[a] = 1
dp[0] = 0
for k in d:
    for l in range(k,m+1):
        if dp[l-k] != 10001: 
            dp[l] = min(dp[l],dp[l-k]+1)
if dp[m] ==10001:
    print(-1)
else:
    print(dp[m])