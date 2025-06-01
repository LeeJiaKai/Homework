from collections import deque
directions = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs(r, c, maze, start_x, start_y):
    vis = [[False]*c for _ in range(r)]
    vis[start_x][start_y] = True
    q = deque()
    q.append((start_x, start_y, 0))
    while q:
        x, y, time = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<r and 0<=ny<c and not vis[nx][ny]:
                if maze[nx][ny] == '.':
                    q.append((nx, ny, time+1))
                    vis[nx][ny] = True
                elif maze[nx][ny] == 'E':
                    return True, time+1
    return False, -1

for _ in range(int(input())):
    r, c = map(int, input().split())
    maze = [input() for _ in range(r)]
    for i in range(r):
        if 'S' in maze[i]:
            j = maze[i].index('S')
            break
    found, time = bfs(r, c, maze, i, j)
    if found:
        print(time)
    else:
        print("oop!")
