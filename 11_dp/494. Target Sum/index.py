"""https://leetcode.com/problems/target-sum/
"""


class Solution1:
    def findTargetSumWays(self, nums, target):
        """
        brute force
        count ways
        """
        count = 0

        def dfs(i, total):
            nonlocal count
            if i == len(nums):
                if total == target:
                    count += 1
                return

            dfs(i+1, total+nums[i])
            dfs(i+1, total-nums[i])

        dfs(0, 0)

        return count


class Solution2:
    def findTargetSumWays(self, nums, target):
        """
        brute force
        top down
        直接遞迴回傳
        """
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            return (dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i]))

        return dfs(0, 0)


class Solution3:
    def findTargetSumWays(self, nums, target):
        """
        top down
        把算過的 ways cache
        """
        cache = {}

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in cache:
                return cache[(i, total)]

            cache[(i, total)] = dfs(i+1, total+nums[i]) + \
                dfs(i+1, total-nums[i])

            return cache[(i, total)]

        return dfs(0, 0)
