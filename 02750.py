a = int(input())
if a % 2 != 0: #if a = 0, negative, 
    print("0 0")
elif a %4 == 0:
    print(int(a/4), int(a/2))
else:
    print(a//4+1, int(a/2))

