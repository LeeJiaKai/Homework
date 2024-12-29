from collections import  deque
n = int(input())
student = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    student[i].append(sum(student[i]))
    student[i].append(i+1)
student.sort(key=lambda x:x[3])

same = []
cnt = 0
while cnt < 5 or same:
    if student[-1][3] > student[-2][3] and not same:
        print(student[-1][4], student[-1][3])
        cnt += 1
        student.pop()
    elif student[-1][3] == student[-2][3]:
        same.append(student[-1])
        cnt += 1
        student.pop()
    elif student[-1][3] > student[-2][3] and same:
        same.append(student[-1])
        student.pop()
        cnt += 1
        same.sort(key=lambda x:x[0])
        if cnt > 5:
            same = same[1:]
        while same:
            out = same.pop()
            print(out[4], out[3])