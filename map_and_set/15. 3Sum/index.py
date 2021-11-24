"""https://leetcode.com/problems/3sum/
"""
from typing import List

# Approach 1
"""
1. 排序
2. 對每個 num in nums，新的 target = target - num
3. 對 num 之後的子 list 以及新的 target 使用 two sum 的方法尋找
4. two sum hashset 不會排除 duplicates，因此用 results = set() 去濾掉重複。
"""


class Solution_1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.mergeSort(nums)

        target = 0
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            if nums[i] > 0 and target - nums[i] < 0:
                return results

            subsets = self.twoSum(nums[i+1:], target-nums[i])

            if subsets:
                for s in subsets:
                    results.append([nums[i], *s])

        return results

    @staticmethod
    def twoSum(nums, target):
        s = set()
        results = set()
        for num in nums:
            if target - num in s:
                results.add((target-num, num))
            s.add(num)

        return results

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        self.mergeSort(left)
        self.mergeSort(right)

        i = 0
        j = 0
        for k in range(len(nums)):
            if i == len(left):
                nums[k] = right[j]
                j += 1
            elif j == len(right):
                nums[k] = left[i]
                i += 1
            elif left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1

        return
