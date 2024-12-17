import heapq
directions = [[-1,0], [0,1], [1,0], [0,-1]]

def find_min_time_path(start_x, start_y, end_x, end_y, R, C, K, grid):
    vis = [[[False]*K for _ in range(C)] for _ in range(R)]
    q = [(0, start_x, start_y)]
    while q:
        total_time, x, y = heapq.heappop(q)

        if (x, y) == (end_x, end_y):
            return total_time
        total_time += 1
        tk = total_time % K
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<R and 0<=ny<C:
                if tk == 0 or grid[nx][ny] != '#':
                    if not vis[nx][ny][tk]:
                        heapq.heappush(q, (total_time, nx, ny))
                        vis[nx][ny][tk] = True
    return "Oop!"

def main():
    result = []
    for _ in range(int(input())):
        R, C, K = map(int, input().split())
        grid = [list(input()) for _ in range(R)]
        start_x, start_y, end_x, end_y = -1, -1, -1, -1
        for i in range(R):
            if "S" in grid[i]:
                start_x, start_y = i, grid[i].index("S")
            if "E" in grid[i]:
                end_x, end_y = i, grid[i].index("E")
        ans = find_min_time_path(start_x, start_y, end_x, end_y, R, C, K, grid)
        result.append(ans)
    print("\n".join(map(str, result)))

main()