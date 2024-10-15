N, D = map(int, input().split())
h = [int(input()) for _ in range(N)]
used = [0] * N

while 0 in used:
    free = []
    for i in range(N):
        if used[i]:
            continue
        if not free:
            minv = h[i]
            maxv = h[i]
        else:
            if h[i] > maxv:
                maxv = h[i]
            if h[i] < minv:
                minv = h[i]

        if maxv - minv > 2*D:
            break

        if (h[i] + D >= maxv and h[i] - D <= minv):
            free.append(h[i])
            used[i] = 1
    free.sort()
    for v in free:
        print(v)