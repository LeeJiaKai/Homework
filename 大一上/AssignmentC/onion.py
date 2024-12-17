n = int(input())
onion = [["x"]*(n+2)] + [["x"]+list(map(int, input().split()))+["x"] for _ in range(n)] + [["x"]*(n+2)]
layer = []

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dr, dc = directions[0]
r, c = 1, 1
k, i = 1, 0
val = 0
for _ in range(n*n):
    val += onion[r][c]
    onion[r][c] = "x"
    if onion[r+dr][c+dc] != "x":
        r, c = r+dr, c+dc
        continue
    else:
        k %= 4
        if k == 0:
            layer.append(val)
            val = 0
        dr, dc = directions[k]
        r, c = r+dr, c+dc
        k += 1
if val != 0:
    layer.append(val)

print(max(layer))
