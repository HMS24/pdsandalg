"""https://leetcode.com/problems/find-the-duplicate-number/
"""
from typing import List

# Approach 1 Linear Search
"""
線性搜尋，時間複雜度 O(n^2)，太慘了。
"""


class Solution_1:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return nums[i]


# Approach 2 Use Set to Store
"""
利用額外的 set 資料結構儲存次數，空間換時間。
"""


class Solution_2:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)


# Approach 3 Negative Marking
"""
修改陣列，將陣列元素值乘上 -1 藉以紀錄出現 1 次，若遇到已是負數，該數即重覆值。
"""


class Solution_3:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            nums[abs(num)] *= -1


# Approach 4 Array as HashMap (Iterative)
"""
因 list 有 n+1 空間，數值 in [1, n]，
所以可以用 index 為 0 的空間儲存待搜尋數值，
並以數值為索引，與它交換，若遇到相等，即代表該數重覆。
"""


class Solution_4:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]


# Approach 5 Binary search
"""
1. 計算 x in [1,n] 在 nums 裡小於等於的個數
2. count 若大於 x 則往 left 找 [1, mid]
3. 反之往 right 找 [mid, n]
4. 找到 count 大於 x 且為最小數即是
"""


class Solution_5:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        duplicate = 0

        while start <= end:
            mid = (start + end) // 2

            count = sum(num <= mid for num in nums)
            if count > mid:
                end = mid - 1
                duplicate = mid
            else:
                start = mid + 1

        return duplicate
