"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


# Approach 1
"""
for enumerate(numbers, 1)
    second_num = target - num
    if second_num in numbers[i:]:
        find second_num index
        return [i, finded_index + i + 1]
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, first in enumerate(numbers, 1):
            second = target - first
            sub_numbers = numbers[i:]
            if second in sub_numbers:
                j = sub_numbers.index(second) + i + 1

                return [i, j]
            continue


# Approach 2
"""
for i in numbers:
    first_num = numbers[i]
    seconde = target first_num
    for j = i + 1 ~ len(nembers):
        if numbers[j] == second:
            return indexes array
        if numbers[j] > second:
            break
        continue
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            first = numbers[i]
            second = target - first
            for j in range(i+1, len(numbers)):
                if numbers[j] == second:
                    return [i+1, j+1]
                if numbers[j] > second:
                    break
                continue


# Approach 3 - two pointers ! 縮範圍
"""
declare start and end indexes
while start < end:
    sum = start num + end num
    if sum == target:
        return [start+1, end+1]
    if sum > target:
        end -= 1
    start += 1
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return[start+1, end+1]

            if sum > target:
                end -= 1
            else:
                start += 1


# Approach 4 - hash 網路 discussions
"""
for enumerate numbers:
    if target-num in dict:
        return [dict[target-num] +1, i+1]
    dict[num] = i
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
