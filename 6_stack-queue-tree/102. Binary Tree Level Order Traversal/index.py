"""https://leetcode.com/problems/clone-graph/
"""

# Approach 1 Recursion
class Solution_1:
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans

        for depth in range(0, 2000):
            results = []
            self.getNodeValuesByDepth(depth, root, results)
            if not results:
                break
            ans.append(results)
        return ans
            
        
    def getNodeValuesByDepth(self, depth, root, results):
        if depth == 0:
            results.append(root.val)
            return
        if root.left:
            self.getNodeValuesByDepth(depth-1, root.left, results)
        if root.right:
            self.getNodeValuesByDepth(depth-1, root.right, results)

# n
# nlogn
# Approach 2 Recursion improve
class Solution_2:
    def levelOrder(self, root):
        if not root:
            return []

        nodes = [root]
        results = [[root.val]]
        return self.getChildNodes(nodes, results)

    def getChildNodes(self, nodes, results):
        child_nodes = []
        child_node_vals = []
        for node in nodes:
            if node.left:
                child_nodes.append(node.left)
                child_node_vals.append(node.left.val)
            if node.right:
                child_nodes.append(node.right)
                child_node_vals.append(node.right.val)

        if not child_nodes:
            return results

        results.append(child_node_vals)
        return self.getChildNodes(child_nodes, results)

# Approach 3 Iterate
class Solution_2:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        levels = [root]
        while levels:
            res.append([level.val for level in levels])
            levels = [node for level in levels for node in (level.left, level.right) if node]
        return res