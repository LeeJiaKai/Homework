import heapq
directions = [[-1,0], [0,1], [1,0], [0,-1]]

def find_min_energy_path(start_x, start_y, end_x, end_y, m, n, grid):
    if grid[start_x][start_y] == '#' or grid[end_x][end_y] == '#':
        return "NO"
    
    dist = {(start_x, start_y): 0}
    q = [(0, start_x, start_y)]
    while q:
        energy, x, y = heapq.heappop(q)
        if (x, y) == (end_x, end_y):
            return energy
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx <m and 0 <= ny < n and grid[nx][ny] != '#':
                total_energy = energy + abs(int(grid[nx][ny]) - int(grid[x][y]))
                if (nx, ny) not in dist or total_energy < dist[(nx, ny)]:
                    dist[(nx, ny)] = total_energy
                    heapq.heappush(q, (total_energy, nx, ny))
    return "NO"

def main():
    m, n, p = map(int, input().split())
    grid = [list(input().split()) for _ in range(m)]
    result = []
    for _ in range(p):
        start_x, start_y, end_x, end_y = map(int, input().split())
        ans = find_min_energy_path(start_x, start_y, end_x, end_y, m, n, grid)
        result.append(ans)
    print("\n".join(map(str, result)))

main()