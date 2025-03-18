import heapq
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
k = int(input())

a = list(enumerate(zip(nums1, nums2)))
a = sorted((x, y, i) for i, (x,y) in a)
n = len(a)
ans = [0]*n

q = []
i, s = 0, 0
while i < n:
    start = i
    x = a[start][0]

    while i<n and a[i][0] == x:
        ans[a[i][2]] = s
        i += 1
    
    for j in range(start, i):
        y = a[j][1]
        s += y
        heapq.heappush(q, y)
        if len(q) > k: #niubi
            s -= heapq.heappop(q)
print(ans)