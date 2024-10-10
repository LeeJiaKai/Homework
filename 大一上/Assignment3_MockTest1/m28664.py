n = int(input())
xishu = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
last = ['1','0','X','9','8','7','6','5','4','3','2']
for _ in range(n):
    s = input()
    sum = 0
    for i in range(17):
        sum += (ord(s[i])-48)*xishu[i]
    if s[17] == last[sum%11]:
        print("YES")
    else:
        print("NO")