"""https://leetcode.com/problems/array-partition-i/
"""
from typing import List

# Approach 1
"""
1. 數列對半切割
2. 持續切割至只剩一個元素
3. 當數列僅剩一個元素時即時回傳
4. 若不止一個元素，則持續切割待子數列排序完成
5. 排序完的 2 個子數列，分別紀錄 2 個數列的起始位置
6. for loop 原數列並逐一比較 2 數列的值
7. 將較小的值放入原數列，將指標指向下一個元素
8. 若數列為空，則將另一數列依序放入原陣列

def merge(A):
    if len(A) == 0:
        return

    mid = A / 2
    left = A[0, mid)
    right = A[mid, len(A))

    merge(left)
    merge(right)

    for i in [0, n]:
        if left is empty:
            A[i] = right[r_poniter]
            r_poniter += 1
        else if right is empty:
            A[i] = left[l_poniter]
            l_poniter += 1
        else if right <= left:
            A[i] = right[r_poniter]
            r_poniter += 1
        else if right > left:
            A[i] = left[l_poniter]
            l_poniter += 1
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        self.mergeSort(nums)

        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]

        return sum

    def mergeSort(self, nums):
        if len(nums) == 1:
            return

        mid = len(nums) // 2
        left = nums[0:mid]
        right = nums[mid:]

        self.mergeSort(left)
        self.mergeSort(right)

        i = 0
        j = 0
        for index, num in enumerate(nums):
            if i == len(left):
                nums[index] = right[j]
                j += 1
            elif j == len(right):
                nums[index] = left[i]
                i += 1
            elif left[i] <= right[j]:
                nums[index] = left[i]
                i += 1
            elif left[i] > right[j]:
                nums[index] = right[j]
                j += 1


# Approach 2
"""
針對排序優化，非原地排列:

def sort(A):
    if len(A) == 1:
        return A
    
    mid = len(A) // 2
    left = sort(A[0, mid)])
    right = sort(A[mid, len(A))])

    return merge(left, right)

def merge(x, y):
    sorted_list = []
    l = 0
    r = 0
    while l < len(x) and r < len(y):
        if x < y:
            sorted_list.append(x[l])
            l += 1
        else:
            sorted_list.append(y[r])
            r += 1
    sorted_list += x
    sorted_list += y

    return sorted_list

"""


class Sort:
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.mergeSortedArray(left, right)

    def mergeSortedArray(self, A, B):
        sortedArray = []
        l = 0
        r = 0
        while l < len(A) and r < len(B):
            if A[l] < B[r]:
                sortedArray.append(A[l])
                l += 1
            else:
                sortedArray.append(B[r])
                r += 1

        sortedArray += A[l:]
        sortedArray += B[r:]

        return sortedArray
