d = int(input())
n = int(input())
m = [[0]*1025 for _ in range(1025)]
for _ in range(n):
    x, y, k = map(int, input().split())
    for i in range(max(0, x-d), min(x+d+1, 1025)):
        for j in range(max(0, y-d), min(y+d+1, 1025)):
            m[i][j] += k
max_trash = max(max(k) for k in m)
max_point = sum(k.count(max_trash) for k in m)
print(max_point, max_trash)
