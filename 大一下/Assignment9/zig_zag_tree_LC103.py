# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        stack = deque()
        stack.append(root)
        lvl = 0
        while True:
            lvl += 1
            temp = []
            n = len(stack)
            for _ in range(n):
                node = stack.popleft()
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if lvl%2 == 0:
                temp.reverse()
            ans.append(temp)
            if not stack:
                break
        return ans