from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(node, list_left, list_right):
            if list_left:
                k = len(list_left)//2
                new_node = TreeNode(list_left[k])
                node.left = new_node
                dfs(new_node, list_left[:k], list_left[k+1:])
            if list_right:
                k = len(list_right)//2
                new_node = TreeNode(list_right[k])
                node.right = new_node
                dfs(new_node, list_right[:k], list_right[k+1:])
            return
        if not nums:
            return None
        n = len(nums)//2
        head = TreeNode(nums[n])
        dfs(head, nums[:n], nums[n+1:])
        return head

if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 7]
    sol = Solution()
    res = sol.sortedArrayToBST(nums)
