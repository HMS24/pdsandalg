"""
https://leetcode.com/problems/path-sum-ii/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# Approach 1 dfs
"""
加總和等於目標值且無左右子樹:
    終止遞迴
有左子樹:
    往左加總，紀錄 path
有右子樹
    往右加總，紀錄 path

時間複雜度: 
    要將 n 個數字都走訪過，需耗費 O (n)。
空間複雜度:
    function call stack 也會耗費 O (k)，k 為樹的高度。
"""
class Solution_1:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        results = []
        self.dfs(root, targetSum, [root.val], 0+root.val, results)
        return results

    def dfs(self, root, targetSum, path, pathSum, results):
        if pathSum == targetSum and not root.left and not root.right:
            results.append(path[:])
            return
        if root.left:
            self.dfs(root.left, targetSum, path+[root.left.val], pathSum+root.left.val, results)
        if root.right:
            self.dfs(root.right, targetSum, path+[root.right.val], pathSum+root.right.val, results)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

r = TreeNode(
    5,
    TreeNode(
        4,
        TreeNode(1),
        TreeNode(9),
    ),
    TreeNode(
        8,
        TreeNode(2),
        TreeNode(5),
    )
)

s = Solution_1()
res = s.pathSum(r, 18)
print(res)