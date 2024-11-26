direction = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

area = 0
def dfs(i, j):
    global area #use the global keyword to get the 'area' variable outside this function
    if m[i][j] == '.':
        return
    m[i][j] = '.' #turn the 'W' into '.' to avoid recalculations
    area += 1
    for k in range(8): #continue to call dfs() on the connected blocks around the 'W'
        dx, dy = direction[k]
        dfs(i+dx, j+dy)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    m = [['.' for _ in range(M+2)] for _ in range(N+2)]

    for i in range(1,N+1):
        m[i][1:-1] = input()
    
    max_area = 0
    for i in range(1, N+1): 
        for j in range(1, M+1):
            if m[i][j] == 'W':
                area = 0
                dfs(i, j)
                max_area = max(max_area, area) #holds the max of last max_area and new area
    print(max_area)
