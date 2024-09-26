t = [list(map(int, input().split())) for _ in range(int(input()))]
for a, b in t:
    if a % b == 0:
        print(0)
    else:
        print((a//b+1)*b-a)