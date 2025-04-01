from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        def level(q, ans):
            temp = []
            new_q = deque()
            while q:
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            ans.append(temp)
            if new_q:
                level(new_q, ans)
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        level(q, ans)
        return ans
                
