n = int(input())
color = [x for x in input()]
take = 0
for i in range(1,n):
    if color[i] == color[i-1]:
        take += 1
print(take)