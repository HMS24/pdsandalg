"""https://leetcode.com/problems/single-number/
"""
from typing import List

# Approach 1
"""
XOR: The ^ operator will perform a binary XOR in which a binary 1 is copied if and only if it is the value of exactly one operand. Another way of stating this is that the result is 1 only if the operands are different. Examples include:

# 0^0= 0
# 0^1= 1
# 1^0= 1
# 1^1= 01

XOR 運算有交換律，相同為 0，不同為 1 
"""


class Solution_1:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for num in nums:
            n ^= num

        return n
