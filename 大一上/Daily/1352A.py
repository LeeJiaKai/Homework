t = int(input())
power_of_ten = [10000, 1000, 100, 10, 1]
for _ in range(t):
    n = int(input())
    k = 0
    round = []
    for i in power_of_ten:
        if n >= i:
            k += 1
            round.append(n//i*i)
            n %= i
    print(k)
    print(*round)