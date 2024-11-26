directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(total, i, j):
    global max_val, route
    if i == n-1 and j == m-1:
        if total > max_val:
            max_val = total
            route = temp_route[:]
        return
    
    vis[i][j] = 1
    for dir in directions:
        temp_i, temp_j = i+dir[0], j+dir[1]
        if -1<temp_i<n and -1<temp_j<m:
            if not vis[temp_i][temp_j]:
                temp_route.append((temp_i, temp_j))
                dfs(total+val[temp_i][temp_j], temp_i, temp_j)
                temp_route.pop()
    vis[i][j] = 0

n, m = map(int, input().split())
val = [(list(map(int, input().split()))) for _ in range(n)]

max_val = float('-inf')
vis = [[0]*m for _ in range(n)]
route = []
temp_route = [(0,0)]

dfs(val[0][0], 0, 0)

for x, y in route:
    print(x+1, y+1)
