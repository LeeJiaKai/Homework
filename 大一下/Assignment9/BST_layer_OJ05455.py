from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def layer(root):
    ans = []
    stack = deque()
    stack.append(root)
    while stack:
        node = stack.popleft()
        ans.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ans


def insert(val, root):
    node = Node(val)
    temp = root
    while True:
        if val < temp.val:
            if not temp.left:
                temp.left = node
                break
            temp = temp.left
        else:
            if not temp.right:
                temp.right = node
                break
            temp = temp.right

def main():
    data = list(map(int, input().split()))
    used = set()
    root = Node(data[0])
    data = data[1:]
    for x in data:
        if x not in used:
            insert(x, root)
        used.add(x)
    res = layer(root)
    print(*res, end="")


if __name__ == "__main__":
    main()
