from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def check_leaf(node):
            if not node.left and not node.right:
                return True
            return False
        
        def dfs(node, num, res):
            num += str(node.val)
            if node.left: dfs(node.left, num, res)
            if node.right: dfs(node.right, num, res)
            
            if check_leaf(node): res.append(int(num))
            return

        if not root:
            return None
        if not root.left and not root.right:
            return root.val
        res = []
        num = "" + str(root.val)
        if root.left: dfs(root.left, num, res)
        if root.right: dfs(root.right, num, res)
        return sum(res)

if __name__ == '__main__':
    root = [1,2,3]
    sol = Solution()
    res = sol.sumNumbers(root)
