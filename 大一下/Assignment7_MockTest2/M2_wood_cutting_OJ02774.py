n, k = map(int, input().split())
wood = list(int(input()) for _ in range(n))
avg = sum(wood)//k
if avg == 0:
    print(0)
    exit(0)
left, right = 1, avg
while left+1 < right:
    y = (left+right)//2
    cnt = 0
    for x in wood:
        cnt += x//y
    if cnt >= k:
        left = y
    else:
        right = y
print(left)