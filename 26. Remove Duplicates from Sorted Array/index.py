"""https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List

# Approach 1 Linear Search
"""
1. 逐一取出元素，比較前後元素差
2. 若大於 0，則繼續，等於 0 改為 '-'
3. 再逐一取出元素，比較是否等於 '-'
4. 若是則紀錄位置，並繼續往後找非 '-' 元素與之互換。
"""


class Solution_1:
    def removeDuplicates(self, A: List[int]) -> int:
        n = len(A)
        for i in range(n-1):
            if A[i+1] == A[i]:
                A[i] = '-'

        count = 0
        for i in range(n):
            if A[i] == '-':
                count += 1
            elif count > 0:
                A[i-count], A[i] = A[i], A[i-count]

        return n - count
