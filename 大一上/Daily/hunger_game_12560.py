directions = [[-1,0], [-1,1], [0,1], [1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
n, m = map(int, input().split())
cell = [list(map(int, input().split())) for _ in range(n)]

def bombshakalaka():
    new_cell = [[-1]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            cnt = 0
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and cell[nx][ny] == 1:
                    cnt += 1
            if cell[x][y] == 1 and (cnt<2 or cnt>3):
                new_cell[x][y] = 0
            elif cell[x][y] == 0 and cnt == 3:
                new_cell[x][y] = 1
            elif cell[x][y] == 1 and 2<=cnt<=3:
                new_cell[x][y] = 1
            else:
                new_cell[x][y] = 0
    for line in new_cell:
        print(*line)
bombshakalaka()

