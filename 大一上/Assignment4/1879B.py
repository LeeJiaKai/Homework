t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_a = min(a)
    min_b = min(b)

    ans_min_a = sum(min_a + i for i in b)
    ans_min_b = sum(min_b + i for i in a)
    print(min(ans_min_a, ans_min_b))