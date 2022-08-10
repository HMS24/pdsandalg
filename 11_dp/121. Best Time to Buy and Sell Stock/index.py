"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution1:
    """
    Dynamic Programming

    兩種選擇
    * extend previous 也就是不賣時的最佳獲利, 前一天的 max profit + 今天才賣的 profit
    * buy that day 那麼最佳獲利就是 0

    base case
    第一天買所以為 0

    i.e.
            [7, 1, 5, 3, 6, 4]
    opts =  [0, 0, 4, 2, 5, 3]
    """

    def maxProfit(self, prices):
        max_profit = 0
        n = len(prices)
        opts = [0 for _ in range(n)]

        for i in range(1, n):
            opts[i] = max(0, opts[i-1] + (prices[i]-prices[i-1]))
            max_profit = max(max_profit, opts[i])

        return max_profit
