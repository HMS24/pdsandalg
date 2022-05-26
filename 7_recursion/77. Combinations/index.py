"""https://leetcode.com/problems/combinations/
"""

# Approach 1 backtracking
class Solution_1:
    def combine(self, n, k):
        results = []
        self.backtracking(1, n, k, [], results)
        return results

    def backtracking(self, first, n, k, curr, results):
        if len(curr) == k:
            results.append(curr[:])
            return
        for i in range(first, n+1):
            curr.append(i)
            self.backtracking(i+1, n, k, curr, results)
            curr.pop()

# Approach 2 組合公式
class Solution_2:
    def combine(self, n, k):
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [[*range(1, n+1)]]
        results1 = self.combine(n-1, k-1)
        results1 = [item+[n] for item in results1]
        results2 = self.combine(n-1, k)
        return results1 + results2
        