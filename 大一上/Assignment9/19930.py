from collections import deque

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

N, M = map(int, input().split())
m = [[2 for _ in range(M+2)] for _ in range(N+2)] #保护圈
for i in range(1,N+1):
    m[i][1:M] = map(int, input().split())
vis = [[0 for _ in range(M+2)] for _ in range(N+2)] #记录visited

q = deque()
q.appendleft((1, 1, 0)) #(row, col, distance from start)

if m[1][1] == 2:
    print("NO")
    exit(0)

while len(q) != 0: #当全部路径都不是死路
    coord = q.pop() #提取q中最后一位的 坐标 及 目前的最短距离
    vis[coord[0]][coord[1]] = 1

    if m[coord[0]][coord[1]] == 1:
        print(coord[2])
        exit(0)
    for dir in directions:
        temp_i , temp_j = coord[0]+dir[0], coord[1]+dir[1]
        if m[temp_i][temp_j] == 2 or vis[temp_i][temp_j]: #遇到 墙壁 or visited
            continue
        q.appendleft((temp_i, temp_j, coord[2]+1)) #往q的前面(left)加
print("NO")