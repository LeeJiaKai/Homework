import heapq
directions = [[-1,0], [0,1], [1,0], [0,-1]]

def find_start():
    start_x, start_y = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1':
                start_x, start_y = i, j
                return start_x, start_y


def find_border_dfs(x, y):
    grid[x][y] = '2'
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and grid[nx][ny] != '2':
            if grid[nx][ny] == '0':
                if (0,x,y) not in border:
                    border.append((0,x,y))
            elif grid[nx][ny] == '1':
                find_border_dfs(nx,ny)

def find_second_island():
    while border:
        dep, x, y = heapq.heappop(border)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny] != '2':
                if grid[nx][ny] == '1':
                    return dep
                elif grid[nx][ny] == '0':
                    heapq.heappush(border, (dep+1, nx, ny))
                    grid[nx][ny] = '2'

n = int(input())
grid = [list(input()) for _ in range(n)]

start_x, start_y = find_start()
border = []
find_border_dfs(start_x, start_y)
print(find_second_island())