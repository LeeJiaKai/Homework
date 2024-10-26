from math import sqrt

def solve(n, d, islands):
    radar = 1
    ranges = []
    for x, y in islands:
        if y > d:
            return -1
        delta_x = sqrt(d*d - y*y) #毕氏定理
        ranges.append([x-delta_x, x+delta_x])
    
    ranges.sort(key=lambda x:x[1])

    for i in range(n-1):
        if ranges[i][1] >= ranges[i+1][0]:
            ranges[i+1][1] = ranges[i][1]
        else:
            radar += 1
    return radar


case_number = 0
while True:
    n, d = map(int, input().split())
    if [n, d] == [0, 0]:
        break
    islands = []
    for _ in range(n):
        islands.append(tuple(map(int, input().split())))
    
    case_number += 1
    print(f"Case {case_number}: {solve(n, d, islands)}")
    input()