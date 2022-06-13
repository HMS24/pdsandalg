"""https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""

# Approach 1 dfs
# Time Limit Exceeded
class Solution_1:
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
        steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
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
class Solution_2:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        for i in range(n):
            if grid[i][i] == 1:
                break
        else:
            return n
        
        steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
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
                if x not in range(n) or y not in range(n):
                    continue
                if grid[x][y] == 1:
                    continue
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                pathes.append((x, y, shortest_path+1))
        return -1
