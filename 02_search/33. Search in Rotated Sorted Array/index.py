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


# Approach 2 binary search 判斷左右是否正常排序及目標值是否在範圍內
class Soulution2:
    def search(self, nums, target):
        def search_helper(left, right):
            length = right - left + 1
            if length <= 1:
                return left if nums[left] == target else -1

            mid = (left + right) // 2
            # 判斷左邊是否正常排序，加等號的原因在於處理 mid == left
            # 例如 [3, 1] target: 3
            if nums[mid] >= nums[left]:
                # target 是否在正常排序的左邊
                if target in range(nums[left], nums[mid]+1):
                    return binary_search(left, mid)
                return search_helper(mid+1, right)
            else:
                if target in range(nums[mid], nums[right]+1):
                    return binary_search(mid, right)
                return search_helper(left, mid-1)

        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        left, right = 0, len(nums)-1
        return search_helper(left, right)

# Approach 3 優化 approach 1


class Solution3:
    def search(self, nums, target):
        pivot = self.__find_pivot(nums)
        start, end = 0, len(nums)-1

        while start <= end:
            # 真正的 mid = (rotate mid + pivot) % len(nums)
            rotate_mid = (start + end) // 2
            mid = (rotate_mid + pivot) % len(nums)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = rotate_mid + 1
            else:
                end = rotate_mid - 1

        return -1

    @staticmethod
    def __find_pivot(nums):
        start, end = 0, len(nums) - 1

        # 若大於 nums[end] 代表在第 1 段，移動 start
        # 反之在第 2 段，移動 end
        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return start
