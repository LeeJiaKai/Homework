problems = int(input())
okay = 0

for i in range(problems):
    a, b, c = [int(x) for x in input().split()]
    if a + b + c > 1:
        okay += 1
print(okay)
    