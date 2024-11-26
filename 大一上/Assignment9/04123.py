directions = [[2,-1], [2,1], [1,2], [-1,2], [-2,1], [-2,-1], [-1,-2], [1,-2]]

ans = 0
def dfs(dep, i, j):
    if dep == n*m:
        global ans
        ans += 1
        return
    
    for dir in directions:
        temp_i, temp_j = i+dir[0], j+dir[1]
        if -1<temp_i<n and -1<temp_j<m:
            if not vis[temp_i][temp_j]:
                vis[temp_i][temp_j] = 1
                dfs(dep+1, temp_i, temp_j)
                vis[temp_i][temp_j] = 0

T = int(input())
for _ in range(T):
    n, m, x, y = map(int, input().split())
    vis = [[0]*10 for _ in range(10)]
    ans = 0
    vis[x][y] = 1
    dfs(1, x, y)
    print(ans)
