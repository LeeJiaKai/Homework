a, b = map(int, input().split())
sx = []
for i in range(a,b+1):
    x = i//100
    y = i//10 - x*10
    z = i%10
    if x**3 + y**3 + z**3 == i:
        sx.append(i)
if not sx:
    print("NO")
else:
    print(*sx)