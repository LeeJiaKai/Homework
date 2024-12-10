a = list(map(int, input().split(',')))
n = len(a)
dp1, dp2 = [0]*n, [0]*n
dp1[0] = dp2[0] = a[0]
for i in range(1, n):
    dp1[i] = max(dp1[i-1]+a[i], a[i])
    dp2[i] = max(dp1[i-1], dp2[i-1]+a[i], a[i])
print(max(dp2))
