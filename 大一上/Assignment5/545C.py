n = int(input())
x, h = [], []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    h.append(b)
cut = 2
if n == 1:
    print(1)
else:
    for i in range(1, n-1):
        if x[i] - x[i-1] > h[i]:
            cut += 1
        elif x[i+1] - x[i] > h[i]:
            cut += 1
            x[i] += h[i]
    print(cut)