"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution1:
    """
    Dynamic Programming

    兩種 ways
    * 上面走下來
    * 左邊走過來

    base case
    一開始走到 matrix 左右邊緣的點都只有 1 種方法

    i.e.
        m = 3
        n = 3
        s -> "start"
        e -> "end"
         -----------
        | s | _ | _ |
        | _ | _ | _ |
        | _ | _ | e |
         -----------

        base case
         -----------
        | 1 | 1 | 1 |
        | 1 | _ | _ |
        | 1 | _ | _ |
         -----------

        solution
         -----------
        | 1 | 1 | 1 |
        | 1 | 2 | 3 |
        | 1 | 3 | 6 |
         -----------
    """

    def uniquePaths(self, m, n):
        unique_paths_to_position = [[1 for _ in range(n)] for _ in range(m)]

        for x in range(1, m):
            for y in range(1, n):
                unique_ways_to_above_cell = unique_paths_to_position[x-1][y]
                unique_ways_to_left_cell = unique_paths_to_position[x][y-1]

                unique_paths_to_position[x][y] = unique_ways_to_above_cell + unique_ways_to_left_cell

        return unique_paths_to_position[-1][-1]
