for _ in range(int(input())):
    s = list(input().split())
    stack = []
    for i in range(len(s)):
        x = s[i]
        if x[0].isdigit():
            stack.append(float(x))
        else:
            b = float(stack.pop())
            a = float(stack.pop())
            if x == '+':
                stack.append(a+b)
            elif x == '-':
                stack.append(a-b)
            elif x == '*':
                stack.append(a*b)
            elif x == '/':
                stack.append(a/b)
    print("%.2f" % stack[0])
