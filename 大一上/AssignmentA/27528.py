n = int(input())

if n <= 2:
    print(n)
    exit(0)
dp = [1]*(n+1)
dp[2] = 2
for i in range(3,n+1):
    for j in range(1,i):
        dp[i] += dp[j]
print(dp[n])