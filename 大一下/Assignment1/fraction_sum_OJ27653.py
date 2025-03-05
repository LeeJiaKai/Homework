a, b, c, d = map(int, input().split())
#a/b + c/d = ad+bc/bd
top = a*d + c*b
bottom = b*d

def gcd(m, n): #欧几里得算法
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

k = gcd(top, bottom) #最大公约数
print(f"{top//k}/{bottom//k}")