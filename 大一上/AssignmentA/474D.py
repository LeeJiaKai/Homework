MOD = int(1e9+7)
MAXN = 100001
t, k = map(int, input().split())
dp = [0]*MAXN
flower = [0]*MAXN
dp[0] = flower[0] = 1
for i in range(1, MAXN):
    if i >= k:
        dp[i] = (dp[i-k] + dp[i-1]) % MOD
    else:
        dp[i] = 1
    flower[i] = (flower[i-1] + dp[i]) % MOD

for _ in range(t):
    a, b = map(int, input().split())
    print((flower[b]-flower[a-1])%MOD)