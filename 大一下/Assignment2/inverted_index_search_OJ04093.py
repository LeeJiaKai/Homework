from copy import deepcopy as deepcopy

N = int(input())
docs = [list(map(int, input().split()))[1:] for _ in range(N)]

M = int(input())
for i in range(M):
    b = list(map(int, input().split()))
    ans = [] #集合A
    first = True
    while 1 in b: #交集
        k = b.index(1)
        b[k] = 2
        if first:
            for x in docs[k]:
                if x not in ans:
                    ans.append(x)
            first = False
            continue
        temp = []
        #A∩B
        for x in ans: #A中的元素
            if x in docs[k] and x not in temp: #x是否属于B
                temp.append(x) #x属于A∩B
        ans = deepcopy(temp)
    while -1 in b: #差集
        k = b.index(-1)
        b[k] = 2
        temp = []
        #A\B
        for x in ans: #A中的元素
            if x not in docs[k] and x not in temp: #x是否属于B
                temp.append(x) #x属于A\B
        ans = deepcopy(temp)
    if ans:
        ans.sort()
        print(*ans)
    else:
        print("NOT FOUND")
