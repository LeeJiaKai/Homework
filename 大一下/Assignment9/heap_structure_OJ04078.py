from bisect import *
heap = []
for _ in range(int(input())):
    data = list(map(int, input().split()))
    if data[0] == 1:
        x = data[1]
        if not heap:
            heap.append(x)
        else:
            idx = bisect(heap, x)
            heap = heap[:idx] + [x] + heap[idx:]
    elif data[0] == 2:
        print(heap[0])
        heap = heap[1:]
