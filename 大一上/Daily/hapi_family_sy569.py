n, q = map(int, input().split())
love = [list(map(int, input().split())) for _ in range(q)]
status = [[0]*n for _ in range(n)]

for x, y in love:
    status[x-1][y-1] = 1
    if status[x-1][y-1] == status[y-1][x-1] == 1:
        print("Yes")
        exit(0)
print("No")