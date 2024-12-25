n, m = map(int, input().split())
mage = list(map(int, input().split()))
mage.sort()

minus = []
for i in range(n-1):
    minus.append(mage[i+1]-mage[i])
minus.sort()
ans = minus[:-(m-1)]
print(sum(ans))
