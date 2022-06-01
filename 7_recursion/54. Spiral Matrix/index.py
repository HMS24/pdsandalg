"""https://leetcode.com/problems/spiral-matrix/
"""

# Approach 1 recursion
class Solution_1:
    def spiralOrder(self, matrix):
        # 從第一個開始，先加入 results 及座標，螺旋時都只會判斷下一個
        first = matrix[0][0]
        results = [first]
        pathed_set = set()
        pathed_set.add('00')

        m = len(matrix)
        n = len(matrix[0])
        count = m * n

        def spiraled(row, column):
            # results 已經包含矩陣所有數字，終止。
            if count == len(results):
                return

            # 右，colum+1 就是從下一個開始到 column 數量
            for j in range(column+1, n):
                num = matrix[row][j]
                spot = f'{row}{j}'
                if spot in pathed_set:
                    break
                pathed_set.add(spot)
                results.append(num)
                # 記錄目前矩陣座標 
                column = j
            
            # 下 row+1 到 row 數量
            for i in range(row+1, m):
                num = matrix[i][column]
                spot = f'{i}{column}'
                if spot in pathed_set:
                    break
                pathed_set.add(spot)
                results.append(num)
                row = i

            # 左 column-1 到 0，倒著數回來
            for j in range(column-1, 0-1, -1):
                num = matrix[row][j]
                spot = f'{row}{j}'
                if spot in pathed_set:
                    break
                pathed_set.add(spot)
                results.append(num)
                column = j            

            # 上 row-1 到 0，倒著數回來
            for i in range(row-1, 0-1, -1):
                num = matrix[i][column]
                spot = f'{i}{column}'
                if spot in pathed_set:
                    break
                pathed_set.add(spot)
                results.append(num)
                row = i

            # 下一輪
            spiraled(row, column)

        spiraled(0, 0)
        return results
