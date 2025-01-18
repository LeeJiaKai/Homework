h = int(input())
m = int(input())
course = [tuple(map(float, input().split())) for _ in range(m)]
gpa = []
for s, c in course:
    gpa.append(s*c)
gpa.sort(reverse=True)
h = 2*h-0.5*m
ans = 0
for i in gpa:
    temp = 0
    while h>=1 and temp<5:
        temp += i
        h -= 1
    if temp>=5:
        ans += 5
    elif temp>0:
        ans += temp
    else:
        break
print(f"{ans:0,.1f}")

#WA