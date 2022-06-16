"""https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1 recursioin
"""
找到兩個節點的路徑
比較路徑長短
依序從後判斷短的路徑元素是否在長的路徑
若是就找到了
但速度很慢...
"""

class Solution_1:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = self.find_path(root, p)
        q_path = self.find_path(root, q)

        if len(p_path) <= len(q_path):
            short_path_list, long_path_set = p_path, set(q_path)
        else:
            short_path_list, long_path_set = q_path, set(p_path)

        for i in range(-1, -len(short_path_list)-1, -1):
            if short_path_list[i] in long_path_set:
                return short_path_list[i]

    def dfs(self, path, target, res):
        curr = path[-1]
        if curr.val == target.val:
            res.extend(path)
        if curr.left and not res:
            self.dfs(path+[curr.left], target, res)
        if curr.right and not res:
            self.dfs(path+[curr.right], target, res)
        return res

    def find_path(self, root, target):
        res = []
        self.dfs([root], target, res)
        return res
        
        

r = TreeNode(
    3,
    TreeNode(
        5,
        TreeNode(6),
        TreeNode(
            2,
        TreeNode(7),
        TreeNode(4), 
        ),
    ),
    TreeNode(
        1,
        TreeNode(0),
        TreeNode(8),
    )
)


s = Solution_1()
result = s.lowestCommonAncestor(r, TreeNode(7), TreeNode(4))
print(result)