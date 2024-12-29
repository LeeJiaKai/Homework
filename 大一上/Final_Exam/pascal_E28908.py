#AC
lis = list(input().split(';'))
char = ['a','b','c']
dic = {'a':0,'b':0,'c':0}

for x in lis:
    if x == '':
        continue
    dic[x[0]] = x[-1]

ans = []
for i in char:
    ans.append(dic[i])
print(*ans)