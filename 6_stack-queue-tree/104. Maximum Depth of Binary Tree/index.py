"""https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach1 Recursion
"""
如果有左子樹，則遞迴算出左子樹高度
如果有右子樹，則遞迴算出右子樹高度
回傳左右子樹高度最大者
"""

class Solution_1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_height(node, h=1):
            left_h = get_height(node.left, h+1) if node.left else h
            right_h = get_height(node.right, h+1) if node.right else h
            return max(left_h, right_h)

        if root is None:
            return 0
        return get_height(root)