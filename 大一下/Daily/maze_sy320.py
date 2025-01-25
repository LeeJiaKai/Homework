from collections import deque
directions = [[-1,0], [0,1], [1,0], [0,-1]]

def check():
    if maze[0][0] == 1 or maze[n-1][m-1] == 1:
        return False
    return True

def find_shortest_path():
    q = deque([(0, 0, 0)])
    vis = [[False]*m for _ in range(n)]
    vis[0][0] = True
    while q:
        x, y, dep = q.popleft()
        if (x, y) == (n-1, m-1):
            return dep
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m:
                if maze[nx][ny] == 0 and not vis[nx][ny]:
                    q.append((nx, ny, dep+1))
                    vis[nx][ny] = True       
    return -1

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
if check():
    print(find_shortest_path())
else:
    print(-1)

