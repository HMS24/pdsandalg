"""https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""
from typing import List

# Approach 1
"""
"""


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)

        slow = 2
        fast = 2

        while fast < len(nums):
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
