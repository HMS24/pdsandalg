"""https://leetcode.com/problems/plus-one/
"""
from typing import List


# Approach 1
"""
map(str, digits)

''.join(mapped_digits_list)

to num and num += 1

to str and split to List[int]
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([*map(str, digits)]))
        num += 1

        return [int(i) for i in str(num)]


# Approach 2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        length = len(digits)

        while digits[i] == 9:
            digits[i] = 0
            if i == -length:
                digits.insert(0, 1)

                return digits
            i -= 1

        digits[i] += 1

        return digits
