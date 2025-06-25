from collections import defaultdict

n = int(input())
cards = list(input().split())

power = ['A', 'B', 'C', 'D']
q = defaultdict(list)
for x in cards:
    q[int(x[1])].append(x)
    q[str(x[0])].append(x)
for i in range(1, 10):
    l = q[i]
    print(f"Queue{i}:", end='')
    print(*l)
ans = []
for j in power:
    l = q[j]
    l.sort(key=lambda x : x[1])
    ans += l
    print(f"Queue{j}:", end='')
    print(*l)
print(*ans)
