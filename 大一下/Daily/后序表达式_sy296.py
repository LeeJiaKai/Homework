s = list(input().split())
ans = []
fuhao = None
for c in s:
    if c.isdigit():
        ans.append(c)
        if fuhao != None:
            ans.append(fuhao)
            fuhao = None
    else:
        fuhao = c
print(*ans)