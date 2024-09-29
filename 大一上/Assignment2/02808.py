l, M = map(int, input().split())
L = [1]*(l+1)
for i in range(M):
    a, b = map(int, input().split())
    for j in range(a,b+1):
        L[j] = 0
print(L.count(1))
