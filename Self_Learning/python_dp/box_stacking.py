#Given n boxes with the Length, Width, Height, 
#find the tallest h for stacking the boxes while Li < Lj, Wi < Wj
n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*n
for i in range(n):
    dp[i] = box[i][2]
for i in range(n):
    for j in range(n):
        if box[i][0] < box[j][0] and box[i][1] < box[j][i]:
            exit()
print()