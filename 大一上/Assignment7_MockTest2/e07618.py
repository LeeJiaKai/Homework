n = int(input())
id, age = [], []
for i in range(n):
    a, b = input().split()
    id.append(a)
    age.append(int(b))
agesort = age.copy()
agesort.sort(reverse=True)

usedage = [0]*n
ans = []
young = []
for i in agesort:
    k = age.index(i)
    while usedage[k]: #prevent using same index for same age
        k += age[k+1:].index(i)+1
    if i >= 60:
        ans.append(k)
    else:
        young.append(k)
    usedage[k] = 1
young.sort()

for i in ans:
    print(id[i])
for i in young:
    print(id[i])