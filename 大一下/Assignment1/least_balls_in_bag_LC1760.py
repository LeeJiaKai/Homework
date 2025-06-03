from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        k = n + maxOperations
        avg = sum(nums)//k
        if avg == 0:
            return 1
        left, right = avg, max(nums)
        while left < right:
            y = (left+right)//2
            cnt = 0
            for x in nums:
                cnt += (x-1)//y
            if cnt <= maxOperations:
                right = y
            else:
                left = y+1
        return right

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSize([9], 2))  # expect 3
    print(sol.minimumSize([17, 7], 5))  # expect 4