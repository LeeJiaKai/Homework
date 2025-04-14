# A(B(E),C(F,G),D(H(I)))
from collections import defaultdict

def preorder_traversal(node, res):
    res.append(node)
    for child in tree[node]:
        preorder_traversal(child, res)

def postorder_traversal(node, res):
    for child in tree[node]:
        postorder_traversal(child, res)
    res.append(node)

s = input()
if not s:
    print("")
    exit(0)
if len(s) == 1:
    print(s + "\n" + s)
    exit(0)
root = s[0]
tree = defaultdict(list)
stack = []
for x in s:
    stack.append(x)
    if stack[-1] == ')':
        ch = []
        stack.pop()
        while stack[-1] != '(':
            t = stack.pop()
            if t != ',':
                ch.append(t)
        stack.pop()
        ch.reverse()
        tree[stack[-1]].extend(ch)

res1, res2 = [], []
preorder_traversal(root, res1)
postorder_traversal(root, res2)
print(''.join(res1) + '\n' + ''.join(res2))

