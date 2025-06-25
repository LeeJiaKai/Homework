def quadratic_probe_insert(keys, M):
    table = [None] * M
    result = []

    for key in keys:
        pos = key % M
        if table[pos] is None or table[pos] == key:
            table[pos] = key
            result.append(pos)
            continue

        # 否则开始二次探查
        i = 1
        instered = False
        while not instered:
            for sign in [1, -1]:
                new_pos = (pos + sign * (i ** 2)) % M
                if table[new_pos] is None or table[new_pos] == key:
                    table[new_pos] = key
                    result.append(new_pos)
                    instered = True
                    break

            i += 1  # 探查次数增加

    return result


import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
keys = list(map(int, data[2:2 + N]))

positions = quadratic_probe_insert(keys, M)
print(*positions)