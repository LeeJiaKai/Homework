p = int(input())
weapon = list(map(int,input().split()))
weapon.sort()
n, k, naruto, enemy = len(weapon), len(weapon), 0, 0
sold = [0]*n

while True:
    for i in range(n):
        if sold[i]:
            continue
        if p-weapon[i] >= 0:
            p -= weapon[i]
            naruto += 1
            sold[i] = 1
        else:
            break
    if sold.count(0) <= 1:
        break
    if naruto > enemy:
        while True:
            if not sold[k-1]:
                enemy += 1
                p += weapon[k-1]
                sold[k-1] = 1
                break
            else:
                k-=1
    else:
        break
    
print(naruto-enemy)