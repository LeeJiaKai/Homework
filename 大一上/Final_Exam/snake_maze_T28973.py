#AC
from collections import deque
directions = [[0,1], [1,0]]

def snake():
    q = deque()
    q.append((0, 0, 0, 0, 1))
    vis = set()
    vis.add((0, 0, 0, 1))
    while q:
        dep, x1, y1, x2, y2 = q.popleft()
        if (x1, y1, x2, y2) == (n-1, n-2, n-1, n-1):
            return dep
        for i in range(2):
            dx, dy = directions[i][0], directions[i][1]
            nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
            if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n:
                if grid[nx1][ny1] == 0 and grid[nx2][ny2] == 0 and (nx1, ny1, nx2, ny2) not in vis:
                    q.append((dep+1, nx1, ny1, nx2, ny2))
                    vis.add((nx1, ny1, nx2, ny2))
                    if x1 == x2 and (i == 1): #水平且下移
                        nx1, ny1, nx2, ny2 = x1, y1, x2+1, y2-1 #顺时针
                        if (nx1, ny1, nx2, ny2) not in vis:
                            q.append((dep+1, nx1, ny1, nx2, ny2))
                            vis.add((nx1, ny1, nx2, ny2))
                    elif y1==y2 and (i == 0): #竖直且右移
                        nx1, ny1, nx2, ny2 = x1, y1, x2-1, y2+1 #逆时针
                        if (nx1, ny1, nx2, ny2) not in vis:
                            q.append((dep+1, nx1, ny1, nx2, ny2))
                            vis.add((nx1, ny1, nx2, ny2))
    return -1

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print(snake())