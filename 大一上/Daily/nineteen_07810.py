n = int(input())
p = [input() for _ in range(n)]

def nineteen(i):
    if int(i) % 19 == 0:
        return True
    for j in range(len(i)-1):
        if i[j]+i[j+1] == '19':
            return True
    return False

for i in p:
    print("Yes" if nineteen(i) else "No")
