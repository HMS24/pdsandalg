"""https://leetcode.com/problems/combination-sum-ii/
"""

# Approach 1 backtracking
"""
時間複雜度: 
    最壞情況下要將 n 個數字都走訪過，需耗費 O (2 ^ n) ，而 sorting 需耗費 O (n logn)，總體時間複雜度為 O (2^n)
空間複雜度:
    需耗費 O (n)，在回朔法過程不斷發生遞迴， function call stack 也會耗費 O (n) ，整體空間複雜度為 O (n) 。
"""

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


# nums = [1, 2, 2, 2, 5]
# s = Solution_1()
# res = s.combinationSum2(nums, 5)
# print(res)
