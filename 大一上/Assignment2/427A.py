int(input())
events = list(map(int, input().split()))
police = 0
untreated = 0
for i in events:
    if i >= 0:
        if i > 10:
            i=10
        police += i
    else:
        if police == 0:
            untreated += 1
        else:
            police -= 1
print(untreated)