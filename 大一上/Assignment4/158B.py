from math import ceil
n = int(input())
a, b, c, d = map(input().count, ('1', '2', '3', '4'))
taxi = 0
taxi += d
if a <= c:
    taxi += c + ceil(b/2)
else:
    taxi += c + ceil((b*2 + (a-c))/4)
print(taxi)