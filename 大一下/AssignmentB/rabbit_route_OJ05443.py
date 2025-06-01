from collections import defaultdict
import heapq
def find_shortest_route(start, end, route):
    q = [(0, start, [start], [])]
    while q:
        d, current, path, d_path = heapq.heappop(q)
        if current == end:
            return path, d_path
        for next, next_d in route[current]:
            if next in path:
                continue
            new_path = path + [next]
            new_d = d + next_d
            new_d_path = d_path + [next_d]
            heapq.heappush(q, (new_d, next, new_path, new_d_path))

p = int(input())
places = [input() for _ in range(p)]

q = int(input())
route = defaultdict(list)
for _ in range(q):
    a, b, d = input().split()
    d = int(d)
    route[a].append((b, d))
    route[b].append((a, d))

r = int(input())
for _ in range(r):
    start, end = input().split()
    if start == end:
        print(start)
        continue
    path, d_path = find_shortest_route(start, end, route)
    path = path[1:]
    res = f"{start}"
    for i in range(len(path)):
        res += f"->({d_path[i]})->{path[i]}"
    print(res)
