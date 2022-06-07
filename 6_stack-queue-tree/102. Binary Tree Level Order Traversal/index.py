"""https://leetcode.com/problems/clone-graph/
"""

# Approach 1 Recursion
class Solution:
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
        