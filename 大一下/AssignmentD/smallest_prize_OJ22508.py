import sys
from collections import defaultdict, deque

def min_bonus(n, m, matches):
    # 图结构：记录谁打败了谁（反向边）
    graph = defaultdict(list)
    indegree = [0] * n
    
    for a, b in matches:
        graph[b].append(a)  # a > b，所以 b 是 a 的前驱
        indegree[a] += 1

    # 初始化奖金为 100
    bonus = [100] * n

    # 拓扑排序队列
    queue = deque([i for i in range(n) if indegree[i] == 0])

    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            # 如果邻居的奖金不大于当前的，就调整它
            if bonus[neighbor] <= bonus[curr]:
                bonus[neighbor] = bonus[curr] + 1
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sum(bonus)

# 读取输入
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    matches = []
    idx = 2
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx+1])
        matches.append((a, b))
        idx += 2

    result = min_bonus(n, m, matches)
    print(result)