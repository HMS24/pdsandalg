## Approach 1

DFS
Time Limit Exceeded

* 從 8 個方向找出可以走的元素位置 walkable list
    * 不超出邊界
    * 元素值非為 1
    * 沒有走過
* iterate walkable list 利用 backtracking 逐步遞迴往下走，直到抵達 (n-1, n-1) 紀錄 shortest_path
    * 紀錄正在走
    * 遞迴
    * 回溯紀錄
* min(shortest_path_list) else -1
* edge case: grid[0][0] or grid[-1][-1] 等於 1
* 先找斜線看看，如果均為 0 即最短

```python
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
```

## Approach 2

BFS
像倒水一樣，從 (0,0) 開始倒，逐漸往外往下流動，放進 queue 裡一層一層往外計算。

* 取出 queue 的 1 個 path，然後從 ８ 個方向找可以走的方向 append 進 queue
* 用 set 紀錄已走過的位置，或者直接修改 grid 為 1
* 直到取的位置為終點

```python
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
```

## Approach 3

BFS improved

improve approach 2，因為在 queue 裡的 path 都是同一批的擴散，直接 iterate 就好。

```python
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
```