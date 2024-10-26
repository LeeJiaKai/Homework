case_counter = 0
while True:
    p, e, i, d = map(int, input().split())
    if [p, e, i, d] == [-1, -1, -1, -1]:
        break
    case_counter += 1
    t = d+1
    ENERGY, MENTAL, IQ = p%23, e%28, i%33
    while t%23 != ENERGY or t%28 != MENTAL or t%33 != IQ:
        t += 1
    print(f"Case {case_counter}: the next triple peak occurs in {t-d} days.")