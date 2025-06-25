import sys
import threading
import heapq

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B, c = map(int, input().split())
        graph[A].append((B, c))
    INF = 10**30
    dist = [INF] * (N+1)
    dist[1] = 0
    pq = [(0, 1)]  # (当前距离, 节点)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == N:
            break    # 提前退出
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    # 输出从 1 到 N 的最短路距离，即为最大可实现的 x_N - x_1
    print(dist[N])

if __name__ == "__main__":
    threading.Thread(target=main).start()