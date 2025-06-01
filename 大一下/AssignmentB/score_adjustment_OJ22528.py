from bisect import *
def f(x, b):
    x = (b/10**9)*x + 1.1**((b/10**9)*x)
    return x

def check(score, n):
    idx = bisect(score,85)
    p = (n-idx)/n
    return p >= 6/10

def find_b(score, n):
    left, right = 1, 10**9-1
    while left < right:
        y = (left+right)//2
        new_score = []
        for x in score:
            new_score.append(f(x,y))
        
        if check(new_score, n):
            right = y
        else:
            left = y+1
    return right

score = list(map(float, input().split()))
score.sort()
n = len(score)
res = find_b(score, n)
print(res)
