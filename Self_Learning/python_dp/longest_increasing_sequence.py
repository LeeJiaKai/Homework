#Longest Increasing Sequences (LIS)
#find the longest increasing streak of a[i1]<a[i2]<...<a[ik] following the index i1<i2<...<ik
a = list(map(int, input().split()))
dp = [1]*len(a)
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] < a[j]:
            dp[j] = max(dp[j], dp[i]+1)
print(max(dp))
