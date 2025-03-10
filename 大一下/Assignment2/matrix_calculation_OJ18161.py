def input_list():
    r, c = map(int, input().split())
    return [list(map(int, input().split())) for _ in range(r)], r, c

def valid_matrix(ra, ca, rb, cb, rc, cc):
    if ca != rb:
        return False
    if (ra, cb) != (rc, cc):
        return False
    return True

A, ra, ca = input_list()
B, rb, cb = input_list()
C, rc, cc = input_list()

if not valid_matrix(ra, ca, rb, cb, rc, cc):
    print("Error!")
    exit(0)

#P = A*B
P = [[0]*cb for _ in range(ra)] #ra == rc & cb == cc
for i in range(ra):
    for j in range(cb):
        var = 0
        for k in range(ca): #ca == rb
            var += A[i][k]*B[k][j]
        P[i][j] = var
        P[i][j] += C[i][j]

for r in P:
    print(*r)
