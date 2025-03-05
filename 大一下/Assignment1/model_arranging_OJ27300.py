n = int(input())
li = [tuple(input().split('-')) for _ in range(n)]
arr = []
for name, p in li:
    if arr:
        found = False
        for model in arr:
            if name == model[0]:
                model[1].append(p)
                found = True
        if not found:
            arr.append((name, [p]))
    else:
        arr.append((name, [p]))

arr.sort(key=lambda x: x[0])

def convert_param(p):
    if p[-1] == 'M':
        return float(p[:-1])
    elif p[-1] == 'B':
        return float(p[:-1]) * 1000

for model in arr:
    model[1].sort(key=lambda x: convert_param(x))
    print(f"{model[0]}:", end=' ')
    print(", ".join(model[1]))
