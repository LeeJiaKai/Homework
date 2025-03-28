from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, n, depth, path, used, ans):
            if depth == n: #finished a permute
                ans.append(path[:])
                return

            for i in range(n):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    dfs(nums, n, depth+1, path, used, ans)

                    #backtracks
                    path.pop()
                    used[i] = False
        
        n = len(nums)
        if n == 0:
            return []
        
        used = [False for _ in range(n)]
        ans = []
        dfs(nums, n, 0, [], used, ans)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 4]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
