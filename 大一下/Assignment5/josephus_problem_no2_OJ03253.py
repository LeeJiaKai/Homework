while True:
    n, p, m = map(int, input().split())
    if (n, p, m) == (0, 0, 0):
        break
    ans = []
    kid = [x for x in range(n)]
    i = p-1
    while kid:
        k = len(kid)
        i += m-1
        i = i%k
        out = kid.pop(i)
        if i == k-1:
            i = 0
        ans.append(str(out+1))
    print(','.join(ans))
