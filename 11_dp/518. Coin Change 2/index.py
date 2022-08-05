"""https://leetcode.com/problems/coin-change-2/
"""

from typing import List


class Solution1:
    """
    暴力法
    直接 recurse 所有組合
    直到 amount 為 0 base case
    用 set 紀錄不重複的 path

    Time Limit Exceeded

    時間複雜度: O(n * amount^len(coins))
    最壞情況，每個 node 都要 for loop len(coins) 次數
    tree 的深度 為當 coin value 為 1 的時候
    然後每個 node 都要 copy 而且 sort
    慘不忍睹

    空間複雜度: O(amount)
    function call stack
    當 coin value 為 1 時，tree 的深度

    """

    def change(self, amount: int, coins: List[int]) -> int:
        cache = set()

        def dfs(amount, path):
            if amount == 0:
                p = path[:]
                cache.add(tuple(sorted(p)))
                return

            for coin in coins:
                if amount < coin:
                    break
                path.append(coin)
                dfs(amount-coin, path)
                path.pop()

        dfs(amount, [])
        return len(cache)



class Solution2:
    """
    Dynamic Programming

    cache 記住組合的 ways
    例如 target = 5 coins = [1, 2, 5]
    cache_ways 如下

    coin set \ amount

                0   1   2   3   4   5
    []          1   0   0   0   0   0
    [1]         1   1   1   1   1   1
    [1, 2]      1   1   2   2   3   3
    [1, 2, 5]   1   1   2   2   3   4

    考慮 [1, 2] amount = 4 時
    可以分成
        without 2
            [1] amount = 4 有 1 種
        with 2
            [1, 2] amount = 2 有 2 種
    總共有 3 種組合 [1, 1, 1, 1], [1, 2, 2], [1, 1, 2]
    """

    def change(self, amount, coins):
        rows = len(coins) + 1
        columns = amount + 1

        # row: 考慮第 row 個 coin for use
        # column: 該 row 所有 coin 組合出的 amount
        ways_cache = [[0] * columns] * rows

        # base case: 可以組合 amount=0 的方法只有 1 種 就是 empty set
        for row in range(rows):
            ways_cache[row][0] = 1

        for row in range(1, rows):
            coin_value = coins[row-1]
            for _amount in range(1, columns):
                without_this_coin = ways_cache[row-1][_amount]
  
                with_this_coin = 0
                if coin_value <=_amount:
                    with_this_coin = ways_cache[row][_amount-coin_value]

                ways_cache[row][_amount] = without_this_coin + with_this_coin

        return ways_cache[rows-1][amount]
