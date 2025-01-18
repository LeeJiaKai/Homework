#https://codeforces.com/problemset/problem/2045/M
directions = [[1,0], [-1,0], [0,1], [0,-1]]

def dfs(cnt, x, y, dir, vis):
    dx, dy = directions[dir][0], directions[dir][1]
    nx, ny = x+dx, y+dy
    if 0<=nx<r and 0<=ny<c:
        if grid[nx][ny] == '.':
            return dfs(cnt, nx, ny, dir, vis)
        elif grid[nx][ny] == '/':
            dir = change_dir(1, dir)
            if (nx, ny) not in vis:
                vis.add((nx, ny))
                cnt += 1
            return dfs(cnt, nx, ny, dir, vis)
        else:
            dir = change_dir(2, dir)
            if (nx, ny) not in vis:
                vis.add((nx, ny))
                cnt += 1
            return dfs(cnt, nx, ny, dir, vis)
    elif cnt != mirror_amount:
        return "", False
    else:
        end = ''
        if nx == -1:
            ny += 1
            end += 'N' + str(ny)
        elif nx == r:
            ny += 1
            end += 'S' + str(ny)
        elif ny == -1:
            nx += 1
            end += 'W' + str(nx)
        else:
            nx += 1
            end += 'E' + str(nx)
        return end, True

def change_dir(mirror, dir):
    if mirror == 1 and dir == 0:
        dir = 3
    elif mirror == 1 and dir == 1:
        dir = 2
    elif mirror == 1 and dir == 2:
        dir = 0
    elif mirror == 1 and dir == 3:
        dir = 1
    elif mirror == 0 and dir == 0:
        dir = 2
    elif mirror == 0 and dir == 1:
        dir = 3
    elif mirror == 0 and dir == 2:
        dir = 1
    elif mirror == 0 and dir == 3:
        dir = 0
    return dir

def run(start_x, start_y, dir, start):
    vis = set()
    end, found = dfs(0, start_x, start_y, dir, vis)
    if found:
        ans.append(start)
        if end not in ans:
            ans.append(end)

r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
mirror_amount = 0
for row in grid:
    mirror_amount += row.count('/')
    mirror_amount += row.count(chr(92))
locations = [[] for _ in range(4)]
for i in range(c):
    locations[0].append('N'+str(i+1))
    locations[2].append('S'+str(i+1))
for i in range(r):
    locations[1].append('W'+str(i+1))
    locations[3].append('E'+str(i+1))
ans = []

for k in range(c):
    if locations[0][k] not in ans:     
        run(-1, k, 0, locations[0][k])
for k in range(r):
    if locations[1][k] not in ans:
        run(k, -1, 2, locations[1][k])
for k in range(c):
    if locations[2][k] not in ans:
        run(r+1, k, 1, locations[2][k])
for k in range(r):
    if locations[3][k] not in ans:   
        run(k, c+1, 3, locations[3][k])

if ans:
    print(len(ans))
    print(*ans)
else:
    print(0)
