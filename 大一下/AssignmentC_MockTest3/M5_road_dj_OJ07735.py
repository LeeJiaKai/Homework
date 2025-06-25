def dfs(x, length, toll, path, ans):
    for d, l, t in city_map[x]:
        if d in path:
            continue
        toll += t
        if toll > k:
            continue
        length += l
        if d == n:
            ans.append(length)
        path.append(d)
        dfs(d, length, toll, path, ans)

k = int(input())
n = int(input())
r = int(input())
city_map = [list() for _ in range(n+1)]
for _ in range(r):
    start, destination, length, toll = map(int, input().split())
    city_map[start].append((destination, length, toll))

ans = []
for des, length, toll in city_map[1]:
    if toll > k:
        continue
    dfs(des, length, toll, [1], ans)
if not ans:
    print(-1)
else:
    ans.sort()
    print(ans[0])
