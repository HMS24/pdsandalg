"""https://leetcode.com/problems/coin-change/
"""


class Solution1:
    """
    Dynamic Programming

    for amount 從 0 到 target amount
    1 個 coin 慢慢試
    當已放入 coin 時
    subamount 就會是 amount - coin value
    找到 subamount 的 least coin num
    最後 min(上一個 least coin num, 新找到的 least coin num)

    i.e.
    [1, 2, 5]
    amount = 10

    cache         0 1 2 3 4 5 6 7 8 9 10
    least coins   0 1 1 2 2 1 2 2 3 3 2

    對 amount 5 來說
    3 種 coin 都可以使用
    如果放了
      * coin 1:
        coin num = 1
        subamount = 4
        cache[4] 的 least coin num = 2
        目前 cache[5] best least coin num = 3

      * coin 2:
        coin num = 1
        subamount = 3
        cache[3] 的 best least coin num = 1
        目前 cache[5] best least coin num = 2

      * coin 5:
        coin num = 1
        subamount = 0
        cache[0] 的 best least coin num = 0
        目前 cache[5] best least coin num = 1
    """

    def coinChange(self, coins, amount):
        cache = [-1] * (amount+1)
        # base case
        cache[0] = 0

        for target_amount in range(1, amount+1):
            for coin_val in coins:
                # coin 無法組合 amount * 2 ways
                if coin_val > target_amount:
                    continue
                if cache[target_amount-coin_val] < 0:
                    continue

                with_coin_nums = 1 + cache[target_amount-coin_val]

                if cache[target_amount] < 0:
                    cache[target_amount] = with_coin_nums
                else:
                    cache[target_amount] = min(cache[target_amount], with_coin_nums)

        return cache[amount]
