"""https://leetcode.com/problems/subsets/
"""


# Approach 1 iteration
"""
對每個元素`有無`的概念
e.g. nums = [1, 2, 3]

2^0 []
2^1 [] [1]
2^2 [] [1] [2] [1, 2]
2^3 [] [1] [2] [1, 2] [3] [1, 3] [2, 3] [1, 2, 3]
"""

class Solution_1:
    def subsets(self, nums):
        results = [[]]
        for num in nums:
            results += [item+[num] for item in results]
        return results

# Approach 2 recursion
"""
dfs!
將走過的路徑紀錄下來！
持續往下走
用 res 紀答案
"""

class Solution_2:
    def subsets(self, nums):
        results = []
        self.dfs(nums, [], results)
        return results

    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], res)
