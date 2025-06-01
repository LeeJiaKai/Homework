#memory limit exceed
from collections import defaultdict
import heapq
n = int(input())
word_list = [input() for _ in range(n)]
dict = defaultdict(list)
for i in range(n):
    for j in range(i+1, n):
        if sum(1 for a, b in zip(word_list[i], word_list[j]) if a != b) == 1:
            dict[word_list[i]].append(word_list[j])
            dict[word_list[j]].append(word_list[i])

start, end = input().split()
q = [(0, f"{start}", [start])]
while q:
    step, word, route = heapq.heappop(q)
    for next in dict[word]:
        if next in route:
            continue
        new_route = route + [next]
        if next == end:
            print(*new_route)
            exit(0)
        heapq.heappush(q, (step+1, next, new_route))
print("NO")
