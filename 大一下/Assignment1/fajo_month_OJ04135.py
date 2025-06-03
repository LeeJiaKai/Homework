n, m = map(int, input().split())
exp = [int(input()) for _ in range(n)]
if n == m:
    print(max(exp))
    exit(0)
left, right = max(exp), sum(exp)
while left < right:
    y = (left+right)//2
    cnt, p = 1, 0
    for x in exp:
        if p + x > y:
            cnt += 1
            p = x
        else:
            p += x
    if cnt <= m:
        right = y
    else:
        left = y+1
print(left)
