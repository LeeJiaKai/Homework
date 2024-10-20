n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
sum = 0
for i in range(m):
    if a[i] >=0:
        break
    sum -= a[i]
print(sum)
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# used = [0]*n
# sum = 0
# min_i = 0
# for _ in range(m):
#     minv = 0
#     for i in range(n):
#         if used[i]:
#             continue
#         if a[i] < minv:
#             minv = a[i]
#             min_i = i
#     if minv == 0:
#         break
#     sum -= minv
#     used[min_i] = 1
# print(sum)