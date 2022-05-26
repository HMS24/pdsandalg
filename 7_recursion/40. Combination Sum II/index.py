"""https://leetcode.com/problems/combination-sum-ii/
"""

# Approach 1 backtracking
class Solution_1:
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        results = []
        self.backtracking(0, candidates, target, 0, [], results)
        return results

    def backtracking(self, start, candidates, target, curr_sum, curr, results):
        if curr_sum > target:
            return
        if curr_sum == target:
            results.append(curr[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            curr.append(candidates[i])
            self.backtracking(i+1, candidates, target, curr_sum+candidates[i], curr, results)
            curr.pop()


# Approach 2 dfs
class Solution_2:
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates, target, curr_sum, path, results):
        if curr_sum > target:
            return
        if curr_sum == target:
            results.append(path[:])
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            self.dfs(candidates[i+1:], target, curr_sum+candidates[i], path+[candidates[i]], results)
    