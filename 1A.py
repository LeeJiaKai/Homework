import math
m, n, a = map(int, input().split())
print(math.ceil(m/a) * math.ceil(n/a))
#print(-m//a * (-n//a))