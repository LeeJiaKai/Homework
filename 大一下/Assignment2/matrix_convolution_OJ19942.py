m, n, p, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
convo = [list(map(int, input().split())) for _ in range(p)]
ans = [[0]*(n+1-q) for _ in range(m+1-p)]

def cal_convolution():
    val = 0
    for i1 in range(m+1-p):
        for j1 in range(n+1-q):
            for i2 in range(i1,i1+p):
                for j2 in range(j1, j1+q):
                    val += matrix[i2][j2]*convo[i2-i1][j2-j1]
            ans[i1][j1] = val
            val = 0
        
cal_convolution()
for i in ans:
    print(*i)
