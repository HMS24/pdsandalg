"""https://leetcode.com/problems/balance-a-binary-search-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1 Recursion 不穩定的解法，有時無法平衡
"""
1. 算左右子樹高度差
2. 辨別不平衡的型態
3. 依照型態旋轉
"""

class Solution_1:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.reBalance(root)
        root = self.fixImbalance(root)
        return root

    def getHeight(self, root: TreeNode, h: int = 0) -> int:
        l = self.getHeight(root.left, h+1) if root.left else h
        r = self.getHeight(root.right, h+1) if root.right else h
        return max(l, r)

    def getLeftRightHeightDifference(self, root: TreeNode) -> int:
        l = self.getHeight(root.left)+1 if root.left else 0
        r = self.getHeight(root.right)+1 if root.right else 0
        return l-r

    def rotateRight(self, root: TreeNode) -> TreeNode:
        pivot = root.left
        reattachNode = pivot.right
        pivot.right = root
        root.left = reattachNode
        return pivot

    def rotateLeft(self, root: TreeNode) -> TreeNode:
        pivot = root.right
        reattachNode = pivot.left
        pivot.left = root
        root.right = reattachNode
        return pivot

    def fixImbalance(self, root: TreeNode) -> TreeNode:
        d = self.getLeftRightHeightDifference(root)
        if d > 1:
            if self.getLeftRightHeightDifference(root.left) > 0:
                return self.rotateRight(root)
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)
        elif d < -1:
            if self.getLeftRightHeightDifference(root.right) < 0:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)
        return root

    def reBalance(self, root: TreeNode) -> None:
        if root.left:
            self.reBalance(root.left)
            root.left = self.fixImbalance(root.left)
        if root.right:
            self.reBalance(root.right)
            root.right = self.fixImbalance(root.right)

# Approach 2 最穩定的解法
"""
1. 由小到大排序，中序遍歷
2. 從中間開始依序放入左右子樹
"""

class Solution_2:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        nodes = []

        def in_order_traverse(root):
            if root.left:
                in_order_traverse(root.left)
            nodes.append(root.val)
            if root.right:
                in_order_traverse(root.right)

        in_order_traverse(root)

        def balance(left, right):
            if left > right:
                return
            mid = (left+right)//2
            root = TreeNode(nodes[mid])
            root.left = balance(left, mid-1)
            root.right = balance(mid+1, right)
            return root

        return balance(0, len(nodes)-1)
            
root = TreeNode(30, TreeNode(20, TreeNode(10, TreeNode(9), TreeNode(11)), TreeNode(21)))