k = int(input())
s = input()
new = ""
for c in s:
    if 'a' <= c <= 'z':
        c = chr((ord(c)-ord('a')-k) %26 + ord('a'))
    elif 'A' <= c <= 'z':
        c = chr((ord(c)-ord('A')-k) %26 + ord('A'))
    new += c
print(new)