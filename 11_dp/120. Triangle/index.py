"""https://leetcode.com/problems/triangle/
"""


class Solution1:
    """
    Dynamic Programming

    # 1
    from top to down
    很難獲得哪一條才是最短 cost
    需要跑過所有路徑
    最後在比較誰 cost 最少

    # 2
    from bottom to up
    可以試著從結束那一層開始
    層層往上找最少 cost 的

    i.e.
        [
            [5],
            [1, 6],
            [4, 3, 10],
            [3, 2, 4, 1]
        ]

        step1
        從最後一層
        cache = [3, 2, 4, 1]

        step2
        cache = [6, 5, 11, 1]
            * 4 開始往下有(3, 2) cost 最少？ 2
              cache[0] = 4+2
            * 3 開始往下有(2, 4) cost 最少？ 2
              cache[1] = 3+2
            * 10 開始往下有(4, 1) cost 最少？ 1
              cache[2] = 10+1

        step3
        cache = [6, 11, 11, 1]
            * 1 開始往下有(6, 5) cost 最少？ 5
              cache[0] = 1+5
            * 6 開始往下有(5, 11) cost 最少？ 5
              cache[1] = 6+5

        step4
        cache = [11, 11, 11, 1]
            * 5 開始往下有(6, 11) cost 最少？ 6
              cache[0] = 5+6

        step5
        return cache[0] 11
    """

    def minimumTotal(self, triangle):
        n = len(triangle)
        path_cost_cache = triangle[n-1][:]

        for i in range(n-1):
            # 要從倒數二層開始往 root 跑
            layer = triangle[n-2-i]

            for j, val in enumerate(layer):
                left = val + path_cost_cache[j]
                right = val + path_cost_cache[j+1]

                # 左右兩條路徑哪條最短？
                path_cost_cache[j] = min(left, right)

        return path_cost_cache[0]
