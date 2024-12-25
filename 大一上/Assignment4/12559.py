n = int(input())
nums = input().split()
for i in range(n - 1):
    for j in range(i+1, n):
        #print(i,j)
        if nums[i] + nums[j] < nums[j] + nums[i]: #'23'+'9' < '9'+'23'
            nums[i], nums[j] = nums[j], nums[i] #place the string that has the largest 字典序 in front

ans = "".join(nums)
nums.reverse()
print(ans + " " + "".join(nums))
