n, k = map(int, input().split())
a = [x+1 for x in range(n)]

ans = []
i = 0
while len(a)>1:
    i += k-1
    i %= len(a)
    ans.append(a.pop(i))
print(*ans)
