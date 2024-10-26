n = int(input())
T = list(map(int, input().split()))
student = T.copy()
used_student = [0]*n

T.sort()
ans = []
for i in T:
    k = student.index(i)
    while used_student[k]:
        k += student[k+1:].index(i)+1
    ans.append(k+1)
    used_student[k] = 1
print(*ans)

time = 0
for i in range(n-1):
    time += T[i]*(n-i-1)
time /= n
print(f"{time:.2f}")