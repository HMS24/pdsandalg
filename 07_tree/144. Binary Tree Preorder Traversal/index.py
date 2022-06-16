"""https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

from helper import TreeNode

# 2^n
# logn
# Approach 1 Recursion
class Solution_1:
    def preorderTraversal(self, root):
        res = []
        def traverse(root):
            if not root:
                return
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return res

# n
# n
# Approach 2 Iteration
class Solution_2:
    def preorderTraversal(self, root):
        res = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
