from itertools import combinations
nums = list(map(int, input().split()))
ans = []
for i in range(len(nums)+1):
    for sub in combinations(nums, i):
        ans.append(list(sub))
print(ans)
        