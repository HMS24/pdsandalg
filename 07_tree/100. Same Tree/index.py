"""https://leetcode.com/problems/same-tree/
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
用中序遍歷，再比較 tree 的 val，沒有子樹要補 None
1. 找樹的最大高度
2. 中序遍歷
3. 無子樹補 None
4. 比較 list
"""

class Solution_1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        pMaxHeight = self.getMaxHeight(p)
        qMaxHeight = self.getMaxHeight(q)
        pInorder = self.inorderTraversal(p, pMaxHeight, [])
        qInorder = self.inorderTraversal(q, qMaxHeight, [])
        
        if len(pInorder) != len(qInorder):
            return False
        
        for i in range(len(pInorder)):
            if pInorder[i] != qInorder[i]:
                return False
        return True

    def getMaxHeight(self, root, h=0):
        leftHeight = self.getMaxHeight(root.left, h+1) if root.left else h
        rightHeight = self.getMaxHeight(root.right, h+1) if root.right else h
        return max(leftHeight, rightHeight)

    def inorderTraversal(self, root, depth, nodes=[]):
        if depth == 0:
            nodes.append(root.val)
            return nodes

        if root.left:
            self.inorderTraversal(root.left, depth-1, nodes)
        else:
            nodes.extend([None]*(2**depth-1))
        
        nodes.append(root.val)
        
        if root.right:
            self.inorderTraversal(root.right, depth-1, nodes)
        else:
            nodes.extend([None]*(2**depth-1))
        return nodes

# Approach 2 Recursion
"""
每個節點遞迴就好
"""
class Solution_2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
