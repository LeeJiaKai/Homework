row = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    if 1 in row[i]:
        print (abs(i-2)+abs(row[i].index(1)-2))
        break