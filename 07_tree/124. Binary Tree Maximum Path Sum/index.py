"""https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1 recursion
"""
1. 有可能經過 root
2. 在左邊或在右邊
算左右兩邊的最大值
如果負數就取 0
再將鄰近三角形的節點相加
記下來為最大值
之後每個三角形節點都跟它比較（有可能出現在單邊）
最後回傳 root.val + max(left, right)
"""

class Solution_1:
    # negative infinity
    maxResult = float('-inf')
    def maxPathSum(self, root):
        self.postOrder(root)
        return self.maxResult

    def postOrder(self, root):
        if not root:
            return 0
        left = max(0, self.postOrder(root.left))
        right = max(0, self.postOrder(root.right))
        self.maxResult = max(self.maxResult, root.val+left+right)
        return root.val + max(left, right)
        

r = TreeNode(
    -10,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7),
    )
)

s = Solution_1()
print(s.maxPathSum(r))