from collections import defaultdict, deque
def bfs(x, tree, restricted):
    global path
    global cnt
    global max_node_num
    q = [x]
    while q:
        cur = q.pop()
        for nxt in tree[cur]:
            if nxt not in restricted and nxt not in path:
                q.append(nxt)
                path.append(nxt)
                cnt += 1
    if cnt > max_node_num:
        max_node_num = cnt

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
restricted = list(map(int, input().split()))
used = set()
max_node_num = -1
path = [0]
cnt = 1
bfs(0, tree, restricted)
print(max_node_num)
