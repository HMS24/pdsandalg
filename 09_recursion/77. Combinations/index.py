"""https://leetcode.com/problems/combinations/
"""

# Approach 1 backtracking


class Solution1:
    def combine(self, n, k):
        results = []

        def backtracking(start, curr):
            if len(curr) == k:
                return results.append(curr[:])
            for i in range(start, n+1):
                curr.append(i)
                backtracking(i+1, curr)
                curr.pop()

        backtracking(1, [])

        return results

# Approach 2 組合公式


class Solution2:
    def combine(self, n, k):
        # e.g. c(4, 1) = [[1], [2], [3], [4]]
        if k == 1:
            return [[i] for i in range(1, n+1)]
         # e.g. c(4, 4) = [[1, 2, 3, 4]]
        if k == n:
            return [[*range(1, n+1)]]

        results1 = self.combine(n-1, k-1)
        # 一定要取第 1 個數字也就是 n
        results1 = [item+[n] for item in results1]

        results2 = self.combine(n-1, k)
        return results1 + results2
