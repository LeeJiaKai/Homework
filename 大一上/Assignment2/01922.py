import math
while True:
    n = int(input())
    min_time = float("inf")
    if n == 0:
        break
    for i in range(n):
        v, t = map(int,input().split())
        if t >= 0:
            i_time = math.ceil((4500/v)*3.6 + t)
            min_time = min(min_time, i_time)
    print(min_time)