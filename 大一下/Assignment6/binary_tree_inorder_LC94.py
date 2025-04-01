from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(stack, ans):
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                dfs(stack, ans)
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
                dfs(stack, ans)

        if not root:
            return []
        stack = []
        ans = []
        stack.append(root)
        dfs(stack, ans)
        return ans
    
# if __name__ == '__main__':
#     root = [1,None,2,3]
#     solution = Solution()
#     res = solution.inorderTraversal(root)
#     print(res)