n = int(input())
a = list(map(int, input().split()))
dp = [0]*(max(a)+1)
cnt = [0]*(max(a)+1)
for i in a:
    cnt[i] += 1

dp[0] = 0
dp[1] = cnt[1]
for i in range(2, max(a)+1):
    dp[i] = max(dp[i-1], dp[i-2]+cnt[i]*i)

print(max(dp))