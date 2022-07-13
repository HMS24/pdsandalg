## Approach 1

DFS

用 hashmap 記住新增的 node，並且 iterate node neighbors，
最後針對新創 node 的 neighbors append recursion 後的 node。

終止條件為當 hashmap 已有 node 時直接回傳

```python
class Solution1:
    def cloneGraph(self, node):
        visited = {}

        def clone(node):
            if visited.get(node.val, None):
                return visited[node.val]

            copied_node = Node(node.val)
            visited[node.val] = copied_node

            for neighbor in node.neighbors:
                copied_node.neighbors.append(clone(neighbor))

            return copied_node

        return clone(node) if node else None
```

## Approach 2

BFS

一樣使用 hashmap 紀錄已經創造的 node，搭配 queue iterate 取出 node，
然後新增 node 到 hashmap，接下來 iterate neighbors，如果沒有 visited 則 append into queue，
最後 append into new node neighbors。

```python
class Solution2:
    def cloneGraph(self, node):
        if not node:
            return

        visited = {}
        queue = [node]

        while queue:
            curr = queue.pop(0)
            if curr.val not in visited:
                visited[curr.val] = Node(curr.val)

            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr.val].neighbors.append(visited[neighbor.val])

        return visited[node.val]
```