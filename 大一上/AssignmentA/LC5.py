s = input()
n = len(s)
if n <=1:
    print(s)
    exit(0)

res_len = 1
begin = 0
dp = [[False]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = True #every alphabet is defaultly a 回文串

for L in range(2, n+1): #test every length
    for i in range(n):
        j = i+L-1 #last index of the current s[i:j] tested
        if j > n-1: #exceeded the default string length
            break
        
        #check function
        if s[i] == s[j]: #the first and last alphabet of the current s[i:j] is same
            if L <= 2: 
                dp[i][j] = True
            else:
                dp[i][j] = dp[i+1][j-1] #跟子串的回文串状态一样
        
        if dp[i][j] and L>res_len: #passed check func and is a new res_len
            res_len = L
            begin = i
print(s[begin: begin+res_len])
