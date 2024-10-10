n = int(input())
while True:
    if n == 1:
        print("End")
        break
    elif n%2 != 0:
        print(n, end="")
        print("*3+1=", end="")
        n = n*3+1
        print(n)
    else:
        print(n, end="")
        print("/2=", end="")
        n = n//2
        print(n)