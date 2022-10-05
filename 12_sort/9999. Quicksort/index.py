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

    [time complexity](./assets/mergesort.jpg)

    非穩定排序，原先相等元素的順序可能會被打亂。

    另外 quick sort 最差情況(順序或逆序)有可能為 O(n^2)
    為何會有 quick sort 優於 merge sort 的說法？

    首先再亂序的情況下，其實要出現剛好跑出 O(n^2) 的可能性不高
    平均時間仍然為 O(nlogn)
    其次是空間複雜度，利用 in-place 方式，也省去了要合併的操作
    partition 的時候交換 pivot 跟 i 就做完合併了
    因此空間複雜度僅看遞迴呼叫的次數。
    最佳 O(logn) 最差 O(n)

    結論
    quick sort 有較佳的額外空間可以快取
    且避免最差情況也很容易(透過 random select pivot)
    另外還是要看 dataset 的 size(https://stackoverflow.com/questions/70402/why-is-quicksort-better-than-mergesort)
    以及 swap(quick) or copy(merge) 的效率


    如何優化
    - randomly pivot
    - balance pivot: 取前中後三個元素的中間值
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
        # 找到 pivot 的位置
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
