"""https://leetcode.com/problems/min-cost-climbing-stairs/
"""

# Dynamic


class Solution1:
    def minCostClimbingStairs(self, cost):
        length = len(cost)
        cache = [None] * length
        cache[0], cache[1] = cost[0], cost[1]

        for i in range(2, length):
            cache[i] = min(cache[i-1], cache[i-2]) + cost[i]

        return min(cache[-1], cache[-2])
