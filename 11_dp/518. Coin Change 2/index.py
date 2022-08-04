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
