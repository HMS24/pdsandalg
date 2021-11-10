"""https://leetcode.com/problems/binary-search/
"""
from typing import List
from math import floor


# Approach 1
"""
min = 0
max = list last index
while min < max:
    get mid and floor int
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        min = mid + 1
    else:
        max = mid - 1
if nums[min] == target:
    return min
return -1
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1
        while min <= max:
            mid = floor((min + max) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                min = mid + 1
            else:
                max = mid - 1
        return -1
