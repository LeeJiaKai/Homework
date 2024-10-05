n, k = map(int, input().split())
scores = list(map(int, input().split()))
advance = 0
for i in range(n):
    if scores[i]<=0:
        break
    if i >= k:
        if scores[i] < scores[i-1]:
            break
    advance += 1
print(advance)