from collections import defaultdict
def A_matrix(grid, n):
    M = [[0]*n for _ in range(n)]
    for i in range(n):
        for x in grid[i]:
            M[i][x] = 1
    return M        

def D_matrix(grid, n):
    M = [[0]*n for _ in range(n)]
    for i in range(n):
        M[i][i] = len(grid[i])
    return M

def matrix_deduct(X, Y):
    for i in range(n):
        for j in range(n):
            X[i][j] -= Y[i][j]
    return X

def print_matrix(M):
    for i in range(n):
        print(*M[i])

n, m = map(int, input().split())
grid = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    grid[a].append(b)
    grid[b].append(a)
A = A_matrix(grid, n)
D = D_matrix(grid, n)
L = matrix_deduct(D, A)
print_matrix(L)
