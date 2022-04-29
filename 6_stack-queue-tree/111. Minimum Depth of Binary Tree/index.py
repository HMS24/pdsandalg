"""https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1 Recursion 深度優先
"""
如果有左子樹，則遞迴算出左子樹高度
如果有右子樹，則遞迴算出右子樹高度
如果只有左子樹，回傳右邊高度
如果只有右子樹，回傳左邊高度
因為是算跟 leaf node 的高度，根不算
"""

class Solution_1:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def get_height(node, h=1):
            if node is None:
                return 0
            left_h = get_height(node.left, h+1) if node.left else h
            right_h = get_height(node.right, h+1) if node.right else h

            if node.left is None and node.right:
                return right_h
            elif node.right is None and node.left:
                return left_h
            else:
                return min(left_h, right_h)

        return get_height(root)

# Approach 2 Recursion 深度優先 優化！
"""
"""

class Solution_2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
                return 0
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1