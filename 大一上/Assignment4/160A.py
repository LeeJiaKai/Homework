n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
sumc = 0
take = 0
for i in range(n):
    sumc += a[i]
    take += 1
    if sumc > sum(a[i+1:]):
        break
print(take)