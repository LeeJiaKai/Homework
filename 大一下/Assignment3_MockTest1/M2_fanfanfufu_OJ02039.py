n = int(input())
a = input()
l = len(a)
ans = ''
k = l//n

for i in range(n):
    for j in range(k):
        if j % 2 == 0:
            ans += a[i+j*n]
        else:
            ans += a[(n-i-1)+j*n]
print(ans)