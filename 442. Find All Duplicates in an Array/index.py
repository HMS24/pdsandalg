"""https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""
from typing import List

# Approach 1 for loop
"""
1. 建立 set 及 arr
2. 取得數列裡的整數，檢測 set 有無該整數，有則插進 arr，無則新增
3. 重複 2 直到跑完數列
4. 回傳 arr

def find_duplicates(nums):
    s = set()
    a = []
    for num in nums:
        if set has num:
            append num in a
        else:
            set add num
    return a
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_set = set()
        duplicated_nums = []
        for num in nums:
            if num in nums_set:
                duplicated_nums.append(num)
            else:
                nums_set.add(num)

        return duplicated_nums


# Approach 2 sort 後 for loop
"""
1. 排序
2. 後減前等於 0

def (nums):
    sort(nums)
    a = []
    for i in [0, n-2]:
        if nums[i+1] - nums[i] == 0:
            append in a
    return a
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicated_nums = []
        for i in range(0, len(nums)-1):
            if nums[i+1] - nums[i] == 0:
                duplicated_nums.append(nums[i])

        return duplicated_nums


# Approach 3 list 當 hash map
"""
1. 因為 1 <= a[i] <= n
2. 利用整數當索引
3. 對該整數索引的值乘上 -1
4. 若為負的則重覆，插入回傳陣列。
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicated_nums = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                duplicated_nums.append(abs(x))
            else:
                nums[abs(x)-1] *= -1

        return duplicated_nums


# Approach 4 negative and n marking and Big(2n) == Big(n) 最符合題目要求
"""
1. list as hash map
2. 整數當索引，若第一次則乘上 -1，第二次則減數列長度
3. 重覆 2 的步驟
4. 逐一 pop 出數列的第一個整數，判斷是否為超出數列長度，超出則將索引 append 數列。
5. return 數列
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            _num = abs(num)
            index = _num-n-1 if _num > n else _num-1

            if nums[index] < 0:
                nums[index] -= n
            else:
                nums[index] *= -1

        for i in range(0, n):
            num = nums.pop(0)
            if abs(num) > n:
                nums.append(i+1)

        return nums
