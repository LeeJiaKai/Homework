from bisect import *
from collections import deque
power_of_2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_dfs(stack, a):
    node = stack.popleft()
    if a:
        nxt = TreeNode(a.pop())
        stack.append(nxt)
        node.left = nxt
    if a:
        nxt = TreeNode(a.pop())
        stack.append(nxt)
        node.right = nxt
    if stack and a:
        build_tree_dfs(stack, a)

def print_leaf_dfs(node, path):
    global ans
    path.append(node.val)
    if node.right:
        print_leaf_dfs(node.right, path)
        path.pop()
    if node.left:
        print_leaf_dfs(node.left, path)
        path.pop()
    ans.append(path)
    return

n = int(input())
a = list(map(int, input().split()))
a.reverse()
layer_num = bisect(power_of_2, len(a)-1)
root = TreeNode(a.pop())
stack = deque()
stack.append(root)
build_tree_dfs(stack, a)

ans = []
path = []
print_leaf_dfs(root, path)
print(ans)
