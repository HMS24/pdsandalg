"""https://leetcode.com/problems/single-number-iii/
"""
from typing import List

# Approach 1
"""
xor 運算
1. 全部數字 xor
2. 從右開始找 xor 為 1 的 bit 位置， 因為 xor 相同為 0 ，重複數字會互相抵消，若為 1 代表有數字不重複。
3. 將這個 bit 位置為 1 的數字再做 xor 運算，即得 1 不重複數字
4. 最後與原先 xor 再做 xor 得到另 1 重複數字。 

"""


class Solution_1:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor1 = 0
        xor2 = 0
        least_set_bit = 0
        for num in nums:
            xor1 ^= num

        for bit in range(32):
            if xor1 & 1 << bit:
                least_set_bit = bit
                break

        for num in nums:
            if num & 1 << least_set_bit:
                xor2 ^= num

        return [xor1 ^ xor2, xor2]


# Approach 2
"""
用 set 來記錄數字
"""


class Solution_2:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)

        return [*s]
