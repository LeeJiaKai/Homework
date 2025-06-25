n = int(input())
a = []
ans = 0
i = 0
for _ in range(2*n):
    data = list(input().split())
    if data[0] == "add":
        a.append(int(data[1]))
    elif data[0] == "remove" and a:
        i += 1
        if a[-1] != i:
            a.sort(reverse=True)
            a.pop()
            ans += 1
            continue
        a.pop()
print(ans)
