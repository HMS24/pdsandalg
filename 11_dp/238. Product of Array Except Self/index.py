"""https://leetcode.com/problems/product-of-array-except-self/
"""


class Solution1:
    """
    input
    1 1 2 5
        .
    以 2 為例
    before 就是 2 之前的元素 before[2] = 1*1
    1 1 1 1
    after 就是 2 之後的元素 5 after[2] = 5
    1 1 5 1

    output = before * after
    
    """
    def productExceptSelf(self, nums):
        n = len(nums)
        before = [1] * n
        after = [1] * n

        for i in range(1, n):
            before[i] = before[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            after[i] = after[i+1] * nums[i+1]

        return [before[i] * after[i] for i in range(n)]
