import heapq
directions = [[-1,0], [0,1], [1,0], [0,-1]]

def find_card(start_x, start_y, end_x, end_y, r, c, grid):
    q = [(0, start_x, start_y)]
    vis = [[0]*(c+2) for _ in range(r+2)]
    while q:
        dep, x, y = heapq.heappop(q)
        print(dep, x, y)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if (nx,ny) == (end_x, end_y):
                return True, dep
            if 0<=nx<r+2 and 0<=ny<c+2:
                if grid[nx][ny] == ' ' and not vis[nx][ny]:
                    heapq.heappush(q, (dep+1, nx, ny))
                    vis[nx][ny] = 1
    return False, 0

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    grid = [[' ']*(w+2)] + [' ' + input() + ' ' for _ in range(h)] + [[' ']*(w+2)]
    cnt = 1
    board, cnt_board = True, 1
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if (x1, y1, x2, y2) == (0, 0, 0, 0):
            break
        found, ans = find_card(y1, x1, y2, x2, h, w, grid)
        if board:
            print(f"Board #{cnt_board}:")
            board = False
        print(f"Pair {cnt}: ", end="")
        print(f"{ans} segments." if found else "impossible.")
        cnt += 1
    cnt_board += 1

# WA