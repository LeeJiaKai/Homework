from collections import defaultdict, deque

def check_cycle(x, dir):
    q = deque()
    for y in dir[x]:
        q.append(y)
    
    while q:
        nxt = q.popleft()
        if nxt == x:
            return True
        for y in dir[nxt]:
            q.append(y)
    return False

n, m = map(int, input().split())
dir = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    if u in dir[v]:
        print("Yes")
        exit(0)
    dir[u].append(v)

for x in range(n):
    found = check_cycle(x, dir)
    if found:
        print("Yes")
        exit(0)
print("No")
