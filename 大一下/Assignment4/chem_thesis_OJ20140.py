s = input()
stack = []
for x in s:
    stack.append(x)
    if stack[-1] == ']':
        stack.pop()
        temp = []
        while stack[-1] != '[':
            temp.append(stack.pop())
        stack.pop()
        numstr = '' #考虑多位数 不可单用int
        while temp[-1].isdigit():
            numstr += str(temp.pop())
        num = int(numstr) if numstr else 1
        temp = temp*num
        while temp:
            stack.append(temp.pop())
print(*stack, sep="")
