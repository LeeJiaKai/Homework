n, m = map(int, input().split())
s = [[0]*(m+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(n)] + [[0]*(m+2)]
p = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i][j] == 1:
            p += 4 - s[i+1][j] - s[i-1][j] - s[i][j-1] - s[i][j+1]
print(p)
