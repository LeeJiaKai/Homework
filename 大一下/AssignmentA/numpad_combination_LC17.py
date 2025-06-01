from collections import deque
digits = input()
num_to_abc = ['', '', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
if not digits:
    print([])
q = deque()
for c in num_to_abc[int(digits[0])]:
    q.append(c)
cnt = len(num_to_abc[int(digits[0])])
for i in range(1,len(digits)):
    for _ in range(cnt):
        parent = q.popleft()
        for c in num_to_abc[int(digits[i])]:
            q.append(parent+c)
    cnt *= len(num_to_abc[int(digits[i])])
q = list(q)
print(q)