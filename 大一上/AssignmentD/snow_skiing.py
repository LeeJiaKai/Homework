import heapq
directions = [[-1,0], [0,1], [1,0], [0,-1]]

R, C = map(int, input().split())
snow = [list(map(int, input().split())) for _ in range(R)]

q = [(snow[i][j], i, j) for i in range(R) for j in range(C)]
heapq.heapify(q)

dp = [[1]*C for _ in range(R)]
ans = 1

while q:
    h, x, y = heapq.heappop(q)
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0<=nx<R and 0<=ny<C and snow[nx][ny]<h:
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
    ans = max(ans, dp[x][y])
print(ans)