n = int(input())
orange = list(map(int, input().split()))
p_orange = 0
for i in orange:
    p_orange += i
print((p_orange/(n*100))*100)