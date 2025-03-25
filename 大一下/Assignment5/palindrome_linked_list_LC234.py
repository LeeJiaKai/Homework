class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = None
        while slow:
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt
        
        left, right = head, pre
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
