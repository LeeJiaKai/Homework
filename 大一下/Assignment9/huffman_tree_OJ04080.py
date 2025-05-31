import heapq

def min_weighted_path_length(n, weights):
    heapq.heapify(weights)
    total = 0
    while len(weights) > 1:
        a = heapq.heappop(weights)
        b = heapq.heappop(weights)
        combined = a + b
        total += combined
        heapq.heappush(weights, combined)
    return total

n = int(input())
weights = list(map(int, input().split()))
print(min_weighted_path_length(n, weights))
