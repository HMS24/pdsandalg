"""https://leetcode.com/problems/maximum-subarray/
"""

# Iteration


class Solution1:
    """
    Time Limit Exceeded

    將所有連續的 subarray 找出來跟 maximun 比較。
    固定 index 往後開始加，
    然後與 maximum 比較。

    時間複雜度: O(n^2)
    空間複雜度: O(1)
    """

    def maxSubArray(self, nums):
        n = len(nums)
        maximun = float("-inf")

        def find(start):
            nonlocal maximun
            curr_sum = 0

            for i in range(start, n):
                curr_sum += nums[i]
                maximun = max(maximun, curr_sum)

        for i in range(n):
            find(i)

        return maximun


# DP


class Solution2:
    """
    子問題:
    就是對某個 index's value 當 subarray 的 ending，我要如何找出連續最大的 subarray 總和？
    
    基本選擇有 2 個:
    1. 持續 extend subarray，目前的 best 為前面一個的最佳 max subarray sum + 目前的 value
    2. 從目前的 value 出發為新的 subarray

    依據基本選擇做比較，填入 DP table，代表為當下 index 為 ending 的 subarray 的最佳解。
    最後再找出整個 DP table 的最佳解

    時間複雜度: O(n)
    空間複雜度: O(n)
    """
    def maxSubArray(self, nums):
        n = len(nums)
        max_table = [None] * n
        max_table[0] = nums[0]

        for i in range(1, n):
            max_table[i] = max(nums[i], max_table[i-1]+nums[i])

        return max(max_table)

# DP improved


class Solution3:
    """
    將 DP table 改為 max_ending_here，因為跟前面一個最佳解做比較，後續再跟 local 的 max_so_far 做比較即可。
    """
    def maxSubArray(self, nums):
        max_so_far = nums[0]
        max_ending_here = nums[0]

        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here+nums[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
