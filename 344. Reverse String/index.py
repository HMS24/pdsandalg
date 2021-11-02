"""https://leetcode.com/problems/reverse-string/
"""
from typing import List

# Approach 1
"""
1. 設定兩個指標，起始位置跟最後位置 
2. 2 指標所指元素交換
3. 起始位置 + 1, 最後位置 - 1
4. 重複 123 步驟直到起始指標大於或等於最後指標

def reverse(S):
    start = 0
    end = len(S) - 1
    while start < end:
        swap(S(start), S(end))
        start++
        end--
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


# Approach 2
"""
1. 指標位於倒數第 2 的元素
2. 取得並移除元素且插入串列最後的位置
3. 指標+1
4. 重複 123 直到串列最後元素

def reverse(S):
    for i in [0, n):
        pop(S[-2-i])
        append(S[last])
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        last_index = len(s) - 1
        for i in range(len(s) - 1):
            e = s.pop(-2-i)
            s.append(e)


# Approach 3 遞迴
"""
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.recursion(s, start=0, end=len(s)-1)

    def recursion(self, s, start: int, end: int) -> None:
        if start >= end:
            return

        self.recursion(s, start=start+1, end=end-1)

        s[start], s[end] = s[end], s[start]
