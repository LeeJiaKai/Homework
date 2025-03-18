nums = list(map(int, input().split()))
s = 0
for x in nums:
    s = s^x
print(s)
