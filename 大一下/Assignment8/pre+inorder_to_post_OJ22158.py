class TreeNode:
    def __init__(self, alp, left=None, right=None):
        self.alp = alp
        self.left = left
        self.right = right

# def dfs(node, ch_left, ch_right, pre, mid):
#     if ch_left:
#         temp_alp = pre.pop()
#         temp = TreeNode(temp_alp)
#         k = ch_left.index(temp_alp)
#         dfs(temp, ch_left[:k].reverse(), ch_left[k+1:].reverse(), pre, mid)
#         node.left = temp
#     else:
#         return

def create_tree(preorder, inorder):
    if not preorder or not inorder:
        return

    root_val = preorder[0]
    root = TreeNode(root_val)
    k = inorder.index(root_val)

    root.left = create_tree(preorder[1:1+k], inorder[:k])
    root.right = create_tree(preorder[1+k:], inorder[k+1:])

    return root

def postorder_traversal(node, res):
    if node is None:
        return
    
    postorder_traversal(node.left, res)
    postorder_traversal(node.right, res)

    res.append(node.alp)

while True:
    try:
        preorder = input().strip()
        inorder = input().strip()
        root = create_tree(preorder, inorder)
        res = []
        postorder_traversal(root, res)
        print(''.join(res))
    except EOFError:
        break