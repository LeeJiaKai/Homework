from collections import deque
directions = [[-1,0], [0,1], [1,0], [0,-1]]

def flood_da_A_country(start_x, start_y, boss, m, n, grid):
    h = grid[start_x][start_y]
    q = deque([(start_x, start_y)])
    vis = [[0]*n for _ in range(m)]
    while q:
        x, y = q.popleft()
        vis[x][y] == 1
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n:
                if grid[nx][ny] < h and not vis[nx][ny]:
                    if (nx, ny) == boss:
                        return True
                    q.append((nx, ny))
    return False

for _ in range(int(input())):
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    boss = tuple(map(int, input().split()))
    flood = False
    for _ in range(int(input())):
        water = tuple(map(int, input().split()))
        x, y = water[0]-1, water[1]-1
        if grid[x][y] <= grid[boss[0]][boss[1]]:
            continue
        if flood_da_A_country(water[0], water[1], boss, m, n, grid):
            print("Yes")
            flood = True
            break
    if not flood:
        print("No")
