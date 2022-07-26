"""https://leetcode.com/problems/subsets/
"""


# Approach 1 iteration

class Solution1:
    def subsets(self, nums):
        results  = [[]]
        for num in nums:
            results += [item+[num] for item in results]
        return results


# Approach 2 backtracking

class Solution2:
    def subsets(self, nums):
        results = []

        def backtrack(start, curr):
            results.append(curr[:])

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        backtrack(0, [])
        return results
