"""https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

# Approach 1 binary search


class Solution1:
    def search(self, nums, target):
        pivot = self.__find_pivot(nums)

        # 若 pivot 為 0，代表沒有翻轉直接 search
        if pivot == 0:
            return self.__binary_search(nums, target)

        # [4, 5, 6, 7, 0, 1, 2],
        # pivot = 4,
        # left = [4, 5, 6, 7],
        # right = [0, 1, 2]
        left = nums[:pivot]
        right = nums[pivot:]

        # target > 樞紐點，找左半部
        if target >= nums[0]:
            return self.__binary_search(left, target)

        # 找右半部時，因為是丟切過的 list，需要 +pivot
        result = self.__binary_search(right, target)
        return result if result < 0 else (result + pivot)

    @staticmethod
    def __find_pivot(nums):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < nums[mid-1]:
                return mid

            # 大於第一個元素值代表處於左邊，縮小左邊
            if nums[mid] >= nums[0]:
                start = mid + 1
            else:
                end = mid - 1
        return 0

    @staticmethod
    def __binary_search(nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
