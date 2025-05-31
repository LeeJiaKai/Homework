# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cnt = 1
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.popleft()
            if node.left:
                cnt += 1
                stack.append(node.left)
            if node.right:
                cnt += 1
                stack.append(node.right)
        return cnt
