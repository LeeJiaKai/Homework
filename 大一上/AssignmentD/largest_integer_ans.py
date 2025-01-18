import math
limit = int(input())
n = int(input())
lst = list(map(str, input().split()))

# 两倍长度是正确的。
max_len = len(max(lst, key = lambda x:len(x)))
lst.sort(key = lambda x: x * math.ceil(2*max_len/len(x)), reverse = True)


# 动态规划部分优化
dp = [0] * (limit + 1)  # dp[i]表示长度为i的最大拼接值
for num in lst:
    for i in range(limit, len(num) - 1, -1):  # 反向更新，避免重复计算
        dp[i] = max(dp[i], dp[i - len(num)] * (10 ** len(num)) + int(num))

print(dp[limit])