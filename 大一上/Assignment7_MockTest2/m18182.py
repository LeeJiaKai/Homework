nCases = int(input())
for _ in range(nCases):
    n, m, b = map(int, input().split())
    skill = {}
    for i in range(n):
        t, x = map(int, input().split())
        if t not in skill.keys():
            skill[t] = [x]
        else:
            skill[t].append(x)

    for t in sorted(skill.keys()):
        skill[t].sort(reverse=True)
        b -= sum(skill[t][:m])
        if b <= 0:
            print(t)
            break
    if b > 0:
        print("alive")
        