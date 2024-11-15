N, B = map(int, input().split())
price = list(map(int, input().split()))
weight = list(map(int, input().split()))

dp=[0]*(B+1)
for i in range(N):
    for j in range(B, weight[i] - 1, -1):
        dp[j] = max(dp[j], dp[j-weight[i]]+price[i])

print(dp[B])