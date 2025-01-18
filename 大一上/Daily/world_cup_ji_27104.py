n = int(input())
kun = list(map(int, input().split()))
jiwo = [0]*n
for i in range(n):
    for j in range(i-kun[i],i+kun[i]+1):
        if 0<=j<n:
            jiwo[j] += 1
cammed = [0]*n
cnt = 0
while 1 in jiwo:
    i = jiwo.index(1)
    for j in range(i-kun[i],i+kun[i]+1):
        if 0<=j<n:
            cammed[j] = 1
    jiwo[i] = 0
    cnt += 1
if 0 in cammed:
    ptr = 0

    mx = max(jiwo)
    while ptr < n:
        # 假设下一个指针位置为当前指针加上当前观测范围再加一
        nxt = ptr + jiwo[ptr] + 1

        # 遍历一个以当前指针为中心的大窗口，考虑到最大观测范围mx的影响
        for i in range(max(0, ptr - mx), min(n, ptr + mx + 1)):
            if 0 <= i < n and i - jiwo[i] <= ptr and i + jiwo[i] + 1 > nxt:
                nxt = i + jiwo[i] + 1  # 更新最远可达位置

        cnt += 1  # 每次循环代表安装了一个摄像头
        ptr = nxt
