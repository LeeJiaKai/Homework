import heapq

n = int(input())
a = list(map(int, input().split()))

h = 0
consumed = []
for potion in a:
    h += potion #just drink first
    heapq.heappush(consumed, potion) #heappush into the list with order
    if h < 0: #if the potion drank just now makes health go negative
        h -= consumed[0] #throw the lowest potion drank before out
        heapq.heappop(consumed) #heappop -> throw the lowest
print(len(consumed))
