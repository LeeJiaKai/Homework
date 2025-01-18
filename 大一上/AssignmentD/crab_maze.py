from collections import deque
directions = [[-1,0], [0,1], [1,0], [0,-1]]
def bfs(start_x1, start_y1, start_x2, start_y2, mushroom_x, mushroom_y, n, maze):
    vis = set()
    q = deque([(start_x1, start_y1, start_x2, start_y2)])
    vis.add((start_x1, start_y1, start_x2, start_y2))
    while q:
        x1, y1, x2, y2 = q.popleft()
        if (x1,y1) == (mushroom_x, mushroom_y) or (x2, y2) == (mushroom_x, mushroom_y):
            return True
        for dx, dy in directions:
            nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
            if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n:
                if maze[nx1][ny1] != 1 and maze[nx2][ny2] != 1 and (nx1, ny1, nx2, ny2) not in vis:
                    vis.add((nx1, ny1, nx2, ny2))
                    q.append((nx1, ny1, nx2, ny2))
    return False

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]

mushroom_x, mushroom_y = -1, -1
crab = []
for i in range(n):
    for j in range(n):
        if maze[i][j] == 9:
            mushroom_x, mushroom_y = i, j
        if maze[i][j] == 5 and not crab:
            crab.append((i, j))
            if i+1<n and maze[i+1][j] == 5:
                crab.append((i+1,j))
            else:
                crab.append((i,j+1))
if bfs(crab[0][0],crab[0][1],crab[1][0],crab[1][1], mushroom_x, mushroom_y, n, maze):
    print("yes")
else:
    print("no")

        