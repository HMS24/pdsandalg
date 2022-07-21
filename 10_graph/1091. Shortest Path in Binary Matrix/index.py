"""https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""

# Approach 1 dfs
# Time Limit Exceeded


from collections import deque


class Solution1:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        for i in range(n):
            if grid[i][i] != 0:
                break
        else:
            return n

        minimums = []
        steps = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                 (1, 0), (1, -1), (0, -1), (-1, -1)]
        visited = [[False for _ in range(n)] for _ in range(n)]

        def walk(row, column, path=1):
            if (row, column) == (n-1, n-1):
                minimums.append(path)
                return

            neighbors = []
            for step in steps:
                x = row + step[0]
                y = column + step[1]
                if x < 0 or y < 0:
                    continue
                if x > n-1 or y > n-1:
                    continue
                if visited[x][y]:
                    continue
                if grid[x][y] == 1:
                    continue
                neighbors.append((x, y))

            for x, y in neighbors:
                visited[x][y] = True
                walk(x, y, path+1)
                visited[x][y] = False

        visited[0][0] = True
        walk(0, 0)
        return min(minimums) if minimums else -1

# Approach 2 bfs


class Solution2:
    def shortestPathBinaryMatrix(self, grid):
        # edge case
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # 斜線最短
        n = len(grid)
        for i in range(n):
            if grid[i][i] == 1:
                break
        else:
            return n

        steps = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                 (1, 0), (1, -1), (0, -1), (-1, -1)]
        visited = set()
        pathes = [(0, 0, 1)]
        visited.add((0, 0))

        while pathes:
            row, column, shortest_path = pathes.pop(0)
            if (row, column) == (n-1, n-1):
                return shortest_path

            for step in steps:
                x = row + step[0]
                y = column + step[1]
                # 超出邊界
                if x not in range(n) or y not in range(n):
                    continue
                if grid[x][y] == 1:
                    continue
                # 如果之前走過代表相較路徑短，不用再走
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                pathes.append((x, y, shortest_path+1))
        return -1

# Approach 3 bfs improved


class Solution3:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        for i in range(n):
            if grid[i][i] == 1:
                break
        else:
            return n

        steps = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                 (1, 0), (1, -1), (0, -1), (-1, -1)]
        visited = set()
        pathes = [(0, 0, 1)]
        visited.add((0, 0))

        # 在 pathes queue 裡的 elem 都是同一批，可以一次走完
        for path in pathes:
            row, column, shortest_path = path
            if (row, column) == (n-1, n-1):
                return shortest_path

            for step in steps:
                x = row + step[0]
                y = column + step[1]
                if x not in range(n) or y not in range(n):
                    continue
                if grid[x][y] == 1:
                    continue
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                pathes.append((x, y, shortest_path+1))

        return -1

# Approach 4 bfs improved again


class Solution4:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        for i in range(n):
            if grid[i][i] == 1:
                break
        else:
            return n

        steps = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                 (1, 0), (1, -1), (0, -1), (-1, -1)]
        visited = set()
        pathes = [(0, 0, 1)]
        visited.add((0, 0))

        while pathes:
            # 在 pathes queue 裡的 elem 都是同一批，可以一次走完
            for _ in pathes:
                # 原本沒有 pop 掉，重複執行
                row, column, shortest_path = pathes.pop(0)
                if (row, column) == (n-1, n-1):
                    return shortest_path

                for step in steps:
                    x = row + step[0]
                    y = column + step[1]
                    if x not in range(n) or y not in range(n):
                        continue
                    if grid[x][y] == 1:
                        continue
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    pathes.append((x, y, shortest_path+1))

        return -1

# Approach 5 bfs improved again again


class Solution5:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        if n == 1:
            return 1

        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                      [0, 1], [1, -1], [1, 0], [1, 1]]

        togo = deque([(0, 0)])
        steps = 0
        while togo:
            # 同樣距離的點 同一批次執行
            for _ in range(len(togo)):
                r, c = togo.popleft()
                if r == n-1 and c == n-1:
                    return steps + 1
                for dr, dc in directions:
                    # 8 個方向都試
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        # 標記為牆壁 並且加入togo
                        grid[nr][nc] = 1
                        togo.append((nr, nc))
            steps += 1
        return -1
