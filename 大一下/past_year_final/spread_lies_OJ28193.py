from collections import defaultdict
n, m = map(int, input().split())
coins = list(map(int, input().split()))

# 并查集结构
parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        parent[py] = px

# 构建并查集
for _ in range(m):
    x, y = map(int, input().split())
    union(x-1, y-1)

# 将每个连通块分组
groups = defaultdict(list)
for i in range(n):
    root = find(i)
    groups[root].append(i)

# 计算总花费
total_cost = 0
for group in groups.values():
    min_coin = min(coins[i] for i in group)
    total_cost += min_coin

print(total_cost)
