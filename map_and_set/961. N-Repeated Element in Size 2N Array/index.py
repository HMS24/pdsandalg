"""https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
"""
from typing import List

# Approach 1
"""
1. 計算字母出現頻率，用 dict 儲存
2. 出現頻率大於 1 的數字
"""


class Solution_1:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for key in d:
            if d[key] > 1:
                return key


# Approach 2
"""
1. 排序
2. 比較前後元素相減 == 0 ?
"""


class Solution_2:
    def repeatedNTimes(self, nums: List[int]) -> int:
        self.merge(nums)

        # print(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 0:
                return nums[i]

    def merge(self, a: List[int]) -> None:
        if len(a) == 1:
            return

        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        self.merge(left)
        self.merge(right)

        i = 0
        j = 0
        for index in range(len(a)):
            if i == len(left):
                a[index] = right[j]
                j += 1
            elif j == len(right):
                a[index] = left[i]
                i += 1
            elif left[i] <= right[j]:
                a[index] = left[i]
                i += 1
            else:
                a[index] = right[j]
                j += 1

        return


# Approach 3
"""
1. 用 set 儲存
"""


class Solution_3:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)


# Approach 4
"""
1. 2n 個槽 n+1 個元素 n 個重複
2. case 1: 有兩個重複的元素相臨
3. case 2: 重複與不重複交互排列，重複的元素可能是最後一個也可能是倒數第二個。
4. ex: 10 個槽 6 個值 5 個重複，不重複先插入 1,3,5,7,9，重複則只能 2,4,6,8,10。
"""


class Solution_4:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        for i in range(n-2):
            if nums[i] == nums[-1]:
                return nums[-1]
        return nums[-2]
