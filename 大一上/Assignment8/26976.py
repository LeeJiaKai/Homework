n = int(input())
l = list(map(int, input().split()))

count = 1
direction = 0
for i in range(n-1):
    if l[i] == l[i+1]:
        continue
    elif l[i+1]-l[i] > 0:
        if direction == 1:
            continue
        direction = 1
        count += 1
    else:
        if direction == -1:
            continue
        direction = -1
        count += 1
print(count)