n, m1, m2 = map(int, input().split())
X = [[0]*n for _ in range(n)]
Y = [[0]*n for _ in range(n)]
for _ in range(m1):
    r, c, k = map(int, input().split())
    X[r][c] = k
for _ in range(m2):
    r, c, k = map(int, input().split())
    Y[r][c] = k

Z = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        val = 0
        for k in range(n):
            val += X[j][k] * Y[k][i]
        Z[j][i] = val

for i in range(n):
    for j in range(n):
        if Z[i][j] != 0:
            print(i, j, Z[i][j])
