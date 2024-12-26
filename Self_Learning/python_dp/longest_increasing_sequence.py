a = list(map(int, input().split()))
dp = [1]*len(a)
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] < a[j]:
            dp[j] = max(dp[j], dp[i]+1)
print(max(dp))
