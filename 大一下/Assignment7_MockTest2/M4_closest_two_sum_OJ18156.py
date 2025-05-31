t = int(input())
nums = list(map(int, input().split()))
nums.sort()
n = len(nums)

if n == 2:
    print(sum(nums))
    exit(0)

left, right = 1, n-1
ans = nums[0] + nums[-1]
min_d = abs(t-ans)
while left < right:
    a = nums[left] + nums[right]
    d = abs(t-a)
    if d < min_d:
        ans = a
        min_d = d
    elif d == min_d:
        if a < ans:
            ans = a
    if a < t:
        left += 1
    else:
        right -= 1
print(ans)
