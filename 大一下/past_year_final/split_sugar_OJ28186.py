n, m = map(int, input().split())
a = list(map(int, input().split()))
for idx in range(1, n+1):
    a[idx-1] = (a[idx-1], idx)
i = 0
while len(a)>1:
    a[i] = (a[i][0] - m, a[i][1])
    if a[i][0] <= 0:
        a.pop(i)
        if i >= len(a):
            i = 0
        continue
    i += 1
    if i >= len(a):
        i = 0
print(a[0][1])
