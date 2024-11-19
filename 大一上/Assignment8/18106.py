n = int(input())
m = [["x"]*(n+2)] + [["x"]+[0]*n+["x"] for _ in range(n)] + [["x"]*(n+2)]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dr, dc = directions[0]
k = 0
r, c = 1, 1
for i in range(1, n*n+1):
    m[r][c] = i
    if m[r+dr][c+dc] != 0:
        k += 1
        dr, dc = directions[k%4]
    r += dr
    c += dc

for r in range(1, n+1):
    for c in range(1, n+1):
        print(m[r][c], end=" ")
    print()
