"""
https://leetcode.com/problems/path-sum-ii/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# Approach 1 dfs
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


# Approach 2 iteration using queue
class Solution_2:
    def pathSum(self, root, targetSum):
        results = []
        queue = []
        queue.append([root, [root.val], root.val])
        while queue:
            node, path, sum = queue.pop(0)
            if sum == targetSum and not node.left and not node.right:
                results.append(path)
            if node.left:
                queue.append([node.left, path+[node.left.val], sum+node.left.val])
            if node.right:
                queue.append([node.right, path+[node.right.val], sum+node.right.val])

        return results


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

s = Solution_2()
res = s.pathSum(r, 18)
print(res)