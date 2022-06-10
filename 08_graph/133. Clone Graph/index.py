"""https://leetcode.com/problems/clone-graph/
"""

# Approach 1 dfs
class Solution_1:
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

# Approach 2 bfs
class Solution_2:
    def cloneGraph(self, node):
        if not node:
            return
        visited = {}
        queue = [node]
        visited[node.val] = Node(node.val)
        
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
