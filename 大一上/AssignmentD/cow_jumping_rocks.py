def check(x):
    num = 0
    now = 0
    for i in range(1, N+2):
        if rocks[i]-now < x:
            num += 1
        else:
            now = rocks[i]
    if num > M:
        return False
    else:
        return True

L, N, M = map(int, input().split())
rocks = [0] + [int(input()) for _ in range(N)] + [L]

lo, hi = 0, L+1
ans = -1
while lo < hi:
    mid = (lo+hi)//2
    if not check(mid):
        hi = mid
    else:
        ans = mid
        lo = mid+1
print(ans)