#https://leetcode.cn/problems/valid-parentheses/description/

s = input()
bracket_type = ['(', '[', '{', ')', ']', '}']
stack = []
for bracket in s:
    if bracket_type.index(bracket) < 3:
        stack.append(bracket_type.index(bracket))
    else:
        if stack:
            last_bracket = stack.pop()
            if bracket_type.index(bracket) - 3 != last_bracket:
                print("false")
                exit(0)
        else:
            print("false")
            exit(0)
if stack:
    print("false")
else:
    print("true")