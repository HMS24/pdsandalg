"""
The 0-1 Knapsack Problem

https://web.ntnu.edu.tw/~algo/KnapsackProblem.html
"""


class Solution:
    def knapsack(self, values, weights, maxWeightConstraint):
        '''
        :type values: list of int
        :type weights: list of int
        :type maxWeightConstraint: int
        :rtype: int
        '''
        m = 0
        walked = set()

        def dfs(v, w, walked):
            nonlocal m
            if w > maxWeightConstraint:
                return
            for i, val in enumerate(values):
                if i not in walked:
                    walked.add(i)
                    dfs(v+val, w+weights[i], walked)
                    walked.remove(i)
            m = max(m, v)

        dfs(0, 0, walked)

        return m


class Solution2:
    def knapsack(self, values, weights, maxWeightConstraint):
        '''
        :type values: list of int
        :type weights: list of int
        :type maxWeightConstraint: int
        :rtype: int
        '''
        n = len(weights)
        dp = [[0]*(maxWeightConstraint+1) for _ in range(n+1)]

        for x in range(1, n+1):
            for y in range(1, maxWeightConstraint+1):
                w = weights[x-1]
                v = values[x-1]

                use_item = dp[x-1][y] if w > y else dp[x-1][y-w] + v
                not_use_item = dp[x-1][y]

                dp[x][y] = max(use_item, not_use_item)

        return dp[-1][-1]


if __name__ == "__main__":
    assert 80 == Solution2().knapsack([60, 50, 70, 30], [5, 3, 4, 2], 5)
