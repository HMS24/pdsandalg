"""https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
from typing import List

# Approach 1
"""
1. 從第一個元素依序開始找
2. 若下一個元素大於該元素值，則持續線性搜尋，若小於則回傳結果。
3. 若數列長度為 3 直接回傳中位數的 index。
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) == 3:
            return 1
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i+1]:
                return i
            continue


# Approach 2
"""
1. 找數列的中位數
2. 比較前後元素，若遞增，找右邊子數列的中位數
3. 遞減，找左邊子數列的中位數
4. 持續比較前後元素，直到找到結果
5. 若子數列的長度為 3 ，則取中位數回傳結果

def(A):
    start = 0
    end = len(A) - 1
    while end - start >= 3:
        m = (start + end + 1) / 2
        if prev < curr > next:
            return m
        if 遞增:
            start = m
        else:
            end = m

     // 當只剩 3 元素
    return m
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while end - start >= 3:
            m = (start + end + 1) // 2
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            if arr[m-1] < arr[m] < arr[m+1]:
                start = m
            else:
                end = m

        return 1
