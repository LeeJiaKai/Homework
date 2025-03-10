from collections import defaultdict

N = int(input())
words = defaultdict(list)
for i in range(N):
    a = list(input().split())
    for j in range(1,len(a)):
        if i+1 not in words[a[j]]:
            words[a[j]].append(i+1)

M = int(input())
for _ in range(M):
    word = input()
    if not words[word]:
        print("NOT FOUND")
    else:
        print(' '.join(map(str, sorted(words[word]))))
