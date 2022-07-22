## Approach 1

DFS

從 root 節點往子節點利用 DFS 進行深度搜索，每次記錄當前的值總和與路徑，若遇到 leaf 則判斷總和是否和 sum 相等。

<div style="margin:30px 0px"><img src="https://i.imgur.com/cMc6e1N.jpg" alt="_note" width="40%" height="30%"/></div>

* 加總和等於目標值且無左右子樹
    * 終止遞迴
* 有左子樹:
    * 往左加總，記錄 path
* 有右子樹
    * 往右加總，記錄 path

```python
class Solution1:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        results = []

        def dfs(root, path, rest_num):
            if not root.left and not root.right and rest_num == 0:
                return results.append(path[:])

            # 參數 copy 一份 list 不斷新增 list，對記憶體負擔較大。
            if root.left:
                dfs(root.left, path+[root.left.val], rest_num-root.left.val)

            if root.right:
                dfs(root.right, path+[root.right.val], rest_num-root.right.val)

        dfs(root, [root.val], targetSum-root.val)

        return results
```

#### 時間複雜度:
要將 n 個數字都走訪過，需耗費 $\mathcal{O}(n)$。

#### 空間複雜度:
最差情況 function call stack 也會耗費 $\mathcal{O}(n)$。

#### 備註:
原本多了加總大於目標值即 return 的終止條件，但題目有包含負數，因此得跑完至 leaf node 才能判斷。

## Approach 2

DFS improved

在 function 裡 copy list，記憶體負擔大，利用 backtracking append and pop 增進空間使用效率。
另外當我們走到 leaf 時， rest_num 和 leaf node 本身的值相同，才有解。

```python
class Solution2:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        results = []

        def dfs(root, path, rest_num):
            if not root:
                return
            # notice: rest_num == root.val
            if not root.left and not root.right and rest_num == root.val:
                return results.append(path[:]+[root.val])

            # backtracking
            path.append(root.val)
            dfs(root.left, path, rest_num-root.val)
            dfs(root.right, path, rest_num-root.val)
            path.pop(-1)

        dfs(root, [], targetSum)

        return results
```

## Approach 3

Iteration using queue

```python
class Solution3:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        results = []
        queue = [[root, [root.val], targetSum-root.val]]
        while queue:
            node, path, rest_num = queue.pop(0)
            if rest_num == 0 and not node.left and not node.right:
                results.append(path)
            if node.left:
                queue.append(
                    [node.left, path+[node.left.val], rest_num-node.left.val]
                )
            if node.right:
                queue.append(
                    [node.right, path+[node.right.val], rest_num-node.right.val]
                )

        return results
```

#### 時間複雜度： 
要將 n 個數字都走訪過，需耗費 $\mathcal{O}(n)$。

#### 空間複雜度：
用 queue 存所有節點的內容，需耗費 $\mathcal{O}(n)$。

#### 思考
把所有節點都算出需要的內容，放進 queue 裡再一個一個取出判斷。
why use queue?，因為要由上往下 append 走過的路徑，為 BFS
    
## Approach 4

Iteration using queue improved

append 進 queue 裡的都是同一 level 的 nodes，可以一起跑完。

```python
class Solution4:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        results = []
        queue = [[root, [root.val], targetSum-root.val]]
        while queue:
            for _ in range(len(queue)):
                node, path, rest_num = queue.pop(0)
                if rest_num == 0 and not node.left and not node.right:
                    results.append(path)
                if node.left:
                    queue.append(
                        [node.left, path+[node.left.val], rest_num-node.left.val]
                    )
                if node.right:
                    queue.append(
                        [node.right, path+[node.right.val], rest_num-node.right.val]
                    )

        return results
```