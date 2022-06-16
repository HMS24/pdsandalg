"""https://leetcode.com/problems/binary-tree-inorder-traversal/
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
有左邊
    遞迴左
append val
有右邊
    遞迴右
"""

class Solution_1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recurse(root):
            if root.left:
                recurse(root.left)
            ans.append(root.val)
            if root.right:
                recurse(root.right)

        if root:
            recurse(root)
        return ans

# Approach2 Iterate
"""
1. stack 存走過的 node
2. 往最左下走
3. 沒有 node 就 pop stack 裡的 node
4. 將被 pop 的 node 存入 ans []
5. 往被 pop 的 node 右邊走
"""

class Solution_2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                ans.append(node.val)
                root = node.right

        return ans