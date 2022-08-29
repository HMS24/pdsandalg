"""
Quicksort

"""


class Solution:
    """
    e.g. 
        4   5   1   2   3
    i                   pivot
        j

    - 4 < 3 ? no, move on
        4   5   1   2   3
    i                   pivot
            j

    - 5 < 3 ? no, move on
        4   5   1   2   3
    i                   pivot
                j

    - 1 < 3 ? yes, i+1, swap(i, j)
        1   5   4   2   3
        i               pivot
                    j

    - 2 < 3 ? yes, i+1, swap(i, j)
        1   2   4   5   3
            i           pivot
                    j

    - j is done swap(i+1, pivot)
        1   2   3   5   4
                i+1     pivot

    - quicksort(0, 1) quicksort(3, 5)
    ...
    ...
    ...
    """

    def quicksort(self, nums):
        '''
        :type nums: list of int
        :rtype: list of int
        '''
        self.quicksort_helper(nums, 0, len(nums)-1)

        return nums

    def quicksort_helper(self, nums, left, right):
        """recursive helper"""
        # right 在 split 階段會不斷 -1 因此得確保 left < right
        if left < right:
            # partition
            pivot_position = self.partition(nums, left, right)
            # split
            self.quicksort_helper(nums, left, pivot_position-1)
            self.quicksort_helper(nums, pivot_position+1, right)

    def partition(self, nums, left, right):
        """find pivot position"""
        pivot = nums[right]

        # i 記得比 pivot 小的最後一個位置
        # j scan whole list
        # 如果 j 掃到了，就先把 i+1 然後交換 i, j+1
        i = left - 1
        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1

                self.swap(nums, i, j)

        # 最後交換 pivot 的位置
        self.swap(nums, i+1, right)
        return i + 1

    def swap(self, nums, first, second):
        # 如果 i, j 剛好相等無需真正交換
        if first == second:
            return
        nums[first], nums[second] = nums[second], nums[first]
