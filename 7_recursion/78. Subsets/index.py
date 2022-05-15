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
時間複雜度: n2^n
空間複雜度: n2^n
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
用 res 記答案
時間複雜度: 2^k
空間複雜度: n
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

# Approach 3 backtracking 回溯法
"""
將球丟進球池
符合數量紀錄
然後拿出一顆球
再丟球進去
類似窮舉
時間複雜度: k2^k
空間複雜度: n+1
"""

class Solution_3:
    def subsets(self, nums):
        res = []
        for k in range(len(nums)+1):
            self.backtrack(nums, k, [], res)
        return res

    def backtrack(self, nums, k, curr, results):
        if len(curr) == k:
            results.append(curr[:])
            return

        for i in range(len(nums)):
            curr.append(nums[i])
            self.backtrack(nums[i+1:], k, curr, results)
            curr.pop()


nums = [1, 3, 9]
s = Solution_2()
res = s.subsets(nums)
print(res)
print(count_)