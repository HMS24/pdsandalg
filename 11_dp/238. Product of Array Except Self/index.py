"""https://leetcode.com/problems/product-of-array-except-self/
"""


class Solution1:
    def productExceptSelf(self, nums):
        """
        : type arr: list of int
        : rtype: list of int
        """
        n = len(nums)
        before = [1] * n
        after = [1] * n

        for i in range(1, n):
            before[i] = before[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            after[i] = after[i+1] * nums[i+1]

        return [before[i] * after[i] for i in range(n)]
