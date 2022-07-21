"""
https://leetcode.com/problems/path-sum-ii/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# Approach 1 dfs


class Solution1:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        results = []

        def dfs(root, path, rest_num):
            if not root.left and not root.right and rest_num == 0:
                return results.append(path[:])

            # 參數 copy 一份 list 不斷新增 list，對記憶體負擔較大。
            if root.left:
                dfs(root.left, path+[root.left.val], rest_num-root.left.val)

            if root.right:
                dfs(root.right, path+[root.right.val], rest_num-root.right.val)

        dfs(root, [root.val], targetSum-root.val)

        return results

# Approach 2 dfs improve


class Solution2:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        results = []

        def dfs(root, path, rest_num):
            if not root:
                return
            # notice ! rest_num == root.val
            if not root.left and not root.right and rest_num == root.val:
                return results.append(path[:]+[root.val])

            # backtracking
            path.append(root.val)
            dfs(root.left, path, rest_num-root.val)
            dfs(root.right, path, rest_num-root.val)
            path.pop(-1)

        dfs(root, [], targetSum)

        return results

# Approach 3 iteration using queue


class Solution3:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        results = []
        queue = [[root, [root.val], targetSum-root.val]]
        while queue:
            node, path, rest_num = queue.pop(0)
            if rest_num == 0 and not node.left and not node.right:
                results.append(path)
            if node.left:
                queue.append(
                    [node.left, path+[node.left.val], rest_num-node.left.val]
                )
            if node.right:
                queue.append(
                    [node.right, path+[node.right.val], rest_num-node.right.val]
                )

        return results

# Approach 4 iteration using queue


class Solution4:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        results = []
        queue = [[root, [root.val], targetSum-root.val]]
        while queue:
            for _ in range(len(queue)):
                node, path, rest_num = queue.pop(0)
                if rest_num == 0 and not node.left and not node.right:
                    results.append(path)
                if node.left:
                    queue.append(
                        [node.left, path+[node.left.val], rest_num-node.left.val]
                    )
                if node.right:
                    queue.append(
                        [node.right, path+[node.right.val], rest_num-node.right.val]
                    )

        return results
