from collections import defaultdict

while True:
    n, m = map(int, input().split())
    ans = []
    if (n, m) == (0, 0):
        break

    players = defaultdict(int)
    for _ in range(n):
        p = list(map(int, input().split()))
        for i in p:
            players[i] += 1

    top = sorted(players.items(), key=lambda x: x[1], reverse=True)

    top2 = top[1][1]
    ans.append(top[1][0])
    if len(top) > 2:
        for i in range(2, len(top)):
            if top[i][1] == top2:
                ans.append(top[i][0])
    ans.sort()
    print(*ans)
